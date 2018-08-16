import logging, re, os, getpass, base64, datetime
import requests, json
import itc_mapping, account

from string import Template

loglevel = 'INFO'
logging.basicConfig(format='%(levelname)s:%(message)s', level=loglevel, filename='app.log')

DATE_PATTERN = re.compile(r"""^(
  ((19|20)\d\d)-		# four digits for the year
  ((0|1)?\d)-			# one or two digits for the month
  ((0|1|2|3)?\d)		# one or two digits for the day
  ).*?$
  """, re.VERBOSE)

ENTRY_PATTERN = re.compile(r"""^
  (\d+):(\d+)\s*-\s*	# start time
  (\d+):(\d+):			# stop time
  (\s*)(.+?)(\s-\s(.+))?	# a space, ticket number/name of activity and additional comment
  $""", re.VERBOSE)

TICKET_PATTERN = re.compile(r'^\w+?-\d+?$')

TEMPLATE_DIR = 'payload_sample/'

ITC_URL='http://FIXME'

date = None
valuesDict = {'loginId': None, 'ticketRid': "", 'comment': "", 'startTime': None, 'endTime': None, 'date': None}

def promptUserCredential():
  loginId = input('Enter your loginId: ')
  passwd = getpass.getpass('Enter your password: ')
  credential = loginId + ":" + passwd
  credential = base64.b64encode(credential.encode()).decode()

  logging.debug("base 64 credential: %s", credential)

  valuesDict['loginId'] = loginId

  return credential

def parseEntry(mo):
  startTime = mo.group(1) + ':' + mo.group(2)
  endTime = mo.group(3) + ':' + mo.group(4)
  activity = mo.group(6)
  comment = mo.group(8)

  valuesDict['startTime'] = startTime
  valuesDict['endTime'] = endTime
  valuesDict['comment'] = comment

  mo = TICKET_PATTERN.search(activity)
  valuesDict['ticketRid'] = mo.group(0).upper() if mo else ''
  
  logging.debug('After parsing: %s', str(valuesDict))
  return activity

def preparePayload(templateFile, values):
  with open(templateFile) as fin:
    src = Template(fin.read())
    payload = src.substitute(values)
    return payload

def pickTemplate(ticket):
  key = 'nevismeta' if ticket.lower().startswith('nevismeta') else ticket
  return TEMPLATE_DIR + itc_mapping.template_mapping.get(key)

def sendRequest(payload, credential, entry):
  headers = {'Authorization' : credential, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
  resp = requests.post(ITC_URL, data=json.dumps(payload), headers=headers)
  logging.debug("Response: %s %s", resp.status_code, resp.text)
  if resp.status_code == 201:
    logging.info('Successful book entry: %s', entry)
  else:
    logging.error('Wasted: %s', entry)

def bookItc():
  logging.info('>> Start booking ITC: %s', datetime.datetime.now())
  credential = promptUserCredential()

  with open('itc_log') as logfile:
    for line in logfile:
      line = line.strip()
      if not line:
        continue

      # parse date
      mo = DATE_PATTERN.search(line)
      if mo:
        date = mo.group(1)
        valuesDict['date'] = date
        logging.info('Processing on date: %s', date)
        continue

      mo = ENTRY_PATTERN.search(line)
      if mo:
        activity = parseEntry(mo);
        templateFile = pickTemplate(activity)
        payload = preparePayload(templateFile, valuesDict) 

        # TODO: sending REST request
        logging.debug('Sending payload of %s', payload)
        sendRequest(payload, credential, line)

      else:
        logging.error('Skipping entry: %s', line)
    
  logging.info('<< End booking ITC: %s', datetime.datetime.now())
 
if __name__ == '__main__':
  bookItc()

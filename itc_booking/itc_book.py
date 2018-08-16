import logging, re, os, getpass, base64
import itc_mapping, account

from string import Template

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Start booking ITC')


DATE_PATTERN = re.compile(r"""^(
  ((19|20)\d\d)-		# four digits for the year
  ((0|1)?\d)-			# one or two digits for the month
  ((0|1|2|3)?\d)		# one or two digits for the day
  ).*?$
  """, re.VERBOSE)

ENTRY_PATTERN = re.compile(r"""^
  (\d+):(\d+)-			# start time
  (\d+):(\d+):			# stop time
  (\s*)(.+?)(\s-\s(.+))?	# a space, ticket number/name of activity and additional comment
  $""", re.VERBOSE)

TICKET_PATTERN = re.compile(r'^\w+?-\d+?$')

date = None
valuesDict = {'loginId': None, 'ticketRid': "", 'comment': "", 'startTime': None, 'endTime': None, 'date': None}

def promptUserCredential():
  loginId = input('Enter your loginId: ')
  passwd = getpass.getpass('Enter your password: ')
  credential = loginId + ":" + passwd
  credential = base64.b64encode(credential.encode()).decode()

  logging.debug("base 64 credential: " + credential)

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
  if mo:
    valuesDict['ticketRid'] = mo.group(0).upper()
  
  logging.debug('After parsing: ' + str(valuesDict))
  return activity

def preparePayload(templateFile, values):
  with open(templateFile) as fin:
    src = Template(fin.read())
    payload = src.substitude(values)
    return payload

def pickTemplate(ticket):
  key = 'nevismeta' if ticket.lower().startswith('nevismeta') else ticket
  return itc_mapping.template_mapping.get(key)

def bookItc():
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
        logging.info('Processing on date: ' + date)
        continue

      mo = ENTRY_PATTERN.search(line)
      if mo:
        activity = parseEntry(mo);
        templateFile = pickTemplate(activity)
        payload = preparePayload(templateFile, valuesDict) 

        # TODO: sending REST request
        logging.debug('Sending payload of ' + payload)

      else:
        logging.info('Skipping entry: ' + line)
 
if __name__ == '__main__':
  bookItc()

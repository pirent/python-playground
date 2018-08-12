#!/usr/bin/python3
import logging, re, os
import itc_mapping, account

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Start booking ITC')


DATE_PATTERN = re.compile(r"""^(
  ((0|1|2|3)?\d)-		# one or two digits for the day
  ((0|1)?\d)-			# one or two digits for the month
  ((19|20)\d\d)			# four digits for the year
  ).*?$
  """, re.VERBOSE)

ENTRY_PATTERN = re.compile(r"""^
  (\d+):(\d+)-			# start time
  (\d+):(\d+):			# stop time
  (\s*)(.+?)(\s-\s(.+))?	# a space, ticket number/name of activity and additional comment
  $""", re.VERBOSE)

date = None

# TODO: take account and password number

# TODO: find out how to use ITC token 

def parseEntry(mo):
  startTime = mo.group(1) + ':' + mo.group(2)
  endTime = mo.group(3) + ':' + mo.group(4)
  ticketNumber = mo.group(6)
  comment = mo.group(8)
  result = (startTime, endTime, ticketNumber, comment)
  logging.debug('Entry: ' + str(result))
  return result

def bookItc():
  with open('itc_log') as logfile:
    for line in logfile:
      line = line.strip()
      if not line:
        continue

      # parse date
      mo = DATE_PATTERN.search(line)
      if mo:
        date = mo.group(1)
        logging.info('Processing on date: ' + date)
        continue

      mo = ENTRY_PATTERN.search(line)
      if mo:
        startTime, endTime, ticket, comment = parseEntry(mo);
        key = 'nevismeta' if ticket.lower().startswith('nevismeta') else ticket
        workType, tag = itc_mapping.tag_mapping.get(key)
        logging.debug('Type of work is ' + str(workType))
        logging.debug('Tag is ' + str(tag))

        # TODO: sending REST request

      else:
        logging.info('Skipping entry: ' + line)
 
if __name__ == '__main__':
  bookItc()

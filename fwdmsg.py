import argparse
import smtplib
import sys

# Read arguments
parser = argparse.ArgumentParser(description='Forward messages via SMTP')
parser.add_argument(
    'infile',
    nargs='?',
    type=argparse.FileType('r'),
    default=sys.stdin,
    help='MIME-encoded email file(if empty, stdin will be used)')
parser.add_argument('--username', required=True)
parser.add_argument('--password', required=True)
parser.add_argument('--from_addr', required=True)
parser.add_argument('--to_addr', required=True)
parser.add_argument('--host', default='smtp.gmail.com')
parser.add_argument('--port', default='587', type=int)
args = parser.parse_args() 

# Read infile (is stdin if no arg)
stdin_data = args.infile.read()
args.infile.close()

# Send the message
server = smtplib.SMTP(args.host, args.port)
server.starttls()
server.login(args.username, args.password)
server.sendmail(args.from_addr, args.to_addr, stdin_data)
server.quit()

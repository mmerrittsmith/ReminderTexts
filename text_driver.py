import argparse
import config
from twilio.rest import Client

parser = argparse.ArgumentParser()
parser.add_argument('-r',
					'--recipient', 
					help='Key of the recipient in the \
                          Recipients dict, currently \
                          one of {"SO", "Self"}.',
                    type=str)
parser.add_argument('-m',
					'--message',
					help='String message that you want \
					      to send. Can be a string key \
					      to the messages dict.',
				    type=str)
args = parser.parse_args()


def parse():
	"""
	parse()
	Validate the command line args, and return the recipient phone # 
	and message.

	Gets: nothing
	Returns:
		recipient, a string
		message, a string
	"""
	if args.recipient not in config.RECIPIENTS:
		raise KeyError('Recipient not in config.RECIPIENTS')
	recipient = config.RECIPIENTS[args.recipient]

	if args.message in config.MESSAGES:
		message = config.MESSAGES[args.message]
	else:
		message = args.message

	return recipient, message


def send(recipient, message):
	"""
	send(recipient, message)
	Creates a Client instance and uses it to send a SMS message
	
	Gets:
		recipient, a string
		message, a string
	Returns: Nothing
	"""
	client = Client(config.SID, config.TWILIO_TOKEN)
	payload = client.messages.create(body=message, from_=config.TWILIO_NUMBER, to=recipient)


def main():
	recipient, message = parse()
	send(recipient, message)


if __name__ == '__main__':
	main()
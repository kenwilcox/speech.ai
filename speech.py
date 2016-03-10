import os
key = os.environ.get('OXFORD_SPEECH_KEY')
luis = os.environ.get('LUIS_URL')

if key is not None:
	from projectoxford.speech import SpeechClient
	sc = SpeechClient(key, gender="Female", locale="en-US")

	print = sc.print
	input = sc.input
else:
	print("Missing Env var: OXFORD_SPEECH_KEY")

print("Welcome to Ken's Pizza Place")
order = input("What can I get for you today? ")

print("You said: ", order)

if luis is not None:
	from projectoxford.luis import LuisClient
	from projectoxford.speech import join_and

	# The URL could be wrapped in quotes
	lc = LuisClient(luis.replace('"', ""))
	intent, toppings, _ = lc.query(order)

	if intent == "Pizza" and toppings:
		print("I will send you a pizza with", join_and(toppings))
	else:
		print("Sorry, we only sell pizza here.")
else:
	print("Set the LUIS_URL Env var to enable processing of your order")

print("Thank you for visiting Ken's Pizza Place!")
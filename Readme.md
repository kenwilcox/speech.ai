#PizzaShoppe

This is actually a fun project. It requires Python and currently only runs on Windows (library limitation)

## Get Started
- You need python installed and in your %PATH%, I'm using Python 3.5.1
- First Rename `setup.template.bat` to just `setup.bat` - it's in the `.gitignore` so you won't commit it to git
- Then go to [project oxford](http://www.projectoxford.ai/speech), sign up and get primary api key, and paste that in the `setup.bat` file replacing `YOUR_SPEECH_KEY`
- Then go to [LUIS](http://luis.ai)
	- sign up and click on New App, and import the `PizzaShoppe.json` file as a new application.
	- click train in the bottom left, once that's done
	- click publish in the upper left
	- click on Publish web service
	- copy and paste the given URL into the `setup.bat` file replacing the `YOUR_LUIS_URL`. Keep the quotes since Windows doesn't like the characters in the URL
- Whew - now open the project folder in the command prompt
- You need to install the projectoxford python library, you can do so by
	- type `pip install projectoxford` and press enter
- type `setup.bat` and press enter
- type `python speech.py` and press enter and enjoy the show

###Plug
[https://blogs.msdn.microsoft.com/pythonengineering/2016/02/15/talking-with-python-fabrikam-pizza-shack/](https://blogs.msdn.microsoft.com/pythonengineering/2016/02/15/talking-with-python-fabrikam-pizza-shack/)
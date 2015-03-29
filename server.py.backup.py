import mraa
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

home_dictionary = {'deadbolt': {'pin': 12, 'led':None}, 
		'garage': {'pin': 13, 'led':None}}
home_dictionary.get('deadbolt')

for key, value in home_dictionary:
	value['led'] = mraa.Gpio(value['pin'])
	value['led'].dir(mraa.DIR_OUT)


deadboltLED = 
deadboltLED.dir(mraa.DIR_OUT)

garageLED = mraa.Gpio(13)
garageLED.dir(mraa.DIR_OUT)

@app.route('/', methods=['GET', 'POST'])
def hello():
	if (request.method == 'POST'):
		posted_vars = request.form
		if 'garage' in posted_vars:
			set_garage(request.form.get('garage') == "on")
		if 'deadbolt' in posted_vars:
			set_deadbolt(request.form.get('deadbolt') == "on")

	return render_home(get_garage(), get_deadbolt())

def render_home(garage, deadbolt):
	"Show the home page."
	return render_template('home.html', garage=garage, deadbolt=deadbolt)

def get_deadbolt():
	return deadboltLED.read() == 1

def get_garage():
	return garageLED.read() == 1

def set_garage(garage):
	if garage:
		print "turning garage on"
		garagenum = 1
	else:
		print "turning garage off"
		garagenum = 0
	garageLED.write(garagenum)

def set_deadbolt(deadbolt):
	if deadbolt:
		deadboltnum = 1
	else:
		deadboltnum = 0
	deadboltLED.write(deadboltnum)

#@app.route('/led/<status>')
#def setStatus(status = None):
#	if (status == "on"):
#		led.write(1)
#	else:
#		led.write(0)
#	return render_template('home.html', garage, deadbolt)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')

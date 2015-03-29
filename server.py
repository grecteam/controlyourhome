# import mraa
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

home_dictionary = {
	'deadbolt': {'pin': 12, 'status': None, 'led': None}, 
	'garage': {'pin': 13, 'status': None, 'led': None}}

def get_status(key):
	# return home_dictionary[key]['led'].read() == 1
	return home_dictionary[key]['status']

def set_status(key, value):
	# home_dictionary[key]['led'].write(int(value))
	home_dictionary[key]['status'] = value

for key, value in home_dictionary.iteritems():
	# value['led'] = mraa.Gpio(value['pin'])
	# value['led'].dir(mraa.DIR_OUT)
	# set_status(key, get_status(key))
	set_status(key, True)

@app.route('/', methods=['GET', 'POST'])
def hello():
	if (request.method == 'POST'):
		posted_vars = request.form
		for key in posted_vars:
			set_status(key, request.form.get(key) == "on")

	return render_template('home.html', home_dictionary = home_dictionary)

@app.route('/about/')
def about():
	return render_template('about.html', home_dictionary = home_dictionary)

@app.route('/contact/')
def contact():
	return render_template('contact.html', home_dictionary = home_dictionary)

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

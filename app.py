from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from Algcomposer import *
import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('main_page.html')

@app.route('/submit', methods=['POST'])
def perform_script():
	option = request.form["options"]
	root = request.form["root"]
	scale = request.form["scale"]
	song = request.form["guitar_tab"]
	jumps = [2,2,1,2,2,2,1] #just in case I messed up
	if scale == "major":
		jumps = [2,2,1,2,2,2,1]
	elif scale == "minor":
		jumps = [2,1,2,2,1,2,2]

	if option == 'ck':
		output = go_through_file(song, get_scale([0,7,2,9,5,0],jumps), option)
	if option == 'ckr':
		output = go_through_file(song, get_scale([0,7,2,9,5,0],jumps), 'ck', 5)
	
	return output 

@app.route('/success')
def sucess_page():
	return render_template('success.html')

@app.route('/naughty')
def naughty_page():
	return render_template('naughty.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)


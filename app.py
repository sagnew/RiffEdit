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
	root = request.form["root"]
	scale = request.form["scale"]
	song = request.form["guitar_tab"]
	#return redirect('/success', 301)
	return root + " " + scale + " " + song + " "

@app.route('/success')
def sucess_page():
	return render_template('success.html')

@app.route('/naughty')
def naughty_page():
	return render_template('naughty.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask.ext.wtf import Form, TextAreaField
from Algcomposer import *
import os

class OutputForm(Form):
	output = TextAreaField('This is output')

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('main_page.html')

@app.route('/submit', methods=['POST', 'GET'])
def perform_script():

	#Initialize variables
	output = ""
	option = request.form["options"]
	root = request.form["root"]
	scale = request.form["scale"]
	song = """%s""" % request.form["guitar_tab"]

	#Initializes the scale chosen by the user
	jumps = get_scale_steps(scale)
	roots = get_root_note_positions(root)

	#Executes the method chosen by the user
	if option == 'ck':
		output = go_through_file(song, get_scale(roots, jumps), option)
	if option == 'ckr':
		output = go_through_file(song, get_scale(roots, jumps), 'ck', 5)

	with open("templates/main_page.html") as main_page:

		#Setting up variables for replacing
		scale_text = "<option value=" + '"' + scale + '"'
		root_text = "<option value=" + '"' + root + '"'
		method_text = "<option value=" + '"' + option + '"'
		input_text = "Enter text-based guitar tablature."
		
		#replace form elements in the original html file to preserve input
		replacement = main_page.read().replace("View output here", output)
		replacement = replacement.replace(input_text, song)
		replacement = replacement.replace(scale_text, scale_text + "selected")
		replacement = replacement.replace(root_text, root_text + "selected")
		replacement = replacement.replace(method_text, method_text + "selected")
		with open("templates/submitted.html", 'w') as output_file:
			#Write to submitted.html
			output_file.write(replacement)

	return render_template('submitted.html') 

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug=True)


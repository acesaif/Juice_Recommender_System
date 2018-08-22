import os
import dash
import time
import base64
import string
import random
from textblob import Word
from textblob import TextBlob
import dash_core_components as dcc
import dash_html_components as html
from wordprevention import stopwords
from dash.dependencies import Input, Output

def refined_cleaning(ipt):
	if type(ipt) == str:
		given_input = ipt.split(' ')
		clean = [word for word in given_input if word not in stopwords]
		senty = ' '.join(clean)
		endy = [word for word in senty if word not in string.punctuation]
		endy = ''.join(endy)
		endy = TextBlob(endy)
		correction = endy.correct()
		seperate = correction.split(' ')
		final = [each.singularize() for each in seperate]
		final = [Word(each) for each in final]
		final_check = [str(each.spellcheck()[0][0]) for each in final]
		final_check = ' '.join(final_check)
		return final_check
	else:
		return 'not a valid input'

# print(refined_cleaning('coldfk fevergk')) # cold fever

specific_input = 'cold'
pathy = os.getcwd()
everything = os.listdir(pathy)
all_dirs = []
for root, dirs, files in os.walk(pathy):
	if '.git' in dirs:
		dirs.remove('.git')
	all_dirs.append(dirs)
main_dirs = all_dirs[0]

matched_dirs = [dirs for dirs in main_dirs if specific_input in dirs]
dirs_content = []
for dirs in matched_dirs:
	os.chdir(dirs)
	dirs_content.append(os.listdir(os.getcwd()))
	os.chdir(pathy)
content = [j for i in dirs_content for j in i]

only_images = []
for file in content:
	image, ext = os.path.splitext(file)
	if ext == '.jpg' or ext == '.png':
		only_images.append(image + ext)

selected_images = [random.choice(only_images) for image in range(4)]

images_paths = []
for image in selected_images:
	for root, dirs, files in os.walk(pathy):
		for name in files:
			if name == image:
				images_paths.append(os.path.abspath(os.path.join(root, name)))

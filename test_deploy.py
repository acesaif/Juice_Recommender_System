import os
import dash
import time
import base64
import string
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

w = 'cold'
pathy = os.getcwd()
everything = os.listdir(pathy)
all_dirs = []
for root, dirs, files in os.walk(pathy):
	if '.git' in dirs:
		dirs.remove('.git')
	all_dirs.append(dirs)
main_dirs = all_dirs[0]
print(main_dirs)
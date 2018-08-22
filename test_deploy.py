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

def get_images(disease_input):
	disease_refined = refined_cleaning(disease_input)
	disease_refined = disease_refined.split(' ')
	specific_input = random.choice(disease_refined)
	# print(specific_input)
	pathy = os.getcwd()
	everything = os.listdir(pathy)
	all_dirs = []
	for root, dirs, files in os.walk(pathy):
		if '.git' in dirs:
			dirs.remove('.git')
		if 'some_data_screenshots' in dirs:
			dirs.remove('some_data_screenshots')
		all_dirs.append(dirs)
	main_dirs = all_dirs[0]

	matched_dirs = [dirs for dirs in main_dirs if specific_input in dirs]
	dirs_content = []
	for dirs in matched_dirs:
		os.chdir(str(dirs))
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

	return selected_images, images_paths

# print(get_images('cold'))

app = dash.Dash(__name__)

app.layout = html.Div([
	html.Div([
		dcc.Input(id='disease-input', type='text', 
			placeholder='Disease name: ', value='', size=40),
		html.Hr(),
	], style={'textAlign' : 'center', 'margin-top' : 25}),
	html.Div(id='recommeded-images'),
])

@app.callback(
	Output('recommeded-images', 'children'),
	[Input('disease-input', 'value')]
)
def basing_image(ipt):
	encoded_images = []

	try:
		if ipt == '':
			return html.Div([
				html.H4('Sorry, I cound not understand the Input.')
			], style={'textAlign' : 'center', 'margin-top' : 200})
		else:
			specific_images, specific_paths = get_images(str(ipt))
			image1 = specific_paths[0]
			en1 = base64.b64encode(open(image1, 'rb').read())
			image2 = specific_paths[1]
			en2 = base64.b64encode(open(image2, 'rb').read())
			image3 = specific_paths[2]
			en3 = base64.b64encode(open(image3, 'rb').read())
			image4 = specific_paths[3]
			en4 = base64.b64encode(open(image4, 'rb').read())

			encoded_images.append(
				html.Div([
					html.Div([
						html.Div([
							html.Img(src='data:image/png;base64,{}'.format(en1), id='display-image-1', 
								style={'width' : 250, 'height' : 200}),
							dcc.Markdown('''''' +str(os.path.splitext(specific_images[0])[0]) +'''''')
						], className='six columns', style={'textAlign' : 'right'}),
						html.Div([
							html.Img(src='data:image/png;base64,{}'.format(en2), id='display-image-2', 
								style={'width' : 250, 'height' : 200}),
							dcc.Markdown('''''' +str(os.path.splitext(specific_images[1])[0]) +'''''')
						], className='six columns', style={'textAlign' : 'left'}),
					], className='row', style={'margin-bottom' : 25}),
					html.Div([
						html.Div([
							html.Img(src='data:image/png;base64,{}'.format(en3), id='display-image-3', 
								style={'width' : 250, 'height' : 200}),
							dcc.Markdown('''''' +str(os.path.splitext(specific_images[2])[0]) +'''''')
						], className='six columns', style={'textAlign' : 'right'}),
						html.Div([
							html.Img(src='data:image/png;base64,{}'.format(en4), id='display-image-4', 
								style={'width' : 250, 'height' : 200}),
							dcc.Markdown('''''' +str(os.path.splitext(specific_images[3])[0]) +'''''')
						], className='six columns', style={'textAlign' : 'left'})
					], className='row')
				])
			)
			time.sleep(1.5)
			return encoded_images

	except Exception as e:
		return html.Div([
			html.H4('Some kind of nut got stuck into my AI system. Need some time to be alright')
		], style={'textAlign' : 'center', 'margin-top' : 200})

app.css.append_css({
	'external_url' : 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

app.scripts.append_script({
	'external_url' : 'https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js'
})

if __name__ == '__main__':
	app.run_server(debug=True)
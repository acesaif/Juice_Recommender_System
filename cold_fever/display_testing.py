import os
import dash
import time
import base64
import  random
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

pathy = os.getcwd()

pics = []
for file in os.listdir(pathy):
	image, ext = os.path.splitext(file)
	if ext == '.jpg' or ext == '.png':
		pics.append(image + ext)

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
		if ipt == 'cold' or ipt == 'fever':
			if len(pics) == 4:
				image1 = pics[0]
				en1 = base64.b64encode(open(image1, 'rb').read())
				image2 = pics[1]
				en2 = base64.b64encode(open(image2, 'rb').read())
				image3 = pics[2]
				en3 = base64.b64encode(open(image3, 'rb').read())
				image4 = pics[3]
				en4 = base64.b64encode(open(image4, 'rb').read())

				encoded_images.append(
					html.Div([
						html.Div([
							html.Div([
								html.Img(src='data:image/png;base64,{}'.format(en1), id='display-image-1', 
									style={'width' : 250, 'height' : 200}),
								dcc.Markdown('''Curry Green Leaf''')
							], className='six columns', style={'textAlign' : 'right'}),
							html.Div([
								html.Img(src='data:image/png;base64,{}'.format(en2), id='display-image-2', 
									style={'width' : 250, 'height' : 200}),
								dcc.Markdown('''Curry Green Leaf''')
							], className='six columns', style={'textAlign' : 'left'}),
						], className='row', style={'margin-bottom' : 25}),
						html.Div([
							html.Div([
								html.Img(src='data:image/png;base64,{}'.format(en3), id='display-image-3', 
									style={'width' : 250, 'height' : 200}),
								dcc.Markdown('''Pearfication''')
							], className='six columns', style={'textAlign' : 'right'}),
							html.Div([
								html.Img(src='data:image/png;base64,{}'.format(en4), id='display-image-4', 
									style={'width' : 250, 'height' : 200}),
								dcc.Markdown('''Pearfication''')
							], className='six columns', style={'textAlign' : 'left'})
						], className='row')
					])
				)
				return encoded_images
		else:
			return html.Div([
				html.H4('Sorry, I cound not understand the Input.')
			], style={'textAlign' : 'center', 'margin-top' : 200})

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
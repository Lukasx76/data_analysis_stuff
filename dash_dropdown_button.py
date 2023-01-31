from dash import Dash
from dash import dcc
from dash import html

app = Dash()

app.layout = html.div([
  html.H1('First Dash dropdown', style={'textAlign':'center'}),
  
  dcc.Dropdown(
    id='dash-dropdown'
    options=[
      {'label': 'São Paulo', 'value' : ''},
      {'label': 'San Francisco', 'value' : ''},
      {'label': 'Buenos Aires', 'value' : ''}

)])
if __name__ == '__main__':
  app.run()

from dash import Dash
from dash import dcc
from dash import html
from datetime import datetime

app = Dash()

app.layout = html.Div([

    html.H1('First dropdown and date settings', style={'textAlign': 'center'}),

    dcc.Dropdown(
    id='dropdown-with-dash',
    options=[
        {'label': 'São Paulo', 'value' : ''},
        {'label': 'San Francisco', 'value' : ''},
        {'label': 'Buenos Aires', 'value' : ''}]),

    dcc.DatePickerSingle(
        date = datetime(2023, 5, 10)),

    dcc.DatePickerRange(
        start_date=datetime(2023, 1, 31),
        end_date_placeholder_text='Type the end date here',
)])

if __name__ == '__main__':
    app.run(debug=True)

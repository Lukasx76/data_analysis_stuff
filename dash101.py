import dash
from dash import dcc
from dash import html


app = dash.Dash()

app.layout = html.Div([
    html.H1(children = 'Dash',
    style = {
        'textAlign' : 'center',
        'color' : '#AA4A44'
    }),
    html.Div(children = 'A new approach of displaying plots',
    style = {
        'textAlign': 'center',
        'color': '#AA4A44'
    }),
    dcc.Graph(
        figure={
            'data' : [{'x' : [1,2,3,4,5,6], 'y' : [2,4,6,8,10,12], 'type': 'bar', 'name': 'graph1'},
                      {'x' : [1,2,3,4,5,6], 'y' : [12,10,12,8,10,12], 'type': 'bar', 'name': 'graph2'}],
            'layout' : {'title' : 'graph2',
            'plot_bgcolor' : '#19B8BD',
            'paper_bgcolor' : '#19B8BD'}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

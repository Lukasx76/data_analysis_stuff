import dash
from dash import dcc
from dash import html


app = dash.Dash()

app.layout = html.Div([
    html.H1('hello world'),
    html.Div('a new kind of application'),
    dcc.Graph(
        figure={
            'data' : [{'x' : [1,2,3,4,5,6], 'y' : [2,4,6,8,10,12], 'type': 'bar', 'name': 'graph1'},
                      {'x' : [1,2,3,4,5,6], 'y' : [12,10,12,8,10,12], 'type': 'bar', 'name': 'graph2'}],
            'layout' : {'title' : 'graph2'}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

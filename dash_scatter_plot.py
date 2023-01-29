import plotly.graph_objs as go
import numpy as np
from dash import dcc
from dash import html
import dash

# FIRST, Define the x and y axis

x_axis = np.random.randint(1,61, 60)
y_axis = np.random.randint(1,61, 60)

# Second, Create an instance of Dash
app = dash.Dash()

# Third, define the 'shape' of the application
app.layout = html.Div([
    html.H1('Scatter plot', style={
        'textAlign' : 'center'
    }),
    dcc.Graph(
        figure = {
            'data' : [
                go.Scatter(x=x_axis, y=y_axis, mode = 'markers'),
            ]
        }
    )    
])

if __name__ == '__main__':
    app.run(debug=True)

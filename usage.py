import dash_draggable
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    html.Div(
        style={'width': '30vw', 'display': 'inline-flex'},
        children=dash_draggable.dash_draggable(
            id='draggable',
            axis="both",
            handle=".handle",
            defaultPosition={'x': 0, 'y': 100},
            position=None,
            grid=[12, 12],
            disabled=True,
            children=[
                html.Div(
                    id='a-div',
                    className='handle',
                    children=dcc.Graph(
                        id='example-graph',
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar',
                                 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                                 'name': u'Montréal'},
                            ],
                            'layout': {
                                'title': 'Drag anywhere'
                            }
                        }
                    )
                )
            ]
        )),

    html.Div(
        style={'width': '30vw', 'display': 'inline-flex'},
        children=dash_draggable.dash_draggable(
            id='draggable-2',
            axis='x',
            handle='.handle',
            defaultPosition={'x': 200, 'y': 100},
            position=None,
            grid=[25, 25],
            children=[
                html.Div(
                    id='another-div',
                    className='handle',
                    children=[
                        dcc.Graph(
                            id='example2',
                            figure=dict(
                                data=[go.Pie(
                                    labels=['Oxygen', 'Hydrogen',
                                            'Carbon_Dioxide',
                                            'Nitrogen'],
                                    values=[4500, 2500, 1053, 500],
                                )],
                                layout=dict(
                                    title='Drag horizontally'
                                )
                            )
                        )
                    ]
                )
            ]
        ))
])

if __name__ == '__main__':
    app.run_server(debug=True)

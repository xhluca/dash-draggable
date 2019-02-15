import dash_draggable
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_daq as daq


app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config['suppress_callback_exceptions']=True

app.layout = html.Div([
    daq.BooleanSwitch(id='toggle-drag', on=True),
    html.Div(id='status'),
    html.Div(
        style={'width': '30vw', 'display': 'inline-flex'},
        children=dash_draggable.dash_draggable(
            id='draggable',
            axis="both",
            handle=".handle",
            defaultPosition={'x': 0, 'y': 100},
            position=None,
            grid=[12, 12],
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


@app.callback(
    Output('draggable', 'disabled'),
    [Input('toggle-drag', 'on')]
)
def toggle_drag(toggle_status):
    # True/False
    return not toggle_status


@app.callback(
    Output('status', 'children'),
    [Input('toggle-drag', 'on')]
)
def can_drag(toggle_status):
    disabled = toggle_status # True/False
    print(disabled)
    return html.P("'Drag Anywhere' Component Draggable: {}".format(disabled))


if __name__ == '__main__':
    app.run_server(debug=True)

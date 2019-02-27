import dash
import dash_html_components as html
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_daq as daq
import dash_draggable as drag
from dash.exceptions import PreventUpdate
import sd_material_ui

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([

    dcc.Store(id='position-store', storage_type='session', data={'lastXs': [200], 'lastYs': [0]}),

    drag.dash_draggable(id='dragger',
                        handle='.handle',
                        defaultPosition={'x': 200, 'y': 0},
                        children=[
                            html.Div([
                                sd_material_ui.Paper(children=[
                                    sd_material_ui.IconButton(
                                        id='button',
                                        iconClassName='glyphicon glyphicon-menu-hamburger',
                                        iconStyle={'color': 'grey',
                                                   'width': 50,
                                                   'height': 50,
                                                   'position': 'relative',
                                                   'top': '2px',
                                                   'left': '-12px'},
                                        tooltip='Drag Me', touch=True,
                                        tooltipPosition='bottom-right')],
                                    zDepth=3,
                                    circle=True,
                                    style=dict(height=50,
                                               width=50,
                                               textAlign='center',
                                               position='relative',
                                               display='inline-block',
                                               top='25px',
                                               left='-25px')
                                )], className='handle'),

                            html.Div(id='graph-container')
                        ]),
])


############################################################################
# Commit last known position to memory
@app.callback(
    Output('position-store', 'data'),
    [Input('dragger', 'lastX'),
     Input('dragger', 'lastY')],
    [State('position-store', 'data')]
)
def remember_position(lastX, lastY, data):
    data = data or {}
    x_history = data['lastXs'] or []
    y_history = data['lastYs'] or []
    if lastX is not None:
        x_history.append(lastX)
    if lastY is not None:
        y_history.append(lastY)

    data = {'lastXs': x_history, 'lastYs': y_history}
    return data


############################################################################

@app.callback(
    Output('graph-container', 'children'),
    [Input('button', 'n_clicks'),
     Input('position-store', 'modified_timestamp')],
    [State('position-store', 'data'),
     State('graph-container', 'children')]
)
def hide_graph(clicks: int, timestamp, data, content):
    if timestamp is None:
        raise PreventUpdate

    xs = data.get('lastXs')
    ys = data.get('lastYs')

    if len(xs) > 1:
        x_prev = xs[-2]
        y_prev = ys[-2]
        x = xs[-1]
        y = ys[-1]
    else:
        x_prev = y_prev = x = y = None

    KNOB = sd_material_ui.Paper(zDepth=1,
                                style=dict(height=625,
                                           width=750),
                                children=[
                                    html.Div([
                                        daq.Knob(
                                            label="Gradient Ranges",
                                            value=7,
                                            size=500,
                                            color={"gradient": True,
                                                   "ranges": {"red": [0, 5], "yellow": [5, 9],
                                                              "green": [9, 10]}},
                                            style=dict(position='relative',
                                                       top='25px',
                                                       left='0px'))
                                    ])
                                ]),

    if x_prev == x or y_prev == y:
        if content is None or content == []:
            return KNOB
        elif content:
            return []


if __name__ == '__main__':
    app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'})
    app.run_server(debug=True)

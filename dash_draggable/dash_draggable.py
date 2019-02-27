# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class dash_draggable(Component):
    """A dash_draggable component.
...

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): ...
- id (string; optional): The ID used to identify this component in Dash callbacks
- axis (string; optional): ...
- handle (string; optional): ...
- defaultPosition (dict; optional): ...
- position (dict; optional): ...
- grid (list; optional): ...
- lastX (number; optional): ...
- lastY (number; optional): ...
- deltaX (number; optional): ...
- deltaY (number; optional): ...
- moved (boolean; optional): ...
- disabled (boolean; optional): ..."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, onStop=Component.UNDEFINED, axis=Component.UNDEFINED, handle=Component.UNDEFINED, defaultPosition=Component.UNDEFINED, position=Component.UNDEFINED, grid=Component.UNDEFINED, lastX=Component.UNDEFINED, lastY=Component.UNDEFINED, deltaX=Component.UNDEFINED, deltaY=Component.UNDEFINED, moved=Component.UNDEFINED, disabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'axis', 'handle', 'defaultPosition', 'position', 'grid', 'lastX', 'lastY', 'deltaX', 'deltaY', 'moved', 'disabled']
        self._type = 'dash_draggable'
        self._namespace = 'dash_draggable'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'axis', 'handle', 'defaultPosition', 'position', 'grid', 'lastX', 'lastY', 'deltaX', 'deltaY', 'moved', 'disabled']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(dash_draggable, self).__init__(children=children, **args)

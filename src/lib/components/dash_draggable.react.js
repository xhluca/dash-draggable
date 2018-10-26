import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Draggable from 'react-draggable';

/**
 * ...
 */
const dash_draggable = (props) => {
    return (
        <Draggable {...props}>
            <div>
                {props.children}
            </div>
        </Draggable>
    );
};

dash_draggable.defaultProps = {};

dash_draggable.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * ...
     */
    axis: PropTypes.string,

    /**
     * ...
     */
    handle: PropTypes.string,

    /**
     * ...
     */
    defaultPosition: PropTypes.object,

    /**
     * ...
     */
    position: PropTypes.object,

    /**
     * ...
     */
    grid: PropTypes.array,

    /**
     * ...
     */
    children: PropTypes.node
};

export default dash_draggable;
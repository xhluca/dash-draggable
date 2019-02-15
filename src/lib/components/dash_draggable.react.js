import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Draggable from 'react-draggable';

/**
 * ...
 */
class dash_draggable extends Component {
    constructor(props) {
        super(props);
        this.state = {};

        this.handleOnDragStop = this.handleOnDragStop.bind(this);
    }

    handleOnDragStop(event, data) {
        console.log(event);
        console.log(data);
        this.props.setProps({
            lastX: data.lastX,
            lastY: data.lastY,
            deltaX: data.deltaX,
            deltaY: data.deltaY,
        })
    }

    render() {
        return (
            <div id={this.props.id}>
                <Draggable onStop={this.handleOnDragStop}
                           axis={this.props.axis}
                           handle={this.props.handle}
                           defaultPosition={this.props.defaultPosition}
                           position={this.props.position}
                           grid={this.props.grid}
                           disabled={this.props.disabled}
                           >
                    <div>
                        {this.props.children}
                    </div>
                </Draggable>
            </div>
        );
    }
}

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
    onStop: PropTypes.func,

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
    lastX: PropTypes.number,

    /**
     * ...
     */
    lastY: PropTypes.number,

    /**
     * ...
     */
    deltaX: PropTypes.number,

    /**
     * ...
     */
    deltaY: PropTypes.number,

    /**
     * ...
     */
    children: PropTypes.node,

    /**
     * ...
     */
    disabled: PropTypes.bool
};

export default dash_draggable;

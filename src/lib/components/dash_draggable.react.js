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

        this.handleOnDrag = this.handleOnDrag.bind(this);
    }

    handleOnDrag(event, data) {
        console.log(event);
        console.log(data);
        this.props.setProps({testPosition: data});
    }

    render() {
        return (
            <Draggable onDrag={this.handleOnDrag}
                       {...this.props}>
                <div>
                    {this.props.children}
                </div>
            </Draggable>
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
    onDrag: PropTypes.func,

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
    getPosition: PropTypes.object,

    /**
     * ...
     */
    getEvent: PropTypes.object,

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
    children: PropTypes.node,

    /**
     * ...
     */
    disabled: PropTypes.bool
};

export default dash_draggable;

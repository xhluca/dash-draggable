/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';
import dash_draggable from '../lib';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        console.log("You will see this message if props are set correctly");
        console.log(newProps);
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <dash_draggable
                    setProps={this.setProps}
                    {...this.state}

                />
            </div>
        )
    }
}

export default App;

import React, { Component } from 'react';
import { observable, decorate, action } from 'mobx';
import { observer }  from 'mobx-react';


class Counter extends Component {

    count = observable.box(0);

    increment() {
        this.count.set(this.count.get() + 1);
    }

    reset() {
        this.count.set(0);
    }

    render() {
        return (
            <div>
                <p>{this.count.get()}</p>
                <button onClick={() => this.increment()}>Increment</button>
            </div>
        );
    }
}

decorate(Counter, {
    increment: action,
    reset: action
});


export default observer(Counter);
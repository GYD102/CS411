import React, { Component } from 'react';
import MvpPolitician from './components/MvpPolitician';
import './App.css';

// TODO: move the photo instantiation/assignment to inside the MvpPolitician class
import bernie from './photos/bernie.jpg';
import hillary from './photos/hillary.jpg';


class App extends Component {
    render() {
        return (
            <div className="App">
                <div className={"column"}>
                    <MvpPolitician photo={bernie} alt={'Bernie Sanders'} firstName={'Bernard'} lastName={'Sanders'}/>
                </div>

                <div className={"vertical-line"} />a

                <div className={"column"}>
                    <MvpPolitician photo={hillary} alt={'Hillary Clinton'} firstName={'Hillary'} lastName={'Clinton'}/>
                </div>
            </div>
        );
    }
}

export default App;
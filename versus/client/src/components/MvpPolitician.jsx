import React, { Component } from 'react';
import { observable, decorate, action } from 'mobx';
import { observer }  from 'mobx-react';
import Counter from './Counter';

class MvpPolitician extends Component {

    bio = {};
    root = "http://localhost:5000/";

    loadBio = (firstName, lastName) => {
        fetch(
            `${this.root}apis/govTrack/bio/${firstName}/${lastName}`
        )
            .then(response => response.json())
            .then(data => {
                this.bio = data;
            });
    };

    constructor(props) {
        super(props);
        this.props = props;
    }

    componentDidMount() {
        this.loadBio(this.props.firstName, this.props.lastName);
    }

    render() {
        return (
            <div className={"mvp-politician"}>
                <img className={"photo"} src={this.props.photo} alt={this.props.alt} width="250" height="250"/>
                <p>{this.props.firstName + " " + this.props.lastName}</p>
                <Counter/>
                <p>{this.bio['bio']}</p>
            </div>
        );
    }
}

decorate(MvpPolitician, {
    bio: observable,
    loadBio: action
});

export default observer(MvpPolitician);
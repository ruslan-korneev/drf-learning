import './App.css';
import AuthorList from './components/Author';
import React from 'react';
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    };
  };

  componentDidMount() {
    const authors = [
      {
        "first_name": "Ruslan",
        "last_name": "Korneev",
        "birthday_year": 2001,
      }
    ];
    this.setState({"authors": authors});
  };

  render() {
    return (
      <div className='authors'>
        <AuthorList authors={this.state.authors}/>
      </div>
    );
  }
};

export default App;

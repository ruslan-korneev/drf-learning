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
    axios.get("http://127.0.0.1:8000/api/authors/").then(response => {
      this.setState({"authors": response.data})
      console.log(response.data)
    }).catch(error => console.log(error))
  };

  render() {
    return (
      <div>
        <AuthorList authors={this.state.authors}/>
      </div>
    );
  }
};

export default App;

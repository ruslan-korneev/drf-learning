import './App.css';
import AuthorList from './components/Author';
import React, {Component} from 'react';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': [
        {
          'first_name': 'Фёдор',
          'last_name': 'Достоевский',
          'birthday_year': 1821,
        },
        {
            'first_name': 'Александр',
            'last_name': 'Грин',
            'birthday_year': 1880,
        }
      ]
    };
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

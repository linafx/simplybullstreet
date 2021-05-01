import React from "react";
import MockButton from "./MockButton";
import Investments from "./Investments";
import {
  Route,
  Link,
  BrowserRouter as Router,
  Redirect,
  Switch
} from "react-router-dom";

const App = () => {
  return (
    <div>
      <Router>
        <Route exact path="/" component={MockButton}></Route>
        <Route path="/investment" component={Investments}></Route>
      </Router>
    </div>
  );
};

export default App;

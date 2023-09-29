import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./Dashboard.js"
import DayView from "./DayView.js";
import Login from "./Login.js"
import Header from "./Header.js"
import Info from "./Info.js"
import Home from "./Home.js"


function App() {
  return(
  <div>
    <Header></Header>

        <Route exact path ="/">
        <Home></Home>
        </Route>
        <Route exact path ="/login">
        <Login></Login>
        </Route>
        <Route exact path ="/dashboard">
          <Dashboard></Dashboard>
        </Route>
        <Route exact path ="/info">
          <Info></Info>
        </Route>
        <Route exact path ="/dayview">
          <DayView></DayView>
        </Route>
  </div>
)}

export default App;

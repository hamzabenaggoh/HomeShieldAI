import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ChatboxPage from "./pages/ChatBoxPage.tsx";
import "./App.css"; // Your custom styles

const App = () => {
  return (
    <Router>
      <div className="App">
        <h1>Welcome to the Snort Configuration App</h1>
        {/* Define your routes here */}
        <Routes>
          {/* Route for the Chatbox Page */}
          <Route path="/chat" element={<ChatboxPage />} />
          
          {/* You can add more routes here for other parts of your app */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;

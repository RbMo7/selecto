import React from 'react';
import '../App.css'; // Import the separate CSS file

const NotFound = () => {
  return (
    <div className="center bg6 black">
      <h1 className="not-found-heading">Error 404</h1>
      <p className="not-found-text">Page not found</p>
      <p className="not-found-text">Sorry, the page you are looking for does not exist.</p>
    </div>
  );
};

export default NotFound;
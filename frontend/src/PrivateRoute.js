import React from "react";
import { Navigate } from "react-router-dom";

function Protected({ children }) {
  const isSignedIn = !!localStorage.getItem("access_token");
  if (!isSignedIn) {
    return <Navigate to="/" replace />;
  }
  return children;
}
export default Protected;

// import React from 'react';
// import { Route, Navigate } from 'react-router-dom';

// const PrivateRoute = ({ element: Element, ...rest }) => {
//   const isAuthenticated = !!localStorage.getItem('accessToken'); // Check if user is authenticated

//   return (
//     <Route
//       {...rest}
//       element={isAuthenticated ? <Element /> : <Navigate to="/login" />} // Redirect to the login page if not authenticated
//     />
//   );
// };

// export default PrivateRoute;

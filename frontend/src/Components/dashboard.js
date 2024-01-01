// Dashboard.js
import React from 'react';
import '../App.css';
import test from './Images/example.jpeg';
import product1Image from './Images/product1.jpeg';
import product2Image from './Images/product2.jpeg';

const user = {
    name: 'Saroj Poudel',
    email: 'sample@example.com',
    username: 'sp007',
    // Add other user details as needed
  };

  const trackedProducts = [
    { id: 1, name: 'Product 1', imageSrc: product1Image},
    { id: 2, name: 'Product 2', imageSrc: product2Image},
    // Add more tracked products with their image sources
  ];

function Dashboard() {
  return (
    <div className="container">
    <div className="dashboard-container">
      <div className="userDetails">
      <img src={test} alt="Product Image" style={{ maxWidth: '100%' }} />
      
        <div className="userInfo">
          <div className="dashboard-full-name">
            <h5> <b>Welcome!</b> {user.name}</h5>
          </div>
          <div className="user-name">
            <h5><b>Username:-</b>@{user.username}</h5>
          </div>
          <div className="user-email">
            <h5><b>Email:-</b>{user.email}</h5>
          </div>

        </div>
      </div>
      {/* Add your dashboard content below the user details */}
      <div className="dashboardContent">
        <h2 style={{fontSize: '1.5rem'}}>Dashboard Content</h2>
        <p>Write anything about users... </p>
      </div>
    </div>

    <div className="tracked-products">
        <h2>Tracked Products</h2>
        <ul>
          {/* Add your tracked products or components here */}
        {trackedProducts.map((product) => (
          <li key={product.id}>
            <img
              src={product.imageSrc}
              alt={product.name}
              style={{ maxWidth: '100%', height: 'auto' }}
            />
            <p>{product.name}</p>
          </li>
        ))}
        </ul> 
      </div>
      </div>
  );
}

export default Dashboard;

// Dashboard.js
import React from 'react';
import '../App.css';
import test from './Images/example.jpeg';
import product1Image from './Images/product1.jpeg';
import product2Image from './Images/product2.jpeg';
import product3Image from './Images/example.jpeg';


const user = {
    name: 'Saroj Poudel',
    email: 'sample@example.com',
    username: 'sp007',
    // Add other user details as needed
  };

  const trackedProducts = [
    { id: 1, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},
    { id: 2, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},

    // Add more tracked products with their image sources
  ];

function Dashboard() {
  return (
    <div className="container-dash">
    <div className="dashboard-container">
      <div className="userDetails">
      <img src={test} alt="Product Image" style={{ maxWidth: '100%' }} />
      
        <div className="userInfo">
          <div className="dashboard-full-name">
            <h5> <b>Welcome!</b> {user.name}</h5>
          </div>
          <div className="user-name">
            <h5>{user.username}</h5>
          </div>
          <div className="user-email">
            <h5>{user.email}</h5>
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
          <div className="product-container" key={product.id}>
          <div className="title-box">
            <h1>{product.name}</h1>
          </div>

          <div className="photo-and-price">
          <div className="photo-box" style={{ width: '250px' , textAlign: 'center' }}>
            <img src={product.imageSrc} alt="Product Image" style={{ maxWidth: '100%', height:'auto' }} />
          </div>

          <div className="price-box">
          {typeof product.price === 'string' ? (
          <h2>{product.price}</h2>) : (<h2>Price: ${product.price.toFixed(2)}</h2>
           )}
          </div>
        </div>

          <div className="description-box">
          <h3>Description</h3>
          <p> {product.description || 'No description available.'}</p>
          </div>

          <div className="review-box">
            <h3>Customer Reviews</h3>
            <p> {product.reviews || 'No Reviews yet.'}</p>
          </div>

        </div>
        ))}
        </ul> 
      </div>
    </div>
  );
}

export default Dashboard;
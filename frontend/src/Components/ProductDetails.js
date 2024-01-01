// src/components/ProductDetail.js
import React from 'react';
import image from './Images/example.jpeg';

const ProductDetail = () => {
  return (
    <div className="product-container">
      <div className="title-box">
        <h1>Product Title</h1>
      </div>

      <div className="photo-and-price">
        <div className="photo-box">
          <img src={image} alt="Product Image" style={{ maxWidth: '100%' }} />
        </div>

        <div className="price-box">
          <h2>Price: $99.99</h2>
        </div>
      </div>

      <div className="description-box">
        <p>
          This is a brief description of the product. It is a perfume with high quality and fregnance.
        </p>
      </div>

      <div className="review-box">
        <h3>Customer Reviews</h3>
        <p>No reviews yet.</p>
      </div>
    </div>
  );
};

export default ProductDetail;

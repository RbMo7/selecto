// src/pages/ProductPage.js
import React from 'react';
import ProductDetails from './ProductDetails';

const ProductPage = () => {
  const productData = {
    title: 'Example Product',
    price: 19.99,
    image: 'https://example.com/product-image.jpg',
    description: 'This is a sample project',
  };

  return (
    <div className="product-page">
      <ProductDetails {...productData} />
    </div>
  );
};

export default ProductPage;

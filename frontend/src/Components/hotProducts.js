import React from "react";
import product1Image from './Images/product1.jpeg';
import product2Image from './Images/product2.jpeg';

const trackedProducts = [
  { id: 1, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},
  { id: 2, name: 'Iphone 14 pro max', imageSrc: product2Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},
  { id: 1, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},
  { id: 1, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},

  // Add more tracked products with their image sources
];

const HotProduct = ({ product }) => (
  <div className="hot-product" key={product.id}>
    <div className="title-box">
      <h1>{product.name}</h1>
    </div>

    <div className="photo-and-price">
      <div className="photo-box" style={{ width: '250px', textAlign: 'center' }}>
        <img src={product.imageSrc} alt="Product Image" style={{ maxWidth: '100%', height:'auto' }} />
      </div>

      <div className="price-box">
        <p>{product.price}</p>
      </div>
    </div>

    <div className="description-box">
      <p>{product.description}</p>
    </div>

    <div className="reviews-box">
      <p>{product.reviews}</p>
    </div>
  </div>
);

const HotProductList = () => (
    <>
    <hr/>
    <h1 className="hotProducts-edit">Hot Products Searched Currently</h1>
    <hr/>
  <div className="hot-product-list">
    {trackedProducts.map((product) => (
      <HotProduct key={product.id} product={product} />
    ))}
  </div></>
);

export default HotProductList;
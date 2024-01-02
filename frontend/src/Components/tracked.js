import React, { Component } from "react";
import Slider from "react-slick";
import '../App.css';
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import product1Image from './Images/product1.jpeg';
import product2Image from './Images/product2.jpeg';


const trackedProducts = [
    { id: 1, name: 'Iphone 14 pro max', imageSrc: product1Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},
    { id: 2, name: 'Iphone 14 pro max', imageSrc: product2Image, price:'$99.99' ,description:'this is Iphone 14 pro max', reviews:'It is very good has quality camera'},

    // Add more tracked products with their image sources
  ];



export default class SimpleSlider extends Component {
  render() {
    const settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1
    };
    return (
        <div className="tracked-products">
        <h2>Tracked Products</h2>
        <Slider {...settings}>
        {trackedProducts.map((d) => (
            <div className="product-container" key={d.id}>
            <div className="title-box">
              <h1>{d.name}</h1>
            </div>
  
            <div className="photo-and-price">
            <div className="photo-box" style={{ width: '250px' , textAlign: 'center' }}>
              <img src={d.imageSrc} alt="Product Image" style={{ maxWidth: '100%', height:'auto' }} />
            </div>
  
            <div className="price-box">
              {typeof d.price === 'string' ? (
              <h2>{d.price}</h2>) : (<h2>Price: ${d.price.toFixed(2)}</h2>
           )}
            </div>
            </div>
  
          <div className="description-box">
            <h3>Description</h3>
            <p> {d.description || 'No description available.'}</p>
          </div>
  
          <div className="review-box">
            <h3>Customer Reviews</h3>
            <p> {d.reviews || 'No Reviews yet.'}</p>
          </div>
          
          </div>
          ))}
        </Slider>
      </div>
    );
  }
}
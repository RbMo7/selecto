// src/components/ProductDetail.js
import React, { useEffect, useState} from "react";
// import image from "./Images/example.jpeg";
import axios from "axios";
// import  { useEffect} from "react";
// import { useParams } from 'react-router-dom';

const ProductDetail = () => {

  const [Negative, setNegative] = useState("");
  const [Positive, setPositive] = useState("");
  const [Neutral, setNeutral] = useState("");
  const [Summary, setSummary] = useState("");

  // const { productName } = useParams();
  // console.log(productName)
  // const Product_Name= productName.product_name
  // const Product_Image= productName.product_img
  // console.log("Product Name:", Product_Name);
  // console.log("Product Image:", Product_Image);
  
  const productName = localStorage.getItem("productName")
  const productImg = localStorage.getItem("productImg")

  window.addEventListener('beforeunload', () => {
    localStorage.removeItem('productName');
    localStorage.removeItem('productImage');
  });

  useEffect(() => {
    // Define the API endpoint URL
    const apiUrl = "http://127.0.0.1:8000/selecto/api/nlp_view/";
  
    // Making a GET request to fetch data from the Django backend
    axios
      .get(`${apiUrl}${productName}/`)
      .then((response) => {
        const values= response.data.nlp

        console.log(values)
        // Access average sentiment values directly
        const avgNegative = values[0];
        const avgNeutral = values[1];
        const avgPositive = values[2];
        const Summary = values[3];

        setNegative(avgNeutral)
        setPositive(avgNegative)
        setNeutral(avgPositive)
        setSummary(Summary)
  
        console.log('Average Negative:', avgNeutral);
        console.log('Average Neutral:', avgPositive);
        console.log('Average Positive:', avgNegative);
        console.log('Summary:', Summary);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [productName]);
  

  return (
    <div className="product-container">
      <div className="title-box">
        <h1>{productName}</h1>
      </div>

      <div className="photo-and-price">
        <div className="photo-box">
          <img src={productImg} alt="" style={{ maxWidth: "100%" }} />
        </div>

        {/* <div className="price-box">
          <h2>Price: $99.99</h2>
        </div> */}
      </div>

      <div className="description-box">
        <p>
          Summary:
        </p>
        <p>
        {Summary}
        </p>
      </div>

      <div className="review-box">
        <h3>Customer Reviews :</h3>
        <p>Negative : {Negative}</p>
        <p>Positive : {Positive}</p>
        <p>Neutral : {Neutral}</p>
      </div>
    </div>
  );

  
};


export default ProductDetail;

// src/components/ProductDetail.js
import React from 'react';
import image from './Images/example.jpeg';

const ProductDetail = ({ product }) => {
  const { product_name, product_img } = product;



  // useEffect(() => {
  //   // Define the API endpoint URL
  //   const apiUrl = "http://127.0.0.1:8000/selecto/api/get_products/";

  //   // Makaing a GET request to fetch data from the Django backend
  //   axios
  //     .get(`${apiUrl}${productName}/`)
  //     .then((response) => {
  //       // Filter out objects with null values
  //       const filteredProducts = response.data.products.filter(
  //         (product) =>
  //           product.product_name !== null && product.product_img !== null
  //       );
  //       // Update the state with the fetched products
  //       console.log(filteredProducts);
  //       setProducts(filteredProducts);
  //     })
  //     .catch((error) => {
  //       console.error("Error fetching data:", error);
  //     });
  // }, [productName]);



  return (
    <div className="product-container">
      <div className="title-box">
        <h1>{product_name}</h1>
      </div>

      <div className="photo-and-price">
        <div className="photo-box">
          <img src={product_img} alt="" style={{ maxWidth: '100%' }} />
        </div>

        {/* <div className="price-box">
          <h2>Price: $99.99</h2>
        </div> */}
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

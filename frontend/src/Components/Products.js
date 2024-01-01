import React, { useEffect, useState } from "react";
import { Modal } from "react-bootstrap";
import ProductCard from "./Card";
import axios from "axios";

function ProductListModal({ productData, show, onHide }) {
  const [products, setProducts] = useState([]);
  const searchText = productData.length > 0 ? productData[0].searchText : "";
  const productName = productData.length > 0 ? productData[0].productName : "";

  // Using useEffect to fetch data when the component mounts
  useEffect(() => {
    // Define the API endpoint URL
    const apiUrl = "http://127.0.0.1:8000/selecto/api/get_products/";

    // Makaing a GET request to fetch data from the Django backend
    axios
      .get(`${apiUrl}${productName}/`)
      .then((response) => {
        // Filter out objects with null values
        const filteredProducts = response.data.products.filter(
          (product) =>
            product.product_name !== null && product.product_img !== null
        );
        // Update the state with the fetched products
        console.log(filteredProducts);
        setProducts(filteredProducts);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [productName]);

//   // Function to process NLP request
// const processNLPRequest = (productName) => {
//   // Define the NLP API endpoint URL
//   const nlpApiUrl = "http://127.0.0.1:8000/selecto/api/nlp_view/";

//   // Make a GET request for NLP processing
//   return axios.get(`${nlpApiUrl}${productName}`)
//     .then((nlpResponse) => {
//       // Handle the response from the NLP processing endpoint
//       console.log("NLP Processing Response:", nlpResponse.data);

//       // You can return the relevant data or perform other actions as needed
//       return nlpResponse.data;
//     })
//     .catch((error) => {
//       console.error("Error processing NLP request:", error);
//       throw error; // Re-throw the error to be caught by the caller if needed
//     });
// };

// // Example usage in your useEffect
// useEffect(() => {
//   // Define the API endpoint URL
//   const apiUrl = "http://127.0.0.1:8000/selecto/api/get_products/";

//   // Make a GET request to fetch data from the Django backend
//   axios.get(`${apiUrl}${productName}`)
//     .then((response) => {
//       // Filter out objects with null values
//       const filteredProducts = response.data.products.filter(
//         (product) =>
//           product.product_name !== null && product.product_img !== null
//       );
//       // Update the state with the fetched products
//       console.log(filteredProducts);
//       setProducts(filteredProducts);

//       // Call the function to process NLP request
//       return processNLPRequest(productName);
//     })
//     .then((nlpData) => {
//       // Handle the NLP data as needed
//       console.log("Processed NLP Data:", nlpData);

//       // You can update the state or perform any other actions based on the NLP response
//     })
//     .catch((error) => {
//       console.error("Error fetching data:", error);
//     });
// }, [productName]);

  

  return (
    <Modal show={show} onHide={onHide} size="lg">
      <Modal.Header closeButton>
        <Modal.Title>Product List for "{searchText}"</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div>
          {products.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </Modal.Body>
      <Modal.Footer>{/* Footer of modal if needed */}</Modal.Footer>
    </Modal>
  );
}

export default ProductListModal;

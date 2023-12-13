import React, { useEffect, useState } from "react";
import { Modal } from "react-bootstrap";
import ProductCard from "./Card";
import axios from "axios";

function ProductListModal({ productData, show, onHide }) {
  const [products, setProducts] = useState([]);
  const searchText = productData.length > 0 ? productData[0].searchText : "";
  const collectionName = searchText; 

  // Using useEffect to fetch data when the component mounts
  useEffect(() => {
    // Define the API endpoint URL
    const apiUrl = "http://127.0.0.1:8000/products/api/get_products/";

    // Makaing a GET request to fetch data from the Django backend
    axios
      .get(`${apiUrl}${collectionName}/`)
      .then((response) => {
        // Update the state with the fetched products
        setProducts(response.data.products);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [collectionName]); 

  return (
    <Modal show={show} onHide={onHide} size="lg">
      <Modal.Header closeButton>
        <Modal.Title>Product List for "{searchText}"</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div>
          {products.map((product, index) => (
            <ProductCard key={index} product={product} />
          ))}
        </div>
      </Modal.Body>
      <Modal.Footer>
        {/* Footer of modal if needed */}
      </Modal.Footer>
    </Modal>
  );
}

export default ProductListModal;

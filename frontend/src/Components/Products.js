import React, { useEffect, useState } from "react";
import { Modal } from "react-bootstrap";
import ProductCard from "./Card";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
// import ProductDetail from "./ProductDetails";

function ProductListModal({ productData, show, onHide }) {
  const [products, setProducts] = useState([]);
  const searchText = productData.length > 0 ? productData[0].searchText : "";
  const productName = productData.length > 0 ? productData[0].productName : "";
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate("/productdetails"); // Use history.push to navigate
  };

  const handleNoClick=() => {
    onHide();
    toast("Try searching for your desired product again");
  };

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
        const productNames = filteredProducts.map(
          (product) => product.product_name
        );
        const productImg = filteredProducts.map(
          (product) => product.product_img
        );
        console.log(productNames);
        localStorage.setItem("productName", productNames);
        localStorage.setItem("productImg", productImg);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [productName]);

  return (
    <Modal show={show} onHide={onHide} size="lg">
      <Modal.Header closeButton>
        <Modal.Title>Product List for "{searchText}"</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div>
          {products.map((product) => (
            <ProductCard key={product.id} product={product} />

            // <React.Fragment key={product.id}>
            //   {/* Render ProductCard for each product */}
            //   <ProductCard product={product} />

            //   {/* Render ProductDetails for each product */}
            //   <ProductDetails product={product} />
            // </React.Fragment>
          ))}
        </div>
      </Modal.Body>
      <Modal.Footer>
        <p>Is This The Product You are looking for?</p>
        <button
          type="button"
          onClick={handleButtonClick}
          class="btn btn-dark mx-3"
        >
          Yes
        </button>

        <button type="button" onClick={handleNoClick} class="btn btn-dark">
          No
        </button>
      </Modal.Footer>
    </Modal>
  );
}

export default ProductListModal;

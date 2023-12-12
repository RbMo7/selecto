import React from "react";
import { Modal} from "react-bootstrap";
import ProductCard from "./Card"; // Update the import path based on your project structure

function ProductListModal({ products, show, onHide }) {
  const searchText = products.length > 0 ? products[0].searchText : "";
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
        {/* footer of modal if needed */}
      </Modal.Footer>
    </Modal>
  );
}

export default ProductListModal;

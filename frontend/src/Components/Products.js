import React from "react";
import ProductCard from "./Card"; // Update the import path based on your project structure

function ProductList({ products }) {
  return (
    <div>
      {products.map((product, index) => (
        <ProductCard key={index} product={product} />
      ))}
    </div>
  );
}

export default ProductList;

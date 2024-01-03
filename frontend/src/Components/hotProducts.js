import React from "react";



const HotProduct = ({ product }) => (
  <div className="hot-product" key={product.collection}>
    <div className="title-box-hot">
      <h5 style={{ whiteSpace: 'nowrap' }}>{product.collection}</h5>
    </div>
    <div className="hot-product-full">
    <h7>{product.collection}</h7>
    </div>
    <div className="photo-and-price">
      <div className="photo-box" style={{ width: '250px', textAlign: 'center' }}>
        <img src={product.product_img} alt="Product Image" style={{ maxWidth: '100%', height:'auto' }} />
      </div>
    
      <div className="count">
      
        <h6>Total Searches: {product.count}</h6>
      </div>
    </div>
  </div>
);

const HotProductList = ({topCollections}) => (
    <>
    <hr/>
    <h1 className="hotProducts-edit">Hot Products Searched Currently</h1>
    <hr/>
  <div className="hot-product-list">
    {topCollections.map((product) => (
      <HotProduct key={product.collection} product={product} />
    ))}
  </div></>
);

export default HotProductList;
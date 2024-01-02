import React, { useState } from "react";
import { Form, Button, Row, Col, Container } from "react-bootstrap";
import logo from "./Images/Logo-NObg-NOtxt.png";
import axios from "axios";
import { toast } from "react-hot-toast";
import ProductListModal from "./Products";
import Loading from "./Loading"; // Import the Loading component

function Search(props) {
  const [searchText, setSearchText] = useState("");
  const [productName, setProductName] = useState("");
  const [loading, setLoading] = useState(false);
  const [showProductListModal, setShowProductListModal] = useState(false);
  const productData = [{ searchText, productName }];

  const handleShowProductListModal = () => {
    setShowProductListModal(true);
  };

  const handleHideProductListModal = () => {
    setShowProductListModal(false);
  };

  const handleSearch = async (e) => {
    e.preventDefault();

    // Input validation
    if (!searchText.trim()) {
      console.error("Search text is empty");
      toast.error("Search text is empty");
      setShowProductListModal(false);
      return;
    }

    try {
      setLoading(true);
      const { data } = await axios.post(
        "http://localhost:8000/selecto/api/search_and_scrape/",
        { searchText }
      );

      console.log(data.title);
      setProductName(data.title);
    } catch (error) {
      console.error("Error sending search request:", error);
      toast.error("An error occurred while fetching products");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="text-center my-5">
      <h1 className="display-4">
        <img src={logo} alt="Logo" width="300" height="100" className="mb-4" />
      </h1>

      <Form inline onSubmit={handleSearch} className="mb-4">
        <Form.Control
          type="text"
          placeholder="Search for products..."
          className="mr-sm-2"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
        />
        <br />
        <Button
          variant="primary"
          type="Submit"
          onClick={handleShowProductListModal}
          className="btn-transition"
        >
          Search
        </Button>
      </Form>

    
      {loading ? (
        <Loading />
      ) : productName ? (
        <div>
          <ProductListModal
            productData={productData}
            show={showProductListModal}
            onHide={handleHideProductListModal}
          />
        </div>
      ) : null}
    </Container>
  );
}

export default Search;

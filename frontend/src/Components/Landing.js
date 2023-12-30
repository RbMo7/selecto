import React, { useState } from "react";
import { Form,Button, Row, Col, Container } from "react-bootstrap";
import logo from "./Images/Logo-NObg-NOtxt.png";
import axios from "axios";
import { toast } from "react-hot-toast";
import ProductListModal from "./Products";
function Landing(props) {
  const [searchText, setSearchText] = useState("");

  const [showProductListModal, setShowProductListModal] = useState(false);
  const productData = [{searchText}];

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
      // Show an error message or prevent the request
      console.error("Search text is empty");
      toast.error("Search text is empty");
      setShowProductListModal(false);
      return;
    }

    try {
      const response = await axios.post(
        "http://localhost:8000/selecto/api/search_and_scrape/",
        { searchText }
      );
      console.log(response.data);
    } catch (error) {
      console.error("Error sending search request:", error);
      toast.error("An error occurred while fetching products");
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

      <Row className="gx-3">
        <Col md={6} className="mb-5">
        <div className="p-4 rounded border border-primary">
          <h2 className="text-primary">Discover the Best Products</h2>
          <p className="lead">
            Find the products you love with personalized recommendations
            tailored just for you.
          </p>
          </div>
        </Col>
        <Col md={6} className="mb-5">
        <div className="p-4 rounded border border-primary">
          <h2 className="text-primary">Easy and Quick</h2>
          <p className="lead">
            Effortlessly explore and search for products to enhance your
            shopping experience.
          </p>
          </div>
        </Col>
      </Row>
      <ProductListModal
        productData={productData}
        show={showProductListModal}
        onHide={handleHideProductListModal}
      />
    </Container>
  );
}

export default Landing;

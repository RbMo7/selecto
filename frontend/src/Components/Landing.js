import React, { useState } from "react";
import { Form, Button, Row, Col, Container } from "react-bootstrap";
import logo from "./Images/Logo-NObg-NOtxt.png";
import axios from "axios";

function Landing(props) {
  const [searchText, setSearchText] = useState("");

  const handleSearch = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/products/api/search_and_scrape/", {
        searchText,
      });
      console.log(response.data);
    } catch (error) {
      console.error("Error sending search request:", error);
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
        <Button variant="dark" type="submit" className="ml-2">
          Search
        </Button>
      </Form>

      <Row>
        <Col md={6} className="mb-4">
          <h2 className="text-primary">Discover the Best Products</h2>
          <p className="lead">
            Find the products you love with personalized recommendations
            tailored just for you.
          </p>
        </Col>
        <Col md={6} className="mb-4">
          <h2 className="text-primary">Easy and Quick</h2>
          <p className="lead">
            Effortlessly explore and search for products to enhance your
            shopping experience.
          </p>
        </Col>
      </Row>
    </Container>
  );
}

export default Landing;

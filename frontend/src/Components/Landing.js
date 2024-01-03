import React from "react";
import { Row, Col, Container } from "react-bootstrap";
import Search from "./search";

function Landing(props) {
  return (
    <Container className="text-center my-5">
      <Search />
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
    </Container>
  );
}

export default Landing;

import React from "react";
import { Container, Row, Col } from "react-bootstrap";

export default function About(props) {
  return (
    <Container className="py-5">
      <Row>
        <Col className="text-center">
          <h1 className="display-4" style={{ fontWeight: "bold" }}>Discover the World of Selecto</h1>
          <p className="lead">
            Welcome to Selecto! Your personalized gateway to a world of curated product recommendations.
          </p>
        </Col>
      </Row>

      <Row className="my-5">
        <Col md={4}>
          <div className="about-item text-center">
            <h2>Our Mission</h2>
            <hr />
            <p>
              At Selecto, we aim to simplify your product selection journey by providing personalized and an honest reviews on the products you want to buy.
            </p>
          </div>
        </Col>

        <Col md={4}>
          <div className="about-item text-center">
            <h2>Features</h2>
            <hr />
            <p>
              Explore a range of features designed to enhance your product discovery experience. Get a trustworthy review, and decide on whether you want to buy the product or not.
            </p>
          </div>
        </Col>

        <Col md={4}>
          <div className="about-item text-center">
            <h2>Future Plans</h2>
            <hr />
            <p>
              Exciting plans ahead! We're integrating with renowned tracking services and building a community of people who are scared that they will get scammed online. Stay tuned for updates!
            </p>
          </div>
        </Col>
      </Row>

      <hr />

      <Row className="my-5">
        <Col className="text-center">
          <h1 className="display-4">
            <i>*Enjoy Exploring Products with Selecto*</i>
          </h1>
          <p className="lead">Ready to get started? Register now and embark on a journey of personalized product reviews!</p>
          <button className="btn btn-primary">Sign Up</button>
        </Col>
      </Row>
    </Container>
  );
}

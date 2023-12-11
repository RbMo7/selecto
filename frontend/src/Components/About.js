import React from "react";
import { Container, Row, Col } from "react-bootstrap";

export default function About(props) {
  return (
    <Container className="py-5">
      <Row>
        <Col className="text-center">
          <h1 className="display-4">ABOUT SELECTO</h1>
          <p className="lead">
            Welcome to Selecto! Your go-to platform for personalized product
            recommendations. Whether you're a seasoned shopper or exploring new
            products, our mission is to simplify the selection process and offer
            tailored suggestions based on your preferences.
          </p>
        </Col>
      </Row>

      <Row className="my-5">
        <Col md={4}>
          <div className="about-item text-center">
            <h2>OUR MISSION</h2>
            <hr />
            <p>
              At Selecto, we strive to make the product selection journey
              seamless. Understanding that each shopper is unique, we utilize
              data analysis and algorithms to comprehend your preferences,
              providing personalized recommendations. Our goal is to guide users
              in discovering new products effortlessly.
            </p>
          </div>
        </Col>

        <Col md={4}>
          <div className="about-item text-center">
            <h2>FEATURES</h2>
            <hr />
            <p>
              Selecto offers a range of features to enhance your product
              discovery experience. Users can search for products based on their
              interests, and registered users can save and rate their favorite
              items, creating personalized collections. With features like
              "Recommended Products," we aim to present a diverse selection to
              cater to every shopper's preferences.
            </p>
          </div>
        </Col>

        <Col md={4}>
          <div className="about-item text-center">
            <h2>FUTURE PLANS</h2>
            <hr />
            <p>
              Exciting plans lie ahead for Selecto. We plan to integrate with
              renowned e-commerce services, enabling users to seamlessly explore
              and purchase products directly through our platform. Additionally,
              we aspire to build a community of enthusiastic shoppers sharing
              their product experiences, tips, and recommendations. Stay tuned
              for more updates!
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
        </Col>
      </Row>
    </Container>
  );
}

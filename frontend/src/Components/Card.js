import React from "react";
import { Button, Card, Col, Container, Row } from "react-bootstrap";

function ProductCard({ product }) {
  const { product_name, product_img } = product;

  return (
    <Container>
      <Card className="my-3">
        <Row className="g-0">
          <Col md={4}>
            <Card.Img src={product_img} alt={product_name} />
          </Col>
          <Col md={8}>
            <Card.Body>
              <Card.Title>{product_name}</Card.Title>
              <Card.Text>description</Card.Text>
              <Button variant="primary">Learn More</Button>
            </Card.Body>
          </Col>
        </Row>
      </Card>
    </Container>
  );
}

export default ProductCard;


import React, { useEffect, useState } from "react";
import axios from "axios";
import { Container, Row, Col, Spinner } from "react-bootstrap";

import "bootstrap/dist/css/bootstrap.min.css";

const ProductDetail = () => {
  const [loading, setLoading] = useState(true);
  const [negative, setNegative] = useState("");
  const [positive, setPositive] = useState("");
  const [neutral, setNeutral] = useState("");
  const [summary, setSummary] = useState("");

  const productName = localStorage.getItem("productName");
  const productImg = localStorage.getItem("productImg");

  window.addEventListener("beforeunload", () => {
    localStorage.removeItem("productName");
    localStorage.removeItem("productImage");
  });

  useEffect(() => {
    const apiUrl = "http://127.0.0.1:8000/selecto/api/nlp_view/";

    axios
      .get(`${apiUrl}${productName}/`)
      .then((response) => {
        const values = response.data.nlp;

        const avgNegative = values[0];
        const avgNeutral = values[1];
        const avgPositive = values[2];
        const summary = values[3];

        setNegative(avgNegative);
        setPositive(avgPositive);
        setNeutral(avgNeutral);
        setSummary(summary);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [productName]);

  return (
    <Container className="mt-4">
      <Row>
        <Col md={8}>
          <div className="card">
            <div className="card-body">
              <h1>{productName}</h1>
              <div className="photo-box">
                <img src={productImg} alt="" className="img-fluid" />
              </div>
            </div>
          </div>
        </Col>
        <Col md={4}>
          <div className="card">
            <div className="card-body">
              <h3>Customer Reviews :</h3>
              {loading ? (
                <Spinner animation="border" role="status">
                  <span className="sr-only">Loading...</span>
                </Spinner>
              ) : (
                <>
                  <p>Negative : {negative}</p>
                  <p>Positive : {positive}</p>
                  <p>Neutral : {neutral}</p>
                </>
              )}
            </div>
          </div>
        </Col>
      </Row>
      <Row>
        <Col md={12} className="mt-3">
          <div className="card">
            <div className="card-body">
              <h3>Summary:</h3>
              {loading ? (
                <Spinner animation="border" role="status">
                  <span className="sr-only">Loading...</span>
                </Spinner>
              ) : (
                <p>{summary}</p>
              )}
            </div>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default ProductDetail;

// SignInModal.js
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Modal, Button, Form, Image } from "react-bootstrap";
import selectoLogo from "./Images/Logo-NObg.png";
import RegisterModal from "./RegisterModal";
import toast from "react-hot-toast";
import axios from "axios";
import "./styles.css";

function SignInModal(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showRegisterModal, setShowRegisterModal] = useState(false);
  const navigate = useNavigate();

  const handleSignIn = async (e) => {
    e.preventDefault();

    const userData = { email, password };
    // Input validation
    if (!email || !password) {
      // Show an error message or prevent the request
      console.error("Empty Fields");
      toast.error("Don't leave empty fields");
      return;
    }

    try {
      const { data } = await axios.post(
        "http://localhost:8000/selecto/api/signin/",
        { userData }
      );

      if (!data.error) {
        toast.success("SignIn successfully");
        //redirecting user to userdashboard
      } else {
        toast.error(data.error);
      }
    } catch (error) {
      console.error("Error sending search request:", error);
      toast.error("An error occurred ", error);
    }
  };

  const handleRegisterModalShow = () => {
    setShowRegisterModal(true);
  };

  const handleRegisterModalHide = () => {
    setShowRegisterModal(false);
  };

  return (
    <Modal
      {...props}
      size="md"
      aria-labelledby="contained-modal-title-vcenter"
      centered
      className="glassMorphism" // Apply the glass morphism class
    >
      <Modal.Header closeButton>
        <Modal.Title className="text-center w-100">Sign In</Modal.Title>
      </Modal.Header>
      <Modal.Body className="text-center">
        <Image
          src={selectoLogo}
          alt="Selecto Logo"
          width="200"
          height="200"
          className="mb-3"
        />
        <Form onSubmit={handleSignIn}>
          <Form.Group controlId="formBasicEmail">
            <Form.Control
              onChange={(e) => setEmail(e.target.value)}
              value={email}
              type="email"
              placeholder="Enter your email"
            />
          </Form.Group>

          <br />

          <Form.Group controlId="formBasicPassword">
            <Form.Control
              onChange={(e) => setPassword(e.target.value)}
              value={password}
              type="password"
              placeholder="Enter your password"
            />

          </Form.Group>
          <br />
          <Button variant="primary" type="submit" block>
            Sign In
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer text-center>
        Don't have an account?{" "}
        <Button variant="link" onClick={handleRegisterModalShow}>
          Sign Up
        </Button>
      </Modal.Footer>
      <RegisterModal
        show={showRegisterModal}
        onHide={() => {
          handleRegisterModalHide();
          props.onHide(); // Close SignInModal when RegisterModal is closed
        }}
      />
    </Modal>
  );
}

export default SignInModal;

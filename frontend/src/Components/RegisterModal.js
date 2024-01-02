// RegisterModal.js
import React, { useState } from "react";
import { Modal, Button, Form, Image, Col } from "react-bootstrap";
// import selectoLogo from "./Images/logotext.png";
import selectoLogo from "./Images/Logo-NObg.png";
import SignInModal from "./SignInModal";
import toast from "react-hot-toast";
import axios from "axios";

function RegisterModal(props) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showSignInModal, setShowSignInModal] = React.useState(false);

  const handleSignInModalShow = () => {
    setShowSignInModal(true);
  };

  const handleSignInModalHide = () => {
    setShowSignInModal(false);
  };

  const handleRegister = async (e) => {
    e.preventDefault();

    const userData = { name, email, password };
    // Input validation
    if (!email || !password || !name) {
      // Show an error message or prevent the request
      console.error("Empty Fields");
      toast.error("Don't leave empty fields");
      return;
    }

    try {
      const { data } = await axios.post(
        "http://localhost:8000/selecto/api/register/",
        { userData }
      );

      if (!data.error) {
        toast.success("Registered successfully. Proceed to Login");
        setShowSignInModal(true);
      } else {
        toast.error(data.error);
      }
    } catch (error) {
      console.error("Error sending search request:", error);
      toast.error("An error occurred ", error);
    }
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
        <Modal.Title className="text-center w-100">Register</Modal.Title>
      </Modal.Header>
      <Modal.Body className="text-center">
        <Image
          src={selectoLogo}
          alt="Selecto Logo"
          width="200"
          height="200"
          className="mb-3"
        />
        <Form onSubmit={handleRegister}>
          <Form.Group as={Col} controlId="formGridName">
            <Form.Control
              onChange={(e) => setName(e.target.value)}
              value={name}
              type="text"
              placeholder="Enter your name"
            />
          </Form.Group>
          <br />
          <Form.Group as={Col} controlId="formGridEmail">
            <Form.Control
              onChange={(e) => setEmail(e.target.value)}
              value={email}
              type="email"
              placeholder="Enter your email"
            />
          </Form.Group>
          <br />

          <Form.Group className="mb-3" controlId="formGridPassword">
            <Form.Control
              onChange={(e) => setPassword(e.target.value)}
              value={password}
              type="password"
              placeholder="Create a password"
            />
          </Form.Group>

          <Button variant="primary" type="submit" block>
            Register
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <p className="text-muted">
          Already have an account?{" "}
          <Button variant="link" onClick={handleSignInModalShow}>
            Sign In
          </Button>
        </p>
      </Modal.Footer>
      <SignInModal
        show={showSignInModal}
        onHide={() => {
          handleSignInModalHide();
          props.onHide(); // Close RegisterModal when SignInModal is closed
        }}
      />
    </Modal>
  );
}

export default RegisterModal;

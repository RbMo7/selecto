// SignInModal.js
import React, { useState } from "react";
import { Modal, Button, Form, Image } from "react-bootstrap";
import selectoLogo from "./Images/Logo-NObg.png";
import RegisterModal from "./RegisterModal";

function SignInModal(props) {
  const [showRegisterModal, setShowRegisterModal] = useState(false);

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
        <Form>
          <Form.Group controlId="formBasicEmail">
            <Form.Control type="email" placeholder="Enter your email" />
          </Form.Group>

          <br />

          <Form.Group controlId="formBasicPassword">
            <Form.Control type="password" placeholder="Enter your password" />
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

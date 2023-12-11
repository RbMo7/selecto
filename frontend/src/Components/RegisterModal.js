// RegisterModal.js
import React from "react";
import { Modal, Button, Form, Image, Row, Col } from "react-bootstrap";
import selectoLogo from "./Images/Logo-NObg.png";
import SignInModal from "./SignInModal";

function RegisterModal(props) {
  const [showSignInModal, setShowSignInModal] = React.useState(false);

  const handleSignInModalShow = () => {
    setShowSignInModal(true);
  };

  const handleSignInModalHide = () => {
    setShowSignInModal(false);
  };

  return (
    <Modal
      {...props}
      size="md"
      aria-labelledby="contained-modal-title-vcenter"
      centered
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
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridName">
              <Form.Control type="text" placeholder="Enter your name" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Control type="email" placeholder="Enter your email" />
            </Form.Group>
          </Row>

          <Form.Group className="mb-3" controlId="formGridPassword">
            <Form.Control type="password" placeholder="Create a password" />
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

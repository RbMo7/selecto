import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import logo from "./Images/Logo-NObg.png";
import SignInModal from "./SignInModal";
import RegisterModal from "./RegisterModal";

function BasicNavbar() {
  const [showModal, setShowModal] = useState(null);

  const handleModalShow = (modal) => {
    setShowModal(modal);
  };

  const handleModalHide = () => {
    setShowModal(null);
  };

  const isAuthenticated = localStorage.getItem("access_token");
  const userid = isAuthenticated;

  return (
    <>
      <>
        {isAuthenticated ? (
          <>
            {/* Content for authenticated user */}
            <Navbar expand="lg" className="bg-body-tertiary">
              <Container>
                <Navbar.Brand
                  href={`/dashboard/${userid}`}
                  className="d-flex align-items-center"
                >
                  <img src={logo} alt="Logo" width="85" height="85" />
                  <span className="ms-4">
                    <Nav.Link
                      href={`/dashboard/${userid}`}
                      className="me-2 navbar-link"
                    >
                      Home
                    </Nav.Link>
                  </span>
                  <span className="ms-2">
                    <Nav.Link href="/about" className="ms-2 navbar-link">
                      About
                    </Nav.Link>
                  </span>
                </Navbar.Brand>

                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                  <Nav className="ms-auto">
                    <Nav.Link
                      href="/"
                      onClick={() => {
                        localStorage.removeItem("access_token");
                      }}
                      className="ms-2 navbar-link"
                    >
                      Logout
                    </Nav.Link>
                  </Nav>
                </Navbar.Collapse>
              </Container>
            </Navbar>
          </>
        ) : (
          <>
            {/* Content for unauthenticated user */}
            <Navbar expand="lg" className="bg-body-tertiary">
              <Container>
                <Navbar.Brand href="/" className="d-flex align-items-center">
                  <img src={logo} alt="Logo" width="85" height="85" />
                  <span className="ms-4">
                    <Nav.Link href="/" className="me-2 navbar-link">
                      Home
                    </Nav.Link>
                  </span>
                  <span className="ms-2">
                    <Nav.Link href="/about" className="ms-2 navbar-link">
                      About
                    </Nav.Link>
                  </span>
                </Navbar.Brand>

                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                  <Nav className="ms-auto">
                    <Nav.Link
                      href="#"
                      onClick={() => handleModalShow("signIn")}
                      aria-label="Sign In"
                      className="me-2 navbar-link sign-in-link"
                    >
                      Sign In
                    </Nav.Link>
                    <Nav.Link
                      href="#"
                      onClick={() => handleModalShow("register")}
                      aria-label="Register"
                      className="ms-2 navbar-link register-link"
                    >
                      Register
                    </Nav.Link>
                  </Nav>
                </Navbar.Collapse>
              </Container>
            </Navbar>
          </>
        )}
      </>

      {showModal === "signIn" && (
        <SignInModal show={true} onHide={handleModalHide} />
      )}

      {showModal === "register" && (
        <RegisterModal show={true} onHide={handleModalHide} />
      )}
    </>
  );
}

export default BasicNavbar;

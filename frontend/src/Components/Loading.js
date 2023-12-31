// Loading.js
import React from 'react';
import { Modal } from 'react-bootstrap';


const Loading = () => {
  return (
    <Modal show={true} centered backdrop="static" keyboard={false}>
      <Modal.Body className="loading-container text-center">
        <div className="custom-loader"></div>
      </Modal.Body>
    </Modal>
  );
};

export default Loading;

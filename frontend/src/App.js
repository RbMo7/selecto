// import logo from './logo.svg';
import "./App.css";
import Navbar from "./Components/Navbar";
import Landing from "./Components/Landing";
import About from "./Components/About";
import NotFound from "./Components/NotFound";
import ProductDetails from "./Components/ProductDetails";

import { Toaster } from "react-hot-toast";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

export default function App() {
  return (
    <>
      <div>
        <Toaster position="bottom-right" toastOptions={{ duration: 5000 }} />
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Landing />} />

            <Route path="/About" element={<About />} />
            <Route path="/productdetails" element={<ProductDetails />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Router>
      </div>
    </>
  );
}

// import logo from './logo.svg';
import "./App.css";
import Navbar from "./Components/Navbar";
import Landing from "./Components/Landing";
import About from "./Components/About";
import NotFound from "./Components/NotFound";
import ProductDetails from "./Components/ProductDetails";
import Dashboard from "./Components/dashboard";
import SimpleSlider from "./Components/tracked";
import { Toaster } from "react-hot-toast";
import Protected from "./PrivateRoute";
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Search from "./Components/search";
import Settings from "./Components/settings";

export default function App() {
  const [modal, setmodal] = useState(false);
  const isAuthenticated = !!localStorage.getItem("accessToken");
  return (
    <>
      <div>
        <Toaster position="bottom-right" toastOptions={{ duration: 5000 }} />
        <Router>
          <Navbar isAuthenticated={isAuthenticated} setmodal={setmodal} />
          <Routes>
            <Route
              path="/"
              element={<Landing modal={modal} setmodal={setmodal} />}
            />

            <Route
              path="/About"
              element={<About modal={modal} setmodal={setmodal} />}
            />
            <Route
              path="/productdetails"
              element={<ProductDetails modal={modal} setmodal={setmodal} />}
            />
            <Route path="/tracked" element={<SimpleSlider />} />

            <Route path="/search" element={<Search />} />


            <Route
              path="/dashboard/:id"
              element={
                <Protected>
                  <Dashboard modal={modal} setmodal={setmodal} />
                </Protected>
              }
            />

            <Route
              path="/dashboard/:id/settings"
              element={
                <Protected>
                  <Settings modal={modal} setmodal={setmodal} />
                </Protected>
              }
            />

            <Route path="*" element={<NotFound />} />
          </Routes>
        </Router>
      </div>
    </>
  );
}

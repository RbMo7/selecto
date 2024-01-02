import React, { useState, useEffect } from "react";
import axios from "axios";
import { toast } from "react-hot-toast";
import "../App.css";
import img from "./Images/defaultuser.png";
import Upload from "./Images/Upload-icon.png";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function Settings() {
  const id = localStorage.getItem("access_token");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [imgSrc, setImgSrc] = useState("img");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/selecto/api/userdetails/${id}/`
        );
        console.log("API Response:", response.data);
        setName(response.data.user["name"]); // Update state with username
        setEmail(response.data.user["email"]);
        // setImgSrc(response.data.user["profile_image"]);
        // console.log(imgSrc);
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchUserData();
  }, [id]);

  const handleSubmit = async (e) => {
    console.log("yeta aayo");
    e.preventDefault();

    try {
      const updatedUserDetails = {
        id,
        name,
        email
      };

      // Send the updated user details to the backend API
      const { data } = await axios.patch(
        `http://127.0.0.1:8000/selecto/api/update_userdetails/${id}/`,
        { updatedUserDetails }
      );

      if (data.error) {
        toast.error(data.error);
      } else {
        toast.success("Information Updated Successfully");
        navigate(`/dashboard/${id}`);
      }
    } catch (error) {
      // Display error message received from the backend
      const errorMessage = error.response.data.message;
      toast.error(errorMessage);
    }
  };

  const handleImageUpload = (event) => {
    const file = event.target.files[0]; // Get the selected file
    if (file) {
      // Create a FileReader object
      const reader = new FileReader();

      reader.onload = () => {
        // Update the image source with the selected file
        setImgSrc(reader.result);
      };

      reader.readAsDataURL(file); // Read the file as data URL
    }
  };

  return (
    <>
      <div className="container gap ">
        <div className="row">
          <div className="col-md-3 ">
            <h1 className="quicksand20">Settings</h1>
            <hr />

            <ul className=" navbar-nav me-auto mb-2 mb-lg-0 quicksand17  ">
              <li className="nav-item">
                <NavLink
                  className="nav-link "
                  style={{ font: "Montserrat", fontSize: 30 }}
                  to={`/Dashboard/${id}/settings`}
                >
                  My Profile
                </NavLink>
              </li>

              <li className="nav-item">
                <NavLink
                  className="nav-link "
                  style={{ font: "Montserrat", fontSize: 30 }}
                  to={`/pw/${id}`}
                >
                  Edit Password
                </NavLink>
              </li>

              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  // onClick={() => props.setmodal(true)}
                  style={{ font: "Montserrat", fontSize: 30 }}
                  to={`/Dashboard/settings/${id}`}
                >
                  Delete Account
                </NavLink>
              </li>
            </ul>
          </div>

          <div className="col-md-6 ">
            <div className="circle ">
              <img
                src={imgSrc}
                alt="Logo"
                className="logo-image "
                height="200px"
                width="200px"
              />
            </div>
            {/*<div className="upload-logo">*/}
            <label htmlFor="upload-input" className="upload-button shift">
              <span className="upload-button-text">
                <img
                  src={Upload}
                  alt="Update Logo"
                  className="upload-icon"
                  height="60px"
                  width="60px"
                />
              </span>
              <input
                id="upload-input"
                type="file"
                accept="image/*"
                onChange={handleImageUpload}
                style={{ display: "none" }}
              />
            </label>

            <br />
            <form className="quicksand15" onSubmit={handleSubmit}>
              {/* <form className="quicksand15"> */}
              <strong>
                <label htmlFor="Name" className="form-label">
                  FullName
                </label>
                <input
                  onChange={(e) => setName(e.target.value)}
                  type="text"
                  className=" form-control"
                  id="Name"
                  value={name}
                />
                <br />
                <label htmlFor="email" className="form-label">
                  E-mail
                </label>
                <input
                  value={email}
                  required
                  onChange={(e) => setEmail(e.target.value)}
                  type="text"
                  id="email"
                  className=" form-control"
                />

                <br />
                <button
                  type="submit"
                  onClick={handleSubmit}
                  className="btn btn-success btn-lg"
                  // onClick={() => props.setmodal1(true)}
                >
                  Save
                </button>

                <br />
              </strong>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default Settings;

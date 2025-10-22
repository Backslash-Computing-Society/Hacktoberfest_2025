import React, { useState } from "react";
import "./Navbar.css";
function Navbar() {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <nav className="navbar">
            <div className="nav-logo">React Navbar</div>
            <div className="{`nav-links ${isOpen ?'open':''}`}">
            <ul className="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#Contribution">Contribution</a></li>
                <li><a href="#Contact">Contact</a></li>
            </ul>
            </div>
            <div className="nav-toggle" onClick={() => setIsOpen(!isOpen)}>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </nav>
    );
}

export default Navbar;
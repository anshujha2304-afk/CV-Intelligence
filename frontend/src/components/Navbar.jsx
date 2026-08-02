import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md shadow-sm">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-5">
        {/* Logo */}
        <Link
          to="/"
          className="text-3xl font-extrabold text-blue-600 hover:text-blue-700 transition"
        >
          CV-Intelligence
        </Link>

        {/* Navigation */}
        <div className="hidden md:flex items-center gap-8 text-gray-700 font-medium">
          <a href="#features" className="hover:text-blue-600 transition">
            Features
          </a>

          <a href="#about" className="hover:text-blue-600 transition">
            About
          </a>

          <Link to="/login" className="hover:text-blue-600 transition">
            Login
          </Link>

          <Link
            to="/signup"
            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700 transition"
          >
            Sign Up
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
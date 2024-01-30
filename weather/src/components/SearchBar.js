import "bootstrap/dist/css/bootstrap.css";
import { useState } from "react";
function SearchBar({ onSubmit }) {
  const [input, setInput] = useState("");
  const handleFormSubmit = (event) => {
    event.preventDefault();
    onSubmit(input);
  };
  const handleChange = (event) => {
    setInput(event.target.value);
  };
  return (
    <div className="container mt-5">
      <div className="form-outline">
        <form onSubmit={handleFormSubmit}>
          <input
            value={input}
            onChange={handleChange}
            className="form-control"
            placeholder="Name of City"
          />
        </form>
      </div>
    </div>
  );
}
export default SearchBar;

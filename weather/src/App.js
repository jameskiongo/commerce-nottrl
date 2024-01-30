import "bootstrap/dist/css/bootstrap.css";
import SearchBar from "./components/SearchBar";
import searchWeather from "./api";
import WeatherInfo from "./components/WeatherInfo";
import { useState } from "react";
function App() {
  const [weather, setWeather] = useState("");
  const handleSubmit = async (input) => {
    const result = await searchWeather(input);
    setWeather(result);
  };

  return (
    <div>
      <SearchBar onSubmit={handleSubmit} />
      <WeatherInfo weather={weather} />
    </div>
  );
}
export default App;

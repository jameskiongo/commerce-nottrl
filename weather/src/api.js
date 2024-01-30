import axios from "axios";

const apiKey = process.env.REACT_APP_API_KEY;
const searchWeather = async (input) => {
  try {
    const response = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${input}&appid=${apiKey}`,
    );
    return response.data;
  } catch (error) {
    if (error.response && error.response.status === 404) {
      console.error("No such City (404 error)");
      // Handle the 404 error as needed
    } else {
      console.error("Error fetching data:", error);
    }
  }
};
export default searchWeather;

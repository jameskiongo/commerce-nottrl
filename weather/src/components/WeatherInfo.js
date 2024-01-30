import "bootstrap/dist/css/bootstrap.css";
import "./WeatherInfo.css";
function WeatherInfo({ weather }) {
  if (!weather) {
    return <div></div>;
  } else {
    const temp = Math.floor(weather.main.temp - 273.15);
    const description = weather.weather?.[0]?.description;
    const icon = weather.weather?.[0]?.icon;
    return (
      <div className="container mt-5">
        <div className="d-flex flex-row justify-content-center align-items-center">
          <div className="weather__card">
            <div className="d-flex flex-row justify-content-center align-items-center">
              <div className="p-3">
                <h2>{temp}°C</h2>
              </div>
              <div className="p-3">
                <img
                  alt={description}
                  src={`https://openweathermap.org/img/wn/${icon}.png`}
                />
              </div>
              <div className="p-3">
                <h5>{new Date().toDateString()}</h5>
                <h3>{weather.name}</h3>
                <span className="weather__description">{description}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default WeatherInfo;

import { useState, useEffect } from "react";
import { Bar, Line } from "react-chartjs-2";
import "chart.js/auto";

const API = "http://127.0.0.1:8000/api";

export default function App() {
  const [summary, setSummary] = useState(null);
  const [file, setFile] = useState(null);

  useEffect(() => {
    fetch(`${API}/summary/`)
      .then(res => res.json())
      .then(setSummary)
      .catch(() => alert("Backend not running"));
  }, []);

  const upload = () => {
    const form = new FormData();
    form.append("file", file);
    fetch(`${API}/upload/`, { method: "POST", body: form })
      .then(r => r.json())
      .then(d => setSummary(d.summary));
  };

  return (
    <div style={{ fontFamily: "Arial", padding: 20 }}>
      <h1>⚗️ Chemical Equipment Visualizer</h1>

      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload}>Upload CSV</button>

      {summary && (
        <>
          <h3>Summary</h3>
          <p>Total: {summary.total}</p>
          <p>Avg Flowrate: {summary.avg_flowrate.toFixed(2)}</p>
          <p>Avg Pressure: {summary.avg_pressure.toFixed(2)}</p>
          <p>Avg Temperature: {summary.avg_temperature.toFixed(2)}</p>

          <Bar
            data={{
              labels: Object.keys(summary.type_distribution),
              datasets: [{
                label: "Equipment Count",
                data: Object.values(summary.type_distribution),
                backgroundColor: "rgba(0,123,255,0.6)"
              }]
            }}
          />

          <Line
            data={{
              labels: ["Flowrate", "Pressure", "Temperature"],
              datasets: [{
                label: "Averages",
                data: [
                  summary.avg_flowrate,
                  summary.avg_pressure,
                  summary.avg_temperature
                ],
                borderColor: "red"
              }]
            }}
          />
        </>
      )}
    </div>
  );
}

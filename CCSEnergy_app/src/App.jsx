import { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://ccsenergy-api.onrender.com/items')
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <table border="1" cellPadding="8">
      <thead>
        <tr>
          {data[0] && Object.keys(data[0]).map(key => <th key={key}>{key}</th>)}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>
            {Object.values(row).map((val, j) => (
              <td key={j}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default App;
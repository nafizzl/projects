import { useEffect, useState } from "react";
import axios from "axios"

function App() {
  
  const [message, setMessage] = useState("");
  
  useEffect(() => {
    axios
    .get('/')
    .then(res => {
      console.log(res.data.message);
      setMessage(res.data.message);
    })
    .catch(error => {
      console.error("Error fetching...", error);
    });
  }, [])

  return (
    <div>
      <p>{message}</p>
    </div>
  );
}

export default App;

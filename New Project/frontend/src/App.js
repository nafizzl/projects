import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [jsonData, setJsonData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/data/');
                setJsonData(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="App">
            <h1>React Frontend</h1>
            {jsonData && (
                <div>
                    <p>Message from Django: {jsonData.message}</p>
                    <p>Status: {jsonData.status}</p>
                </div>
            )}
        </div>
    );
}

export default App;

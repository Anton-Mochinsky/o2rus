import React, { useState } from 'react';
import axios from 'axios';
import ResultTable from './ResultTable';

const SearchPart = () => {
    const [article, setArticle] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');

    const searchPart = async () => {
        try {
            const token = localStorage.getItem('token');
            const response = await axios.post(
                'http://localhost:8000/api/search/',
                { article },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            setResults(response.data); // Результаты поиска
            setError('');
        } catch (err) {
            setError('Failed to fetch results. Please try again.');
        }
    };

    return (
        <div>
            <h2>Search for Spare Parts</h2>
            <input
                type="text"
                placeholder="Enter article"
                value={article}
                onChange={(e) => setArticle(e.target.value)}
            />
            <button onClick={searchPart}>Search</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ResultTable results={results} />
        </div>
    );
};

export default SearchPart;

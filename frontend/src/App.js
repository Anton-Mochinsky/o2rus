// import React, { useState } from 'react';
// import axios from 'axios';

// const SearchPart = () => {
//     const [article, setArticle] = useState('');
//     const [results, setResults] = useState([]);

//     const searchPart = async () => {
//         const response = await axios.post('http://localhost:8000/api/search/', { article }, {
//             headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
//         });
//         setResults(response.data);
//     };

//     return (
//         <div>
//             <input value={article} onChange={(e) => setArticle(e.target.value)} placeholder="Enter article" />
//             <button onClick={searchPart}>Search</button>
//             <ul>
//                 {results.map((result, idx) => (
//                     <li key={idx}>
//                         <a href={result.link}>{result.article} - {result.quantity} - {result.price}</a>
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// };

// export default SearchPart;
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import SearchPart from './components/SearchPart';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/search" element={<SearchPart />} />
            </Routes>
        </Router>
    );
};

export default App;

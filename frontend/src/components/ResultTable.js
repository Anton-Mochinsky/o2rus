import React from 'react';

const ResultTable = ({ results }) => {
    if (results.length === 0) {
        return <p>No results found</p>;
    }

    return (
        <table border="1" style={{ width: '100%', marginTop: '20px' }}>
            <thead>
                <tr>
                    <th>Article</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody>
                {results.map((result, index) => (
                    <tr key={index}>
                        <td>{result.article}</td>
                        <td>{result.quantity}</td>
                        <td>{result.price}</td>
                        <td>
                            <a href={result.link} target="_blank" rel="noopener noreferrer">
                                View
                            </a>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default ResultTable;

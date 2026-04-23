# Calvin and Hobbes Quoter API

![](calandhobbes.gif)

## Introduction

The Calvin and Hobbes Quoter API is a simple Flask-based RESTful API that provides random quotes from the iconic comic strip Calvin and Hobbes by Bill Watterson. It's a lighthearted way to integrate Calvin and Hobbes's wisdom into your applications or projects.

## Features

- Retrieve random Calvin and Hobbes quotes.
- Built with Flask for simplicity.
- Cross-Origin Resource Sharing (CORS) enabled for easy integration.

## Usage

To use the Calvin and Hobbes Quoter API, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/bhavv04/calandhobbes-quoter
   cd calandhobbes-quoter
   ```
2. Install dependencies:

   ```
   pip install -r requiremnts.txt
   ```
3. Run the API:

   ```
   python api.py
   ```
4. Head to the server to view the JSON file:

   ```
   http://127.0.0.1:8080/api/quotes/random
   ```

## Implementation

This example demonstrates how to fetch random data from an API in various programming languages.

### JavaScript/React

```javascript
import { useState, useEffect } from 'react';

const useRandomData = (apiEndpoint) => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiEndpoint);
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, [apiEndpoint]);

  return data;
};

// Example usage:
const QuoteComponent = () => {
  const quote = useRandomData('http://127.0.0.1:8080/api/quotes/random');

  // Your component logic with the fetched data...
};
```

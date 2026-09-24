# Calvin and Hobbes Quoter API

A lightweight Flask API that serves random quotes from *Calvin and Hobbes* by Bill Watterson.

**Live API:** https://calandhobbes-quoter.vercel.app

## Features

- Random Calvin and Hobbes quotes as JSON
- Built with Flask, with no database or setup required
- CORS enabled, so you can call it directly from the browser
- Deployed on Vercel

## Quick start

Try it without installing anything:

```bash
curl https://calandhobbes-quoter.vercel.app/api/quotes/random
```

## API reference

### `GET /api/quotes/random`

Returns one random quote.

**Example response**

```json
{
  "quote": "It's not a dilemma, it's a trade-off.",
  "author": "Calvin"
}
```

| Field    | Type   | Description                  |
| -------- | ------ | ---------------------------- |
| `quote`  | string | The quote text               |
| `author` | string | The character who said it    |

## Usage

### JavaScript

```javascript
const res = await fetch('https://calandhobbes-quoter.vercel.app/api/quotes/random');
const data = await res.json();
console.log(data.quote, '-', data.author);
```

### React

```javascript
import { useState, useEffect } from 'react';

const useRandomData = (apiEndpoint) => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiEndpoint);
        setData(await response.json());
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, [apiEndpoint]);

  return data;
};

const QuoteComponent = () => {
  const quote = useRandomData('https://calandhobbes-quoter.vercel.app/api/quotes/random');

  return (
    <blockquote>
      <p>{quote.quote}</p>
      <footer>- {quote.author}</footer>
    </blockquote>
  );
};
```

### Python

```python
import requests

data = requests.get("https://calandhobbes-quoter.vercel.app/api/quotes/random").json()
print(f'{data["quote"]} - {data["author"]}')
```

## Run locally

1. Clone the repository:

```bash
   git clone https://github.com/bhavv04/calandhobbes-quoter
   cd calandhobbes-quoter
```

2. (Optional) Create a virtual environment:

```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

4. Start the server:

```bash
   python app.py
```

5. Open http://127.0.0.1:8080/api/quotes/random

## Project structure

```
calandhobbes-quoter/
├── api/                # API code
├── public/             # Front-end (index.html, styles.css, main.js)
├── app.py              # Local entry point
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config
└── Procfile            # Process definition
```

## Contributing

Issues and pull requests are welcome.

## License

Released under the [MIT License](LICENSE).
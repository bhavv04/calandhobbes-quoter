const BASE = 'https://calandhobbes-quoter-production.up.railway.app';
const IMAGES = ['image.png', 'image1.png', 'image2.png', 'image3.png'];

async function fetchQuote() {
  const quote = document.getElementById('quote');
  const author = document.getElementById('author');
  const btn = document.getElementById('btn');
  const img = document.querySelector('img');

  btn.disabled = true;
  quote.classList.add('loading');

  const random = IMAGES[Math.floor(Math.random() * IMAGES.length)];
  img.src = `/assets/${random}`;

  try {
    const res = await fetch(BASE + '/api/quotes/random');
    const d = await res.json();
    quote.textContent = d.quoteText;
    author.textContent = '— ' + d.quoteAuthor;
  } catch {
    quote.textContent = 'Could not load quote.';
    author.textContent = '';
  } finally {
    quote.classList.remove('loading');
    btn.disabled = false;
  }
}

fetchQuote();
const BASE = '';
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

function toggleDocs() {
  const docs = document.getElementById('docs');
  const btn = document.getElementById('docs-btn');
  const open = docs.hidden;
  docs.hidden = !open;
  btn.setAttribute('aria-expanded', String(open));
  btn.textContent = open ? 'Hide docs' : 'How to implement';
}

fetchQuote();

// Tabs
document.querySelector('.tabs')?.addEventListener('click', (e) => {
  const tab = e.target.closest('.tab');
  if (!tab) return;

  document.querySelectorAll('.tab').forEach((t) => {
    const active = t === tab;
    t.classList.toggle('active', active);
    t.setAttribute('aria-selected', String(active));
  });
  document.querySelectorAll('.tab-panel').forEach((p) => {
    p.classList.toggle('active', p.id === `tab-${tab.dataset.tab}`);
  });
});

// Copy buttons
document.getElementById('docs')?.addEventListener('click', async (e) => {
  const btn = e.target.closest('.copy');
  if (!btn) return;

  const target = btn.dataset.copyTarget
    ? document.getElementById(btn.dataset.copyTarget)
    : btn.closest('.code-block').querySelector('code');

  try {
    await navigator.clipboard.writeText(target.textContent);
    btn.textContent = 'Copied!';
  } catch {
    btn.textContent = 'Failed';
  }
  setTimeout(() => (btn.textContent = 'Copy'), 1500);
});
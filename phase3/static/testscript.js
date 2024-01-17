
const API_URL = 'https://itunes.apple.com/search?media=music&limit=10';

const searchBtn = document.getElementById("search-btn");
const searchInput = document.querySelector('#search-term');
const maxDurationInput = document.querySelector('#duration-filter');
const explicitFilterSelect = document.querySelector('#explicit-filter');
const searchResults = document.querySelector('#search-results');
const filterBtn = document.querySelector('#filter-btn');
const resetBtn = document.querySelector('#reset-btn');

let searchTerm = '';
let maxDuration = '';
let isExplicit = '';

searchBtn.addEventListener('click', (event) => {
  event.preventDefault();
  searchTerm = searchInput.value;
  search();
});

filterBtn.addEventListener('click', (event) => {
  event.preventDefault();
  applyFilters();
});

resetBtn.addEventListener('click', (event) => {
  event.preventDefault();
  resetFilters();
});

function search() {
  const url = `${API_URL}&term=${searchTerm}`;
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      displayResults(data.results);
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

function applyFilters() {
  maxDuration = maxDurationInput.value;
  isExplicit = explicitFilterSelect.value;
  search();
}

function resetFilters() {
  maxDurationInput.value = '';
  explicitFilterSelect.value = 'all';
  maxDuration = '';
  isExplicit = '';
  search();
}

function displayResults(results) {
  searchResults.innerHTML = '';

  if (results.length === 0) {
    searchResults.innerHTML = '<p>No results found.</p>';
    return;
  }

  let filteredResults = results;

  // Filter by max duration
  if (maxDuration) {
    filteredResults = filteredResults.filter(result => {
      const durationInSeconds = result.trackTimeMillis / 1000;
      const durationInMinutes = durationInSeconds / 60;
      return durationInMinutes <= maxDuration;
    });
  }

  // Filter by explicitness
  if (isExplicit === 'explicit') {
    filteredResults = filteredResults.filter(result => result.trackExplicitness === 'explicit');
  } else if (isExplicit === 'not-explicit') {
    filteredResults = filteredResults.filter(result => result.trackExplicitness !== 'explicit');
  }

  const resultsHTML = filteredResults.map(result => {
    const trackName = result.trackName;
    const artistName = result.artistName;
    const artworkUrl = result.artworkUrl100;
    const albumName = result.collectionName;
    const releaseDate = result.releaseDate;
    const previewUrl = result.previewUrl;

    return `
      <div>
        <img src="${artworkUrl}" alt="${albumName}">
        <p>${trackName} - ${artistName}</p>
        <p>${albumName} (${releaseDate.substring(0, 4)})</p>
        <audio controls>
          <source src="${previewUrl}" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>
      </div>
      <br>
      <br>
      <br>
    `;
  }).join('');

  searchResults.innerHTML = resultsHTML;
}

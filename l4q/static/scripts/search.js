const urlParams = new URLSearchParams(window.location.search);
const searchForm = document.getElementById("search_form");
const searchButton = document.getElementById("search_button");
const searchInput = document.getElementById("search_input");

searchInput.addEventListener("input", field => {
    const value = field.target.value.trim();
    searchInput.classList.toggle("search_input_active", value.length);
});

searchForm.addEventListener("submit", event => {
    event.preventDefault();
});

document.addEventListener("DOMContentLoaded", () => searchInput.value = urlParams.get("search"));

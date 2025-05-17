const searchForm = document.getElementById("search_form");
const searchButton = document.getElementById("search_button");
const searchInput = document.getElementById("search_input");

const serverInfoFetchHint = document.querySelector(".server_info_hint");
const serverInfoContainer = document.querySelector(".server_info_container");

const validHostnamePattern = /[^\:]+:([0-9]+)/;

function validateHostnamePattern(value) {
    return Boolean(validHostnamePattern.test(value) &&
            parseInt(value.match(validHostnamePattern)[1]) <= 65535 &&
            parseInt(value.match(validHostnamePattern)[1]) > 0);
}

searchInput.addEventListener("input", field => {
    const value = field.target.value.trim();
    searchButton.disabled = !validateHostnamePattern(value);
});

searchForm.addEventListener("submit", event => {
    event.preventDefault();
    searchInput.value = searchInput.value.trim();
    serverInfoContainer.classList.add("hide");
    serverInfoFetchHint.classList.remove("hide");
    serverInfoFetchHint.innerHTML = "Fetching server details...";
    const targetUrl = new URL(location.protocol + '//' + location.host + location.pathname);
    targetUrl.searchParams.set("search", searchInput.value);
    fetch(targetUrl.toString(), {
        method: "GET",
        headers: {
            "x-fetch-subview": "1"
        }
    })
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        return Promise.reject(response)
    })
    .then(response => {
        serverInfoFetchHint.classList.add("hide");
        serverInfoContainer.classList.remove("hide");
        serverInfoContainer.innerHTML = response;
        window.history.pushState({}, "", targetUrl.toString());
        document.title = `${document.querySelector(".server_name").innerHTML} - Info`
    })
    .catch(response => {
        response.text().then(text => serverInfoFetchHint.innerHTML = text);
        window.history.pushState({}, "", targetUrl.toString());
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("search")) {
        searchInput.value = urlParams.get("search").trim();
    }
    searchButton.disabled = !validateHostnamePattern(searchInput.value);
});

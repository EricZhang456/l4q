const searchForm = document.getElementById("search_form");
const searchButton = document.getElementById("search_button");
const searchInput = document.getElementById("search_input");

const serverInfoFetchHint = document.querySelector(".server_info_hint");
const serverInfoContainer = document.querySelector(".server_info_container");

const validHostnamePattern = /[^:]+:([0-9]{1,5})$/;

function validateHostnamePattern(value) {
    return Boolean(validHostnamePattern.test(value) &&
            parseInt(value.match(validHostnamePattern)[1]) <= 65535 &&
            parseInt(value.match(validHostnamePattern)[1]) > 0);
}

searchInput.addEventListener("input", (field) => 
    searchButton.disabled = !validateHostnamePattern(field.target.value.trim())
);

async function fetchServerInfo(pushStateToHistory = true) {
    searchButton.disabled = true;
    searchInput.value = searchInput.value.trim();
    serverInfoContainer.classList.add("hide");
    serverInfoFetchHint.classList.remove("hide");
    serverInfoFetchHint.innerHTML = "Fetching server details...";
    serverInfoContainer.innerHTML = "";
    serverInfoContainer.removeAttribute("data-search-addr");
    const targetUrl = new URL(location.protocol + '//' + location.host + location.pathname);
    targetUrl.searchParams.set("search", searchInput.value);
    const response = await fetch(targetUrl.toString(), {
        method: "GET",
        headers: {
            "x-fetch-subview": "1"
        }
    });

    function finalize() {
        searchButton.disabled = false;
        if (pushStateToHistory) {
            window.history.pushState({}, "", targetUrl.toString());
        }
    }

    if (!response.ok) {
        serverInfoFetchHint.innerHTML = await response.text();
        finalize();
        return;
    }

    const responseBody = await response.text();
    serverInfoFetchHint.classList.add("hide");
    serverInfoContainer.classList.remove("hide");
    serverInfoContainer.innerHTML = responseBody;
    serverInfoContainer.setAttribute("data-search-addr", searchInput.value);
    document.title = `${document.querySelector(".server_name").innerHTML} - Info`;
    finalize();
}

searchForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    await fetchServerInfo(true);
});

document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("search")) {
        searchInput.value = urlParams.get("search").trim();
    }
    searchButton.disabled = !validateHostnamePattern(searchInput.value);
});

window.addEventListener("popstate", async () => {
    const currentSearchAddr = serverInfoContainer.getAttribute("data-search-addr");
    const urlParams = new URLSearchParams(window.location.search);
    if (!urlParams.has("search") || !urlParams.get("search")) {
        serverInfoFetchHint.innerHTML = "Enter a server address and press &quot;Query&quot;.";
        serverInfoFetchHint.classList.remove("hide");
        serverInfoContainer.classList.add("hide");
        document.title = "L4Q";
        return;
    }
    if (urlParams.get("search").trim() !== searchInput.value.trim()) {
        searchInput.value = urlParams.get("search").trim();
    }
    if ((urlParams.has("search") && urlParams.get("search").trim() !== currentSearchAddr) ||
        serverInfoContainer.classList.contains("hide")) {
        await fetchServerInfo(false);
    }
});

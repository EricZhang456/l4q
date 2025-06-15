const serverInfo = document.querySelector(".server_info_container");

function fetchPlayerList() {
    if (serverInfo.innerHTML) {
        const playerListTable = document.querySelector(".server_player_list");
        if (playerListTable) {
            playerListTable.classList.remove("hide");
        }
        const playerListTableBody = document.querySelector(".server_player_list tbody");
        const urlParams = new URLSearchParams(window.location.search);
        const serverAddr = urlParams.get("search");
        fetch(`/search/player_list?search=${serverAddr}`)
        .then(response => {
            if (response.ok) {
                return response.text();
            }
            return Promise.reject(response);
        })
        .then(response => playerListTableBody.innerHTML = response)
        .catch(() => {
            return;
        });
    }
}

function sortTable(table, column, asc = true) {
    const sortDir = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    const sortedRows = rows.sort((a, b) => {
        let aCol, bCol;
        switch (column) {
            case 0:
                aCol = a.querySelector("th").textContent.trim().toLowerCase();
                bCol = b.querySelector("th").textContent.trim().toLowerCase();
                break;
            case 1:
                aCol = parseInt(a.querySelector(`td:nth-child(${column + 1})`).getAttribute("data-duration"));
                bCol = parseInt(b.querySelector(`td:nth-child(${column + 1})`).getAttribute("data-duration"));
                break;
        }
        return aCol > bCol ? (1 * sortDir) : (-1 * sortDir);
    });

    while (tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    tBody.append(...sortedRows);

    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${column + 1})`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${column + 1})`).classList.toggle("th-sort-desc", !asc);
}

function attachSortTablesButtons() {
    document.querySelectorAll(".server_player_list th").forEach(headerCell => {
        headerCell.addEventListener("click", () => {
            const tableElement = headerCell.parentElement.parentElement.parentElement;
            const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
            const currentIsAscending = headerCell.classList.contains("th-sort-asc");
            sortTable(tableElement, headerIndex, !currentIsAscending);
        });
        headerCell.addEventListener("keyup", event => {
            if (event.key === "Enter" || event.key === " ") {
                headerCell.click();
            }
        });
        headerCell.addEventListener("keydown", event => {
            if (event.key === " ") {
                event.preventDefault();
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("search")) {
        fetchPlayerList();
        attachSortTablesButtons();
    }
});

const observer = new MutationObserver(() => {
    fetchPlayerList();
    attachSortTablesButtons();
});
observer.observe(serverInfo, { childList: true });

# l4q

A website to query Left 4 Dead 2 servers, complete with game mode, difficulty and everything.

## Setup

1. Create a virtual environment and install all the dependencies from requirements.txt

```bash
python -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and set L4D2_ADDRESS to a random Left 4 Dead 2 server. This is used to fetch the latest version number for Left 4 Dead 2.

3. Deploy the application.

## Licensing

L4Q is licesed under [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html).

SVG files are from [Bootstrap Icons](https://icons.getbootstrap.com/). Campaign thumbnails are extracted from the Left 4 Dead 2 game files and are properties of Valve.


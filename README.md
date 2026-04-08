# bizarro-google

Small Python scripts for:

- fetching `robots.txt` disallow targets from a domain list
- collecting page bodies from those disallow URLs
- extracting forms from the collected HTML
- searching the extracted results from the command line

## Environment

This repository now includes a Cursor Cloud environment in `.cursor/environment.json`
backed by `.cursor/Dockerfile`.

- Python: 3.11
- Package manager: `pip`
- Runtime dependencies: `formasaurus`, `grequests`, `tabulate`

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

Run the scripts from the repository root:

```bash
python antig.py
python get_forms.py
python search.py searchurl example.com
```

`search.py` supports these modes:

- `searchurl`
- `searchbody`
- `searchformtype`
- `searchformfield`

## Data flow

1. `antig.py` reads `top-1m.csv` and writes `robots_results.txt` plus
   `final_results.jl`
2. `get_forms.py` reads `final_results.jl` and writes `final_results_forms.jl`
3. `search.py` searches `final_results_forms.jl`

## Tests

There is no committed automated test suite in this repository yet. A reasonable
smoke check after setup is:

```bash
python -m py_compile antig.py get_forms.py search.py
python -c "import formasaurus, grequests, tabulate; print('dependencies OK')"
```

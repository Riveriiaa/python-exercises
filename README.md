# Python exercises

A collection of Python exercises from my ICT engineering studies at Metropolia University of Applied Sciences.

The exercises cover programming fundamentals, object-oriented programming, MySQL, HTTP APIs and small Flask applications. Files are grouped by course module. Each numbered file is a separate exercise.

## Modules

| Folder | Topics |
| --- | --- |
| `Module2` | Input, variables, arithmetic and unit conversions |
| `Module3` | Conditions, comparisons and leap years |
| `Module4` | While loops, guessing games and estimating pi |
| `Module5` | For loops, lists, sorting and prime numbers |
| `Module6` | Functions, dice, list processing and price comparisons |
| `Module7` | Sets, dictionaries and an airport directory |
| `Module8` | MySQL queries and distances between airports |
| `Module9` | Classes and a car simulation |
| `Module10` | Elevator, building and race classes |
| `Module11` | Inheritance with publications and vehicles |
| `Module12` | HTTP API clients: jokes and weather |
| `Module13` | Flask endpoints for prime numbers and airport information |

## Run a basic exercise

With Python 3 installed, open a terminal in the repository folder:

```sh
python Module5/3.py
```

Basic exercises use the Python standard library. Some later exercises only define classes or functions; import those files in a Python console or add a small driver script to try them.

## Install optional dependencies

Modules 8 and 13 need additional packages. Use a virtual environment:

```sh
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux:

```sh
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Database exercises

Modules 8 and `Module13/2.py` expect a MySQL database with an `airport` table. The course database and its dataset are not included in this repository.

The queries use these columns: `ident`, `name`, `municipality`, `type`, `iso_country`, `latitude_deg` and `longitude_deg`.

Set the connection details before running a database exercise. In PowerShell:

```powershell
$env:DB_HOST = "127.0.0.1"
$env:DB_PORT = "3306"
$env:DB_NAME = "flight_game"
$env:DB_USER = "your_database_user"
$env:DB_PASSWORD = "your_database_password"
python Module8/1.py
```

On macOS / Linux, set the same variables with `export NAME="value"`. `DB_PASSWORD` is required. The other defaults are `127.0.0.1`, `3306`, `flight_game` and `root`, respectively.

## Weather exercise

`Module12/2.py` uses an OpenWeather API key supplied through an environment variable. In PowerShell:

```powershell
$env:OPENWEATHER_API_KEY = "your_api_key"
python Module12/2.py
```

On macOS / Linux, use `export OPENWEATHER_API_KEY="your_api_key"`.

## Flask examples

Run one application at a time:

```sh
python Module13/1.py
```

Open <http://127.0.0.1:3000/alkuluku/17> to check a prime number.

For the airport endpoint, configure the database variables and run:

```sh
python Module13/2.py
```

Open <http://127.0.0.1:3000/kentta/EFHK> to query the configured course database.

Both Flask examples run locally in development mode. API exercises require internet access. Keep API keys, database passwords and local configuration out of Git.

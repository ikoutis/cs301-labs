# Source of the weather data

`newark-weather.csv` is the dataset of Unit I of the course: one row for each day
from 2006-01-01 to 2024-12-31 at Newark Liberty International Airport, New Jersey,
6,940 days in all. It is a copy of the file that the Unit I notebooks read from
<https://ikoutis.github.io/course-notes/artificial-neuron-notes/data/newark-weather.csv>,
kept here so that the Unit II notebooks read every file from one site.

- **Source:** NOAA, Global Historical Climatology Network Daily (GHCN-Daily),
  station USW00014734,
  <https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00014734.csv>.
  Fetched on 2026-09-09.
- **Licence:** a work of the United States government, in the public domain.
  Credit: NOAA National Centers for Environmental Information.
- **Changes:** the years 2006 to 2024 were selected, the measurements were
  converted from NOAA's storage units to the units of a weather report (degrees
  Fahrenheit, hectopascals, inches, miles per hour), and the column `warm_half`
  was added.

| Column | Meaning | Unit |
|---|---|---|
| `date` | the day | YYYY-MM-DD |
| `tmax_f` | highest temperature of the day | °F |
| `tmin_f` | lowest temperature of the day | °F |
| `humidity_pct` | average relative humidity | % |
| `pressure_hpa` | average sea-level pressure | hPa |
| `precip_in` | precipitation | inches |
| `wind_mph` | average wind speed | miles per hour |
| `warm_half` | 1 if the month is May to October, else 0 | 0 or 1 |

A reading that the station did not report is an empty field: 64 days have no
humidity, 75 no pressure, and 2 no wind. The notebooks of Unit I, and the
notebook of meeting 11, drop the days that lack a temperature, the humidity or
the pressure, which leaves 6,865 days.

`meeting-11-act-1.ipynb` (Step 8) applies to these days the four season units
that were trained in meeting 8 of the course. Their weights and biases, and the
means and standard deviations that standardize the two temperatures, are written
in that notebook.

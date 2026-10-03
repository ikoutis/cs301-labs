# Sources of the Unit II datasets

Every file in this folder was made from a dataset of the
[UCI Machine Learning Repository](https://archive.ics.uci.edu) by
`tools/build_unit2_datasets.py`. Each source is licensed under the licence
named in its entry, which permits sharing and adapting the data when credit
is given and changes are stated. The entries below give that credit and
state the changes.

In every file the columns are numeric, no value is missing, and no column
is constant. Values were not rescaled or rounded.

## 1. MAGIC Gamma Telescope

- **File:** `01-magic-gamma-telescope.csv` (19,020 rows, 10 columns)
- **Source:** R. Bock (2004). MAGIC Gamma Telescope [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C52C8B>
- **Repository page:** <https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 2. HTRU2 Pulsar Candidates

- **File:** `02-pulsar-candidates.csv` (17,898 rows, 8 columns)
- **Source:** Robert Lyon (2015). HTRU2 [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5DK6R>
- **Repository page:** <https://archive.ics.uci.edu/dataset/372/htru2>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 3. Appliances Energy Prediction

- **File:** `03-appliances-energy.csv` (19,735 rows, 28 columns)
- **Source:** Luis Candanedo (2017). Appliances Energy Prediction [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5VC8G>
- **Repository page:** <https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The date column was removed.

## 4. Superconductivity Data

- **File:** `04-superconductivity.csv` (10,632 rows, 82 columns)
- **Source:** Kam Hamidieh (2018). Superconductivty Data [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C53P47>
- **Repository page:** <https://archive.ics.uci.edu/dataset/464/superconductivty+data>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** Every second row was kept (10,632 of 21,263).

## 5. Gas Turbine CO and NOx Emission Data Set

- **File:** `05-gas-turbine-emissions.csv` (36,733 rows, 11 columns)
- **Source:** (2019). Gas Turbine CO and NOx Emission Data Set [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5WC95>
- **Repository page:** <https://archive.ics.uci.edu/dataset/551/gas+turbine+co+and+nox+emission+data+set>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The year column was removed.

## 6. Bike Sharing

- **File:** `06-bike-sharing-hourly.csv` (17,379 rows, 15 columns)
- **Source:** Hadi Fanaee-T (2013). Bike Sharing [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5W894>
- **Repository page:** <https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The row counter and the date column were removed.

## 7. Beijing PM2.5

- **File:** `07-beijing-pm25.csv` (41,757 rows, 11 columns)
- **Source:** Song Chen (2015). Beijing PM2.5 [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5JS49>
- **Repository page:** <https://archive.ics.uci.edu/dataset/381/beijing+pm2+5+data>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The row counter and the wind-direction column (text) were removed, and so were the 2,067 hours with no PM2.5 reading.

## 8. Individual Household Electric Power Consumption

- **File:** `08-household-power.csv` (136,619 rows, 7 columns)
- **Source:** Georges Hebrail; Alice Berard (2006). Individual Household Electric Power Consumption [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C58K54>
- **Repository page:** <https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The date and time columns and the 25,979 minutes with missing measurements were removed; then every fifteenth row was kept.

## 9. Online News Popularity

- **File:** `09-online-news-popularity.csv` (19,822 rows, 60 columns)
- **Source:** Kelwin Fernandes; Pedro Vinagre; Paulo Cortez; Pedro Sernadela (2015). Online News Popularity [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5NS3V>
- **Repository page:** <https://archive.ics.uci.edu/dataset/332/online+news+popularity>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The url column was removed and every second row was kept (19,822 of 39,644).

## 10. Electrical Grid Stability Simulated Data

- **File:** `10-electrical-grid-stability.csv` (10,000 rows, 13 columns)
- **Source:** Vadim Arzamasov (2018). Electrical Grid Stability Simulated Data [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5PG66>
- **Repository page:** <https://archive.ics.uci.edu/dataset/471/electrical+grid+stability+simulated+data>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The text column stabf (stable or unstable) was removed.

## 11. Letter Recognition

- **File:** `11-letter-recognition.csv` (20,000 rows, 16 columns)
- **Source:** David Slate (1991). Letter Recognition [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5ZP40>
- **Repository page:** <https://archive.ics.uci.edu/dataset/59/letter+recognition>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The column that names the letter was removed.

## 12. Pen-Based Recognition of Handwritten Digits

- **File:** `12-pen-digits.csv` (10,992 rows, 16 columns)
- **Source:** E. Alpaydin; Fevzi. Alimoglu (1996). Pen-Based Recognition of Handwritten Digits [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5MG6K>
- **Repository page:** <https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 13. EEG Eye State

- **File:** `13-eeg-eye-state.csv` (14,980 rows, 14 columns)
- **Source:** Oliver Roesler (2013). EEG Eye State [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C57G7J>
- **Repository page:** <https://archive.ics.uci.edu/dataset/264/eeg+eye+state>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The eye-state column was removed.

## 14. Dry Bean

- **File:** `14-dry-bean.csv` (13,611 rows, 16 columns)
- **Source:** (2020). Dry Bean [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C50S4B>
- **Repository page:** <https://archive.ics.uci.edu/dataset/602/dry+bean+dataset>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 15. Skin Segmentation

- **File:** `15-skin-segmentation.csv` (245,057 rows, 3 columns)
- **Source:** Rajen Bhatt; Abhinav Dhall (2009). Skin Segmentation [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5T30C>
- **Repository page:** <https://archive.ics.uci.edu/dataset/229/skin+segmentation>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column y was removed.

## 16. Statlog (Landsat Satellite)

- **File:** `16-landsat-satellite.csv` (6,435 rows, 36 columns)
- **Source:** Ashwin Srinivasan (1993). Statlog (Landsat Satellite) [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C55887>
- **Repository page:** <https://archive.ics.uci.edu/dataset/146/statlog+landsat+satellite>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 17. Spambase

- **File:** `17-spambase.csv` (4,601 rows, 57 columns)
- **Source:** Mark Hopkins; Erik Reeber; George Forman; Jaap Suermondt (1999). Spambase [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C53G6X>
- **Repository page:** <https://archive.ics.uci.edu/dataset/94/spambase>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column was removed.

## 18. Musk (Version 2)

- **File:** `18-musk-molecules.csv` (6,598 rows, 166 columns)
- **Source:** David Chapman; Ajay Jain (1994). Musk (Version 2) [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C51608>
- **Repository page:** <https://archive.ics.uci.edu/dataset/75/musk+version+2>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The two name columns and the class column were removed.

## 19. Default of Credit Card Clients

- **File:** `19-credit-card-clients.csv` (30,000 rows, 23 columns)
- **Source:** I-Cheng Yeh (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C55S3H>
- **Repository page:** <https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The ID column and the class column Y were removed, and columns X1 to X23 were renamed to the names given in the repository's variable table.

## 20. Metro Interstate Traffic Volume

- **File:** `20-metro-traffic.csv` (48,204 rows, 5 columns)
- **Source:** John Hogue (2019). Metro Interstate Traffic Volume [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5X60B>
- **Repository page:** <https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The text columns (holiday, weather description, date and time) were removed.

## 21. Power Consumption of Tetouan City

- **File:** `21-tetouan-power.csv` (52,416 rows, 8 columns)
- **Source:** Abdulwahed Salam; Abdelaaziz El Hibaoui (2018). Power Consumption of Tetouan City [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5B034>
- **Repository page:** <https://archive.ics.uci.edu/dataset/849/power+consumption+of+tetouan+city>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The date and time column was removed.

## 22. Steel Industry Energy Consumption

- **File:** `22-steel-industry-energy.csv` (35,040 rows, 7 columns)
- **Source:** Sathishkumar V E; Changsun Shin; Yongyun Cho (2021). Steel Industry Energy Consumption [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C52G8C>
- **Repository page:** <https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The date column and three text columns were removed.

## 23. Room Occupancy Estimation

- **File:** `23-room-occupancy.csv` (10,129 rows, 17 columns)
- **Source:** Adarsh Pal Singh; Sachin Chaudhari (2018). Room Occupancy Estimation [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5P605>
- **Repository page:** <https://archive.ics.uci.edu/dataset/864/room+occupancy+estimation>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The date and time columns were removed.

## 24. Covertype

- **File:** `24-forest-covertype.csv` (96,836 rows, 10 columns)
- **Source:** Jock Blackard (1998). Covertype [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C50K5N>
- **Repository page:** <https://archive.ics.uci.edu/dataset/31/covertype>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** Only the ten quantitative columns were kept (the 44 indicator columns and the class column were removed), and every sixth row was kept (96,836 of 581,012).

## 25. Taiwanese Bankruptcy Prediction

- **File:** `25-company-financial-ratios.csv` (6,819 rows, 94 columns)
- **Source:** (2020). Taiwanese Bankruptcy Prediction [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5004D>
- **Repository page:** <https://archive.ics.uci.edu/dataset/572/taiwanese+bankruptcy+prediction>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** The class column and the column Net Income Flag, which has the same value in every row, were removed.

## 26. Physicochemical Properties of Protein Tertiary Structure

- **File:** `26-protein-structure.csv` (45,730 rows, 10 columns)
- **Source:** Prashant Rana (2013). Physicochemical Properties of Protein Tertiary Structure [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5QW3H>
- **Repository page:** <https://archive.ics.uci.edu/dataset/265/physicochemical+properties+of+protein+tertiary+structure>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** No change: CASP.csv as distributed.

## 27. SGEMM GPU Kernel Performance

- **File:** `27-gpu-kernel-performance.csv` (48,320 rows, 18 columns)
- **Source:** Enrique Paredes; Rafael Ballester-Ripoll (2017). SGEMM GPU kernel performance [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5MK70>
- **Repository page:** <https://archive.ics.uci.edu/dataset/440/sgemm+gpu+kernel+performance>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** Every fifth row was kept (48,320 of 241,600).

## 28. Accelerometer

- **File:** `28-fan-accelerometer.csv` (153,000 rows, 5 columns)
- **Source:** Gustavo Scalabrini Sampaio; Arnaldo Rabello de Aguiar Vallim Filho; Leilton Santos de Silva; Leandro Augusto da Silva (2019). Accelerometer [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5Q61V>
- **Repository page:** <https://archive.ics.uci.edu/dataset/846/accelerometer>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** No change: the file as distributed.

## 29. Beijing Multi-Site Air Quality

- **File:** `29-beijing-air-quality.csv` (31,876 rows, 15 columns)
- **Source:** Song Chen (2017). Beijing Multi-Site Air Quality [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5RK5G>
- **Repository page:** <https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** Only the Aotizhongxin station's file was used. The row counter, the wind-direction column (text) and the station name were removed, and so were the 3,188 hours with a missing value in the columns that remain.

## 30. Crowdsourced Mapping

- **File:** `30-land-cover-ndvi.csv` (10,545 rows, 28 columns)
- **Source:** Brian Johnson (2016). Crowdsourced Mapping [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C56315>
- **Repository page:** <https://archive.ics.uci.edu/dataset/400/crowdsourced+mapping>
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Changes:** Only training.csv was used, and its class column was removed.

# Rwanda Eastern Province Drought Analysis

Interactive mapping and data analysis of drought patterns and their socio-economic impacts in the Eastern Province of Rwanda (2021-2022).

## 🌍 Interactive Maps
Once GitHub Pages is enabled in your repository settings, you can access the live maps here:

*   **[Current Rainfall & Population Map](https://entaganzwa.github.io/Crash-Course-1/index.html)**: Shows the latest rainfall anomalies (% of normal) by district, integrated with 2022 Census population data.
*   **[Drought Damage & Impact Map](https://entaganzwa.github.io/Crash-Course-1/drought_damage_map.html)**: Visualizes the agricultural and economic impacts of the 2021-2022 drought cycle, including household assistance and crop loss details.
*   **[Ghana Historic Flood Events Map](https://entaganzwa.github.io/Crash-Course-1/ghana_floods_map.html)**: Interactive map of historic flood events in Ghana, showing severity and human impact (displacement).

## 📊 2022 Population Data by District
| District | Population (2022 Census) |
| :--- | :--- |
| **Nyagatare** | 653,861 |
| **Gatsibo** | 551,164 |
| **Bugesera** | 551,103 |
| **Rwamagana** | 484,953 |
| **Kirehe** | 460,860 |
| **Kayonza** | 457,156 |
| **Ngoma** | 404,048 |

## 📉 Drought Impact Summary (2021-2022)
*   **Economic Loss:** Estimated between **$2M and $7.5M USD** for the Eastern Province.
*   **Food Security:** Over **36,000 households** in Kirehe alone required emergency food aid.
*   **Agricultural Production:** Maize and bean yields dropped significantly (up to 50% wilting in some districts like Kayonza).
*   **Livestock:** Pasture degradation and Rift Valley Fever outbreaks in Nyagatare and Kayonza.

## 🛠️ Data Processing
The project includes Python scripts to filter and prepare data from raw sources:

- `scripts/filter_ghana_floods.py`: Filters the global FloodArchive Excel file for Ghana-specific events.
- `scripts/filter_rwanda_drought.py`: Filters the Rwanda 5-year rainfall dataset for Eastern Province districts and adds descriptive names.

To run these scripts, ensure you have `pandas` and `openpyxl` installed:
```bash
pip install pandas openpyxl
python3 scripts/filter_rwanda_drought.py
python3 scripts/filter_ghana_floods.py
```

## 📂 Project Structure

- `index.html`: Main Leaflet map for rainfall anomalies.
- `drought_damage_map.html`: Impact and damage visualization.
- `ghana_floods_map.html`: Ghana flood risk dashboard.
- `data/`: Folder containing all CSV, JSON, and XLSX data sources.
- `scripts/`: Python scripts for data processing and analysis.

---
*Data Source: National Institute of Statistics of Rwanda (NISR), 2022 Population and Housing Census, and FAO/WFP Impact Reports.*

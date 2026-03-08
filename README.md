# Mumbai Weather Data Analysis

## Project Overview
This project performs an exploratory data analysis on a historical weather dataset for Mumbai, India, covering the years 1951–2024. The dataset contains daily records of rainfall, maximum temperature, and minimum temperature. The analysis includes cleaning, deriving key metrics, and creating visualisations to understand long‑term trends and seasonal patterns.

## Code Structure
- `main.py` – main Python script that loads the data, cleans it, computes statistics, and generates plots.
- `data/` – folder containing the raw dataset (`Weather dataset.csv`).
- `visualizations/` – folder where all generated charts are saved (PNG files).
- `report/` – folder containing the final report (`final_report.md`) with embedded charts and insights.
- `requirements.txt` – list of required Python libraries.

## Setup Instructions
1. Install Python from [python.org](https://python.org).
2. Install required packages:
   ```bash
   pip install pandas matplotlib numpy
3. Clone this repository or download the files.
4. Place the dataset as Weather dataset.csv.
5. Run the analysis script.
6. View the generated charts in the visualizations folder and read the report in final_report.md.

## Visual Documentation
- All charts are embedded in the final report (see report/final_report.md).

## Testing Evidence
- Missing values in temperature columns were handled by dropping rows with NaN – this ensures that averages are computed only on valid data.
- Rainfall values marked as Tr (trace) were treated as zero for total rainfall but counted as rainy days, preserving the distinction.
- The script was tested on the full dataset and produced the expected plots without errors.
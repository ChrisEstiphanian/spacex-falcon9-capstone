# Winning the Space Race with Data Science

IBM Applied Data Science Capstone: predicting whether a SpaceX Falcon 9 first stage will land successfully.

| # | Notebook | What it does |
|---|----------|--------------|
| 1 | `1_data_collection_api.ipynb` | Collect launch data from the SpaceX REST API |
| 2 | `2_webscraping.ipynb` | Scrape Falcon 9 launch records from Wikipedia |
| 3 | `3_data_wrangling.ipynb` | Clean the data and create the landing label `Class` |
| 4 | `4_eda_sql.ipynb` | Exploratory analysis with SQL (SQLite) |
| 5 | `5_eda_visualization.ipynb` | Exploratory analysis with charts, plus feature engineering |
| 6 | `6_folium_launch_sites.ipynb` | Interactive launch site maps with Folium |
| – | `spacex_dash_app.py` | Plotly Dash dashboard (`python spacex_dash_app.py`) |
| 7 | `7_machine_learning_prediction.ipynb` | Logistic Regression, SVM, Decision Tree and KNN with GridSearchCV |

## Key results
- 90 Falcon 9 launches (2010–2020); overall landing success 66.7%, rising to 90% in 2019
- KSC LC-39A has the highest launch-site success rate (76.9%)
- Landing legs, grid fins, Block 5 and reused boosters strongly raise success
- Best model: SVM (84.8% cross-validation accuracy, 83.3% test accuracy)

Run the notebooks in order; each one writes the CSV the next one reads (copies are in `data/`).
Charts and map screenshots are in `figures/`.

```
pip install -r requirements.txt
```

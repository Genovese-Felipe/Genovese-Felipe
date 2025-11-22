# Step 3: AI Analysis & Recommendations

This script uses Machine Learning (Isolation Forest) to find energy anomalies and a Rule Engine to suggest construction upgrades.

## What this script does
1.  **Fetches** data from ClickHouse.
2.  **Runs** an Isolation Forest model to identify "anomalous" energy spikes (e.g., AC running when it's not that hot).
3.  **Matches** inefficient homes with products from our `retrofit_materials` table.

---

### Option 1: VS Code + Copilot
1.  **Run:** `python analysis_ai.py`
2.  **Explore:** Look at the "Retrofit Recommendations" table in the output.
3.  **Copilot Challenge:** Ask Copilot: *"Explain how the Isolation Forest model is being used here to detect anomalies."*

### Option 2: JetBrains (PyCharm)
1.  **Run:** Right-click `analysis_ai.py` -> Run.
2.  **Debug:** Set a breakpoint on `df['anomaly'] = model.fit_predict(features)`. Inspect the `df` dataframe to see which rows were marked as -1 (anomalies).

### Option 3: Google Colab
1.  **Cell:**
    ```python
    from analysis_ai import analyze_efficiency, recommend_retrofits
    summary, anomalies = analyze_efficiency()
    recs = recommend_retrofits(summary)

    # Display nicely in Colab
    import pandas as pd
    display(recs)
    ```

### Option 4: Vibe Coding
1.  **Prompt:** *"Run the analysis script. Then, visualize the anomalies using a simple ASCII chart or tell me which home has the most anomalies."*
2.  **Result:** The Agent should analyze the output and summarize: "Home_A_Drafty has the most anomalies, suggesting it needs immediate retrofitting."

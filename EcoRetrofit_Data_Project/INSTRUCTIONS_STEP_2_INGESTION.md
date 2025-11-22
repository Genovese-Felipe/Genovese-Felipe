# Step 2: Data Generation & Ingestion Instructions

Now we will populate the database with synthetic "Smart Home" data and a catalog of construction materials.

## What this script does
- **Generates** hourly data for 5 homes (Drafty, Eco, Standard, etc.) for 30 days.
- **Simulates** physics: How outside temperature affects energy consumption based on insulation.
- **Uploads** this data to your ClickHouse Cloud instance.

---

### Option 1: VS Code + Copilot
1.  **Open Terminal:** In VS Code (`Ctrl+` `).
2.  **Run Script:** `python generate_data.py`
3.  **Monitor:** Watch the output. It should say "Ingesting Retrofit Materials..." and then "Ingested X sensor readings".
4.  **AI Interaction:** Ask Copilot: *"How can I modify this script to generate 365 days of data instead of 30?"* (Hint: Change the `days=30` argument).

### Option 2: JetBrains (PyCharm)
1.  **Locate Script:** Find `generate_data.py` in the project view.
2.  **Run:** Right-click -> Run 'generate_data'.
3.  **Verify:** Open the "Database" tool window in PyCharm (if you have the plugin) or just trust the console output.

### Option 3: Google Colab
1.  **Upload:** Upload `generate_data.py` and `setup_database.py`.
2.  **Cell:**
    ```python
    from generate_data import ingest_data
    ingest_data()
    ```
3.  **Output:** You will see the print statements directly in the notebook.

### Option 4: Vibe Coding
1.  **Prompt:** *"Run the data generation script. After it finishes, write a SQL query to count how many rows are in the `smart_home_sensors` table to verify it worked."*
2.  **Verification:** The Agent should return a number (approx 3600 rows per home x 5 homes = 18,000 rows).

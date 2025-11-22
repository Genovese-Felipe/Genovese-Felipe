# Step 1: Database Setup Instructions

This step initializes your ClickHouse database with the necessary tables for our Smart Home Analysis.

## Prerequisites
1.  Ensure you have your **ClickHouse Cloud** credentials ready (Host, Password).
2.  Create a `.env` file in the `EcoRetrofit_Data_Project` folder with the content from `.env.example`.

---

### Option 1: VS Code + GitHub Copilot (Recommended)
1.  **Open the Folder:** Open `EcoRetrofit_Data_Project` in VS Code.
2.  **Install Extensions:** Ensure you have the Python extension installed.
3.  **Environment Setup:**
    - Open a terminal (`Ctrl+` `).
    - Create a virtual environment: `python -m venv venv`
    - Activate it:
        - Windows: `venv\Scripts\activate`
        - Mac/Linux: `source venv/bin/activate`
    - Install deps: `pip install -r requirements.txt`
4.  **Run Script:**
    - Open `setup_database.py`.
    - Click the "Run" button (play icon) or type `python setup_database.py` in the terminal.
    - **Copilot Tip:** Ask Copilot "Explain what this script does" to understand the schema.

### Option 2: JetBrains IDE (PyCharm)
1.  **Open Project:** Open the `EcoRetrofit_Data_Project` folder.
2.  **Configure Interpreter:**
    - PyCharm will suggest creating a virtual environment. Accept it.
    - Or go to `Settings > Project > Python Interpreter` and add a new one.
3.  **Install Packages:**
    - Open `requirements.txt`.
    - PyCharm usually shows a banner "Install requirements". Click it.
4.  **Run:**
    - Right-click `setup_database.py` and select "Run 'setup_database'".
    - Check the "Run" tab at the bottom for "Table created" messages.

### Option 3: Google Colab (Cloud)
1.  **Upload Files:** Drag `setup_database.py` and `.env` (if safe) to the Colab file explorer. *Note: Be careful uploading .env files to public notebooks.*
2.  **Install Libraries:** Create a code cell:
    ```python
    !pip install clickhouse-connect python-dotenv
    ```
3.  **Run Script:** Create another cell:
    ```python
    from setup_database import create_tables
    # You might need to hardcode credentials here if .env fails in Colab
    create_tables()
    ```

### Option 4: Vibe Coding (Cursor / Replit / AI Agents)
1.  **Prompt the Agent:**
    - "I have a `setup_database.py` file. Please install the dependencies and run it for me."
2.  **Context:** Ensure the Agent has access to your `.env` variables (most AI IDEs have a secure way to store secrets).
3.  **Verify:** Ask the Agent: "Check if the tables `smart_home_sensors` and `retrofit_materials` exist in the database now."

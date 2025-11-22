# Future Studies: Autodesk BIM & Generative Design Integration

This project establishes the **Data Layer** (ClickHouse) and **Logic Layer** (AI). The next logical step is the **Physical Layer** (BIM).

## Proposed Workflow
1.  **BIM Model (Revit):**
    - Create a detailed model of the "Drafty Home".
    - Assign parameters to walls/windows: `u_value`, `material_cost`, `embodied_carbon`.

2.  **Dynamo / Revit API:**
    - Write a script to **fetch** the "Recommendation" from ClickHouse (e.g., "Upgrade to Rockwool").
    - Automatically **swap** the Wall Type in Revit to the recommended material.

3.  **Generative Design:**
    - Use Autodesk Generative Design to iterate through thousands of retrofit combinations (Windows vs. Insulation vs. HVAC).
    - Use ClickHouse to store the simulation results of each iteration for rapid querying.

4.  **Digital Twin:**
    - Connect the live sensor stream from ClickHouse to the Revit model via **Autodesk Tandem**.
    - Visualize real-time temperature as a heat map on the 3D model.

# Troubleshooting Guide

## 1. Connection Failures
**Error:** `clickhouse_connect.driver.exceptions.DatabaseError`
**Solution:**
- Check your `.env` file.
- Ensure your IP is allowed in ClickHouse Cloud (whitelist `0.0.0.0/0` for development if safe, or your specific IP).
- If using "Native" protocol, ensure port 9440 is open. For HTTPS, use 8443.

## 2. Missing Data
**Error:** Empty charts or tables.
**Solution:**
- Run `python generate_data.py` again to repopulate the database.
- Ensure the `ingest_data()` function actually ran without errors.

## 3. Streamlit Not Opening
**Issue:** `streamlit run app.py` doesn't open a browser.
**Solution:**
- Look for the "Local URL" in the terminal (e.g., `http://localhost:8501`).
- Ctrl+Click that link.

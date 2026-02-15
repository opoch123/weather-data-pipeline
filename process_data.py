import duckdb

# Create a connection (this creates a dummy database in memory)
con = duckdb.connect()

# SQL Query: Filter for cities warmer than 20 degrees
# Note: DuckDB treats the JSON file like a table automatically!
query = "SELECT * FROM 'daily_report.json' WHERE temperature > 20"

print("--- Cities with Temperature > 20°C ---")
con.sql(query).show()
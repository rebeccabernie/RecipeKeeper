# Code adapted from
# https://docs.python.org/2/library/sqlite3.html
import sqlite3

DATABASE = 'recipes.db' # Sets DATABASE to recipes file in subfolder

def setup_db():
    # Create database if it doesn't exist
    db = sqlite3.connect(DATABASE) # Create connection object, represents database. Data stored in DATABASE, defined above
    cur = db.cursor() # Allows SQL commands to be performed

    # Create the table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS recipetable(name TEXT PRIMARY KEY, ingredients TEXT, methods TEXT)")
    db.commit() # Save changes
    
    # Insert example into database
    cur.execute("INSERT INTO recipetable VALUES('Pancakes', 'Eggs, Milk, SF Flour', 'Add all to bowl and mix.')")
    db.commit()
    db.close() # Close database

if __name__ == "__main__":
  setup_db()
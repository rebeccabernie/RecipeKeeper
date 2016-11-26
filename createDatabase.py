# Code adapted from
# https://docs.python.org/2/library/sqlite3.html
import sqlite3

DATABASE = 'recipes.db' # Sets DATABASE to recipes file in subfolder

def setup_db():
    # Create database if it doesn't exist
    db = sqlite3.connect(DATABASE) # Create connection object, represents database. Data stored in DATABASE, defined above
    cur = db.cursor() # Allows SQL commands to be performed

    # Create the tables if they don't exist
    # Breakfast Table = btable
    cur.execute("CREATE TABLE IF NOT EXISTS btable(name TEXT PRIMARY KEY, ingredients TEXT, method TEXT)")
    # Lunch Table = ltable
    cur.execute("CREATE TABLE IF NOT EXISTS ltable(name TEXT PRIMARY KEY, ingredients TEXT, method TEXT)")
    # Dinner Table = dtable
    cur.execute("CREATE TABLE IF NOT EXISTS dtable(name TEXT PRIMARY KEY, ingredients TEXT, methods TEXT)")
    # Sweet/Dessert Table = stable
    cur.execute("CREATE TABLE IF NOT EXISTS stable(name TEXT PRIMARY KEY, ingredients TEXT, methods TEXT)")
    
    db.commit() # Save changes
    
    # Insert examples into tables
    cur.execute("INSERT INTO btable VALUES('Pancakes', 'Eggs, Milk, SF Flour', 'Add all to bowl and mix.')")
    cur.execute("INSERT INTO ltable VALUES('Cheese Sandwich', 'Bread, Butter, Cheese', 'Butter bread, add cheese')")
    cur.execute("INSERT INTO dtable VALUES('Roast Chicken', 'Whole Chicken, Butter, Salt, Pepper', 'Put butter, salt and pepper on chicken')")
    cur.execute("INSERT INTO stable VALUES('Cupcake', 'Eggs, Sugar, Marg, SF Flour', 'Add all to bowl and mix.')")
    
    db.commit()
    db.close() # Close database

if __name__ == "__main__":
  setup_db()
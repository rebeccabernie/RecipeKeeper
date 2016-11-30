# Code adapted from
# https://docs.python.org/2/library/sqlite3.html
import sqlite3

DATABASE = 'recipes.db' # Sets DATABASE to recipes file in subfolder

def setup_db():
    # Create database if it doesn't exist
    connDB = sqlite3.connect(DATABASE) # Create connection object, represents database. Data stored in DATABASE, defined above
    cur = connDB.cursor() # Allows SQL commands to be performed

    # Create the tables if they don't exist
    cur.execute("CREATE TABLE IF NOT EXISTS recipeTable(rname TEXT, ing TEXT, method TEXT)")
    
    connDB.commit() # Save changes
    
    # Insert examples into tables
    cur.execute("INSERT INTO recipeTable(rname, ing, method) VALUES('Pancakes', 'Eggs, milk, flour', 'Add all and mix in a bowl')")
   
    connDB.commit()
    connDB.close() # Close database
    
if __name__ == "__main__":
    setup_db()
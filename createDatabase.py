# Code adapted from
# https://docs.python.org/2/library/sqlite3.html
import sqlite3

DATABASE = 'recipes.db' # Sets DATABASE to recipes file in subfolder

def setup_db():
    # Create database if it doesn't exist
    connDB = sqlite3.connect(DATABASE) # Create connection object, represents database. Data stored in DATABASE, defined above
    cur = connDB.cursor() # Allows SQL commands to be performed

    # Create the tables if they don't exist
    # Breakfast Table = btable
    cur.execute("CREATE TABLE IF NOT EXISTS btable(rname TEXT, ing TEXT, method TEXT, PRIMARY KEY (rname))")
    # Lunch Table = ltable
    #cur.execute("CREATE TABLE IF NOT EXISTS ltable(rname TEXT, ing TEXT, method TEXT, PRIMARY KEY (rname))")
    # Dinner Table = dtable
    #cur.execute("CREATE TABLE IF NOT EXISTS dtable(rname TEXT, ing TEXT, method TEXT, PRIMARY KEY (rname))")
    # Sweet/Dessert Table = stable
    #cur.execute("CREATE TABLE IF NOT EXISTS stable(rname TEXT, ing TEXT, method TEXT, PRIMARY KEY (rname))")
    
    connDB.commit() # Save changes
    
    # Insert examples into tables
    cur.execute("INSERT INTO btable (rname, ing, method) VALUES('Pancakes', 'Eggs, milk, flour', 'Add all and mix in a bowl')")
    #cur.execute("INSERT INTO ltable (rname, ing, method) VALUES('Cheese Sandwich', 'Bread, Butter, Cheese', 'Butter bread, add cheese')")
    #cur.execute("INSERT INTO dtable (rname, ing, method) VALUES('Roast Chicken', 'Whole Chicken, Butter, Salt, Pepper', 'Put butter, salt and pepper on chicken')")
    #cur.execute("INSERT INTO stable (rname, ing, method) VALUES('Cupcake', 'Eggs, Sugar, Marg, SF Flour', 'Add all to bowl and mix.')")
    
    connDB.commit()
    connDB.close() # Close database
    
if __name__ == "__main__":
    setup_db()
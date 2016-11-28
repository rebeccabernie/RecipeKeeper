import flask as fl
from flask import render_template, request, g
import sqlite3

DATABASE = 'recipes.db'
app = fl.Flask(__name__)

# Load database, adapted from https://github.com/data-representation/example-sqlite
def loadDB():
  db = getattr(fl.g, '_database', None)
  if db is None:
    db = fl.g._database = sqlite3.connect('recipes.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(fl.g, '_database', None)
  if db is not None:
    db.close()

@app.route("/")
def root():
    return render_template('index.html') # Load index.html file

@app.route("/add", methods=["GET", "POST"])
def addRecipe():
    cur = loadDB().cursor()
    conn = sqlite3.connect(DATABASE)
    curConn = conn.cursor()
    
    # Formatting for /VALUES(%s), var/ found at http://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python
    cur.execute("INSERT INTO btable(rname, ing, method) VALUES(?, ?, ?)",(fl.request.form['rname'],fl.request.form['ing'], fl.request.form['method']))   

    conn.commit()
    conn.close() # Close database
    
    render_template('basicTemplate.html') + str(cur.fetchall())

@app.route("/savedRecipes", methods=["GET", "POST"])
def savedRec():
    cur = loadDB().cursor()    
    cur.execute("Select * from btable")
    cur.execute("SELECT rname FROM btable")
    db.close() # Close database
    
    return (render_template('basicTemplate.html') + str(cur.fetchall()))

if __name__ == "__main__":
    app.run()
import flask as fl
import sqlite3

DATABASE = 'recipes.db'
app = fl.Flask(__name__)

# Load database, adapted from https://github.com/data-representation/example-sqlite
def loadDB():
  db = getattr(fl.g, '_database', None)
  if db is None:
    db = fl.g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def root():
    return app.send_static_file('index.html') # Load index.html file

@app.route("/add", methods=["GET", "POST"])
def bfast():
    rname = fl.request.values["rname"]
    ing = fl.request.values["ing"]
    method = fl.request.values["method"]

    db = sqlite3.connect(DATABASE) # Create connection object, represents database. Data stored in DATABASE, defined above
    cur = db.cursor() # Allows SQL commands to be performed

    # Formatting for /VALUES(%s), var/ found at http://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python
    cur.execute("INSERT INTO btable VALUES(?, ?, ?)", (rname, ing, method))

    db.commit()

    return rname

@app.route("/saved", methods=["GET", "POST"])
def savedRecipes():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    
    cur.execute("SELECT rname FROM btable")
    return str(cur.fetchall())

if __name__ == "__main__":
    app.run()
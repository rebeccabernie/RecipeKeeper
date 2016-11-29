import flask as fl
import sqlite3

app = fl.Flask(__name__)

DATABASE = 'recipes.db'
connDB = sqlite3.connect(DATABASE)
cur = connDB.cursor()

# Load database and close connection adapted from https://github.com/data-representation/example-sqlite
def loadDB():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect('recipes.db')
    return db
"""
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()
"""
@app.route("/")
def root():
    cur = loadDB().cursor()
    return app.send_static_file('index.html') # Load index.html file
    
@app.route("/add", methods=["GET", "POST"])
def addRecipe():
    cur.execute("INSERT INTO btable(rname, ing, method) VALUES(?, ?, ?)",(fl.request.form['rname'],fl.request.form['ing'],fl.request.form['method'],))
    #cur.execute("INSERT INTO btable(ing) VALUES(?)",(fl.request.form['ing'],))
    #cur.execute("INSERT INTO btable(method) VALUES(?)",(fl.request.form['method'],))
    connDB.commit()
    return str(cur.fetchall())
    
@app.route("/savedRecipes", methods=["GET", "POST"])
def savedRec():
    
    cur.execute("SELECT rname FROM btable")
    return str(cur.fetchall())

@app.route("/fullRecipe", methods=["GET", "POST"])
def fullRec():
    
    cur.execute("SELECT * FROM btable")
    return str(cur.fetchall())


if __name__ == "__main__":
    app.run()
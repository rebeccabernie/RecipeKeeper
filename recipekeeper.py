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
    return app.send_static_file('index.html') # Load index.html file
    cur.execute("SELECT rname FROM btable")
    return str(cur.fetchall())
    
@app.route("/add", methods=["GET", "POST"])
def addRecipe():
    #cur.execute("INSERT INTO ltable (rname, ing, method) VALUES('Cheese Sandwich', 'Bread, Butter, Cheese', 'Butter bread, add cheese')")
    cur.execute("INSERT INTO btable(rname) VALUES(?)",(fl.request.form['rname'],))
    connDB.commit()
    return str(cur.fetchall())
    
@app.route("/savedRecipes", methods=["GET", "POST"])
def savedRec():
    
    cur.execute("SELECT rname FROM btable")
    return str(cur.fetchall())


if __name__ == "__main__":
    app.run()
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
    #cur.execute("SELECT * FROM btable")
    return app.send_static_file('index.html') # Load index.html file
    
@app.route("/add", methods=["GET", "POST"])
def addRecipe():
    cur.execute("INSERT INTO recipeTable(rname, ing, method) VALUES(?, ?, ?)",(fl.request.form['rname'],fl.request.form['ing'],fl.request.form['method'],))
    connDB.commit()
    return str(cur.fetchall())
    
@app.route("/savedRecipes", methods=["GET", "POST"])
def savedRec():
    cur.execute("SELECT rname FROM recipeTable")
    return str(cur.fetchall())

@app.route("/fullRecipe", methods=["GET", "POST"])
def fullRec():
    name = request.form['nameform']
    ing = request.form['ingform']
    method = request.form['methodform']
    #print(fl.request.values["rname"])
    #rname = (fl.request.form['#rname'])
    cur.execute("SELECT * FROM recipeTable where rname = (?)", (name))
    return str(cur.fetchall())
    #return fl.request.values["rname"]

#WHERE rname LIKE ?", ('#rname')
    
#print(fl.request.values["rname"])
#return fl.request.values["rname"]

#rname = "%" + rname + "%";
#query = 'select * from btable where rname like "'+ name + '"'
#cur = recipes.rawQuery(query, null)
#cur.execute("SELECT * FROM btable WHERE rname LIKE %(?)%", (fl.request.form['#rname']))
#return str(cur.fetchall())

if __name__ == "__main__":
    app.run()
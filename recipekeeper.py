import flask as fl
import sqlite3

DATABASE = 'recipes/recipes.db'
app = fl.Flask(__name__)

# Load database
def get_db():
  db = getattr(fl.g, '_database', None)
  if db is None:
    db = fl.g._database = sqlite3.connect(DATABASE)
  return db

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/perms", methods=["GET", "POST"])
def perms():
	perms = [''.join(p) for p in it.permutations(fl.request.values["userinput"])]
	return '\n'.join(perms)

if __name__ == "__main__":
    app.run()
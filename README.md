# RecipeKeeper
###### Data Representation and Querying Project 2016
This is a  project for 3rd Year module Data Representation and Querying.

## Project Background 
This is a Single Page Web Application that allows the user to save recipe details to a database. 
My two initial ideas were 

1. A Scrabble Scoring system
2. A Recipe database

Initially I decided on the Scrabble option but after a few hours of coding it had proved to be more of a challenge than I had antipcated. After some thought and another read of the project instructions, I decided that a recipe database would actually be more suitable and possibly easier to complete in the timeframe. 

As an avid baker, this option was also more relevant to me personally. I find one of my biggest problems is writing recipes on bits of paper and subsequently losing the bits - this is a simple application that would solve this problem.


## Downloading and First Run
In order to run this application, you will need [Python 3](https://www.continuum.io/downloads) installed with the Flask library. The SQLite3 python package must also be installed.

Firstly, click on the green Clone/Download button in the top right corner of this page. 
If you simply want to use or test this app, click "Download ZIP", save it somewhere like your Desktop or Documents and extract the files into a folder. 

Open the command line/terminal (search cmd in Windows, terminal if you're on a Mac) and run
```
$ cd C:\Users\You\Documents\AppFolder
```

However, if you want to mess around with the code a bit you will have to clone the repository. Copy the URL in the Clone/Download drop-down. Open the command line/terminal (search cmd in Windows, terminal if you're on a Mac) and run 
```
$ cd C:\Users\You\YourFolder\FolderYouWantTheAppIn
$ git clone https://github.com/rebeccabernie/RecipeKeeper.git
$ cd FolderYouWantTheAppIn
```

After you've the folder set up, you'll need a database. In CL/Terminal, run
```
$ python createDatabase.py      // this creates the database
$ python recipekeeper.py        // this runs the application locally 
```

Once the file is running in CL/Terminal, open up a browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

I used [DB Browser for SQLite](http://sqlitebrowser.org/) to view the contents of my database on my machine - if you're editing the code I would recommend downloading and installing this program. It allowed me to make sure the program was in fact adding to the database, rather than going on what was displaying on http://127.0.0.1:5000/.

## Using the Application
1. Enter your Recipe details in the left column. If you've decided for some reason you don't want to save this recipe, just click the "Reset Form" button and enter a different recipe.
2. When you're happy with the details, click "Save Recipe". This will save your recipe details to the _recipes.db_ file in the application's folder.
3. A button with the name of your recipe will then appear in the middle column on the screen, click this to view the full details of your recipe.

Repeat as needed!

## Architecture / Languages

This web application runs in Python 3 using the Flask framework and SQLite3 as a database.
Python3 and Flask were required as part of this assignment. I had originally chosen to work with [CouchDB](http://couchdb.apache.org/) but I found the online resources weren't as helpful as SQLite online resources. SQLite appeared to be easier to set up, both for developer and application user, so I made the decision to switch before going any further with the project. I'm also well-versed in basic SQL commands, which helped a lot.

Libraries Used:

1. jQuery
2. Tether
3. BootStrap


## Learning Curve

I had never worked with Python to this extent before and I feel that it was my biggest challenge going into this project. However, I eventually got used to the lack of semicolons and am now relatively comfortable with the language. 

Using SQLite for this project reinforced material previously learned in other modules, such as setting up connections to a database in Java or Python. I now better understand how connections work, and how to query a database from a java/python file.

I was also not very confident using Git on the command line, but now I can clone repositories and commit individual files without having to reference any guides.
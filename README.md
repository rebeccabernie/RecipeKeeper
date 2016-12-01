# RecipeKeeper
###### Data Representation and Querying Project 2016
This is a  project for 3rd Year module Data Representation and Querying.

## Project Background 
This is a Single Page Web App that allows the user to save recipe details to a database. 
My two initial ideas were 

1. A Scrabble Scoring system
2. A Recipe database

Initially I decided on the Scrabble option but after a few hours of coding it had proved to be more of a challenge than I had antipcated. After some thought and another read of the project instructions, I decided that a recipe database would actually be more suitable and possibly easier to complete in the timeframe. 
As an avid baker, this option was also more relevant to me personally. I find one of my biggest problems is writing recipes on bits of paper and subsequently losing the bits - this is a simple app that would solve this problem.


## Downloading and First Run
In order to run this application, you will need [Python 3](https://www.continuum.io/downloads) installed with the Flask library. Both must be installed to run the project. The SQLite3 package must also be installed.

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
$ python recipekeeper.py        // this runs the app locally 
```

Once the file is running in CL/Terminal, open up a browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Architecture

This web application runs in Python 3 using the Flask framework and SQLite3 as a database.
Python3 and Flask were required as part of this assignment. I had originally chosen to work with [CouchDB](http://couchdb.apache.org/) but I found the online resources weren't as helpful as SQLite resources. SQLite appeared to be easier to set up, both for developer and app user, so I made the decision to switch before going any further with the project. I'm also well-versed in basic SQL commands, which helped a lot.

## Learning Curve

I had never worked with Python to this extent before and I feel that it was my biggest challenge going into this project. However, I eventually got used to the lack of semicolons and am now relatively comfortable with the language. 
Using SQLite for this project also reinforced material previously learned in other modules, such as setting up connections to a database in Java or Python.
I was also not very confident using Git on the command line, but now I can clone repositories and commit individual files without having to reference any guides.
# RecipeKeeper
###### Data Representation and Querying Project 2016
This is a project for 3rd Year module Data Representation and Querying.

## Project Background 
This is a Single Page Web App that allows the user to save recipe details to a database. 
My two initial ideas were 
*A Scrabble scoring system 
and 
* A recipe database
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
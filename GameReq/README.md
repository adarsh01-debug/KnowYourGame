# Introduction

* This project fetches you data for minimum requirements needed for a PC to run a certain game.
* You can just type the name of the game you are looking for in the search-bar and if the database contains it then it will fetch and display all the minimum requirement assets to run it, eg., RAM, CPU, GPU, HDD space and OS, along with cover and name of the game you searched.
* The API call is made in frontend JavaScript file. The creation and execution of the app is done using Django Restframework. You can find the JS file in ./static/ folder.
* The database is maintained by Django ORM which is created using Django Restframework.
* The RESTful API created is used to store datasets for different games and allows user to fetch it through a GET request.

## How To View

* Clone the project into your local host. You can either use GitBash to do the same or simply download the zip file.
* Activate the virtual environment in the parent directory of the project.
* Change the directory to ./GameReq
* Run the django server to view the website.

## How To Contribute To Database

* Create a super-user to access the admin sites.
* To open the API view page, simply use the URI: localhost:port/viewsets/requirements/
* Add the details of the game you want, make sure to confirm that the game doesn't already exists.
* To add the cover for the game, use pixels: 255x383.
* To resize your cover you can use [reduceimages](https://www.reduceimages.com/)

### PS

This project was made within 24 hours so any suggestions will be welcomed. There might be one or two bugs but I'll work to remove them. I'll also try to update the database daily with data for new games to look up to.

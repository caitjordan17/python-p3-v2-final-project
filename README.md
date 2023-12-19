# Restaurant Finder Python Application

## About

Restaurant Finder is a python Command Line Interface application that is designed to help you find restaurants you love in the cities you love. We have the ability to build a database of cities you have visited and loved. From there you can add or delete restaurants in those cities that you loved. So whenever you are in that city next you can look up your current favorite restaurants!

---

## Capabilities

From the main menu you can see the cities or exit the application.
From the city menu you can:
 - see a list of all the cities you saved
 - add a city you visited and loved
 - remove a city you don't want to see anymore
 - look at the restaurants in the city
 - go back to the main menu
 - exit the application
If you select the last one, you'll be directed to the city details menu where you can:
 - view a list of the restaurants you saved to that city
 - add a restaurant to the current city
 - remove a restaurant from the current city
 - go back to the main menu
 - exit the application


## Setup

This wonderful application does need Python, sqlite, and pipenv installed on your computer. If you've got that, great! Go ahead & fork and clone this repository and open it up in VS Code. You'll then want to set up your virtual environment by running the following in your terminal:
```bash
pipenv install
pipenv shell
```
And run:
```bash
python lib/seed.py
python lib/cli.py
```
Enjoy!


# AngleHealthProject #

The following doc contains instructions on how to run the application using Docker and lists available endpoints. The application is run using Flask and utilizes sqlite3 for its database.

## Running the Application ##

Firstly, the user must clone this repository and run ```docker build --tag commerce-app:latest .``` in the main directory. Once the build is finished, then use ```docker run -d -p 80:80 commerce-app``` to run the application. The URL **hhtp://0.0.0.0:80/** is used to access the endpoints. 

NOTE: Ideally the application would not run on 0.0.0.0, since it represents an unknown target, but it works for the purpose of running and accessing the application.

NOTE 2: The database is restarted every time the application is ran, which is not okay in a production setting, but was needed to show consistent performance during testing.

## Endpoints ##
- ```http://0.0.0.0:80/post``` is used to insert items into the app's database. The input should look like this: 
  ```{
    "posts": [
      {
        "name": "abc",
        "price": 10000,
        "start_date": "01/01/2021"
      },
      {
        "name": "abd",
        "price": 20000,
        "start_date": "01/01/2021"
      }
    ]
  } 
- ```http://0.0.0.0:80/search?keyword=<keyword>&min_price=<min_price>&max_price=<max_price>``` is used to search for items based on a keyword, and optionally a minimum price and a maximum price. Min price and max price can be left out of the URL or set to 0, which will run the search without those parameteres, but a keyword is required and cannot be empty. 
- ```http://0.0.0.0:80/all-items``` is used to retrieve all items in the database. 

## Database CLI ##
A CLI is also included to easily create, delete, and restart the application's sqlite3 database. The following commands can be run:
  - ```python dbCLI.py create``` will create the database if it does not already exist.
  - ```python dbCLI.py delete``` will delete the database if it exists.
  - ```python dbCLI.py restart``` will delete the database then create it again. If the database doesn't already exist, this command will still create it.
  
## Unit Test ##
A unit test that ensures that the application is properly handling requests is included in the project under ```test.py```. The application must be running locally and not through a Docker container in order to properly run the test.
1. Open /env directory in your command line and run ```source Scripts/activate``` in order to activate the virtual environment.
2. Run ```export FLASK_APP=CommerceApp```.
3. Run ```python -m flask run``` to start the server locally.
4. Run ```python test.py``` to run the unit test.

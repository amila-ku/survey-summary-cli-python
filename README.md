# Survey Data Analyzer

This is a CLI application to parse and display survey data from CSV files, and display a summary of results.


## Prerequisites

### Application 
* [docker](https://www.docker.com/)


### Python dependencies
* pip install nose
* pip install pandas

### Running the application
Application can be run by simply suing the docker compose

    docker-compose build
    docker-compose run project <command line arguments>

### Manually Executing the python

    python survey -d survey-1.csv -r survey-1-responses.csv

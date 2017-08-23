# Survey Data Analyzer

This is a CLI application to parse and display survey data from CSV files, and display a summary of results.


## Prerequisites

### Application 
* [docker](https://www.docker.com/)

    curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

### Python dependencies
* pip install nose
* pip install pandas

### Running the application
Application can be run by simply suing the docker compose

    docker-compose build
    docker-compose run project <command line arguments>

    docker-compose run survey -d data/survey-1.csv -r data/survey-1-responses.csv

### Manually Executing the python

    python survey -d data/survey-1.csv -r data/survey-1-responses.csv

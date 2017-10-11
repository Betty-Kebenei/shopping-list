https://s-list.herokuapp.com/

[![Build Status](https://travis-ci.org/Betty-Kebenei/shopping-list.svg?branch=master)](https://travis-ci.org/Betty-Kebenei/shopping-list)
[![Coverage Status](https://coveralls.io/repos/github/Betty-Kebenei/shopping-list/badge.svg?branch=master)](https://coveralls.io/github/Betty-Kebenei/shopping-list?branch=master)
[![Test Coverage](https://codeclimate.com/github/codeclimate/codeclimate/badges/coverage.svg)](https://codeclimate.com/github/codeclimate/codeclimate/coverage)
[![Issue Count](https://codeclimate.com/github/codeclimate/codeclimate/badges/issue_count.svg)](https://codeclimate.com/github/codeclimate/codeclimate)

# Shopping-list Application

This is a shopping list app that allows users to record and share things they want to spend money on. 
This application meets the needs of keeping track of their shopping lists.

The features of the application.
  -Users can create accounts 
  -Users can log in. 
  -Users can create, view, update and delete shopping lists. 
  -Users can add, update, view or delete items in a shopping list
  
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Deployment notes on how to deploy the project on a live system will follow later.

### Prerequisites

Python version 2.7+.
Virtualenv
A decent web browser.

If virtualenv is not installed:
First download get-pip.py, 
Navigate to the directory where the file was downloaded,
Then run the following on the commandpromt as administrator:

  >python get-pip.py
  >pip install virtualenv
After this you don't need to run the commandpromt as administrator:

Create a virtualenv by running

  >virtualenv envname

Activate the virtualenv by running this command
  >pymote_env\Scripts\activate

### Installing
Navigate to the directory containing the project.

Clone the repo by running  

  >git clone https://github.com/Betty-Kebenei/shopping-list 

## Testing the application
Navigate to the root of the application

Install the requirements by running

  >pip install -r requirements.txt

Run the application by

  >python run.py

Access the app on the browser using http://127.0.0.1:5000

## Running Test Cases
In the same directory run 

  >python tests.py
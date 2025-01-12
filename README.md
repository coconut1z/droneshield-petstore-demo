# Swagger Pet store API test
Part 2 of the Droneshield QA tech assessment.

## Description
This project uses Python, Selenium, and Requests to perform automated API testing of [Swagger Petstore](https://petstore.swagger.io/).

## Installation
Assuming Python is already installed:
1. Clone the repository
2. Navigate to the project directory
```bash
cd sauce_demo
```
3. Install dependencies
```bash
pip install pytest selenium requests
```

## Usage
To run all the tests, use:
```bash
pytest tests/test_sauce_demo.py -v
```
The "-v" command line option will show verbose output; it'll show the name of each test and is more readable.
To run a specific set of tests, "-m" and a marker can be used. Markers are:
- pet
- store
- user
- negative

This example will run just the pet tests:
```bash
pytest tests/test_sauce_demo.py -v -m pet
```

Or run just the store and user tests:
```bash
pytest tests/test_sauce_demo.py -v -m "store or user"
```

Or run just the negative pet scenarios:
```bash
pytest tests/test_sauce_demo.py -v -m "pet and negative"
```
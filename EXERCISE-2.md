# Swagger Petstore API testing - Exercise 2
Test strategy, test plan, and decisions and reasons components of part 2 of the Droneshield QA tech assessment.

## Test Strategy
### 1. Test Objectives
- API Testing: Ensuring the Petstore API is working as expected per its requirements ranging from:
    - Proper responses to valid and invalid requests
    - Correctness of data
    - Performance and load handling

### 2. Test Scope
In-Scope:
- All RESTful endpoints:
    - Pet management
    - Store management
    - User management

### 3. Test Types
- Functional Testing: Ensure API behaves correctly according to requirements such as responding with the appropriate status codes.
- Negative Testing: Test the system handles invalid inputs gracefully and returns the correct error codes.

### 4. Test Levels
- Unit Testing: Performing unit tests for individual API calls.
- End to end Testing: Testing the complete flow of the API.

### 5. Test Approach
Automated Testing: Automated scripts using Selenium, Pytest, and Requests to test the API calls.

### 6. Test Environment
- Browsers: Google Chrome
- Devices: Desktop
- Operating Systems: Windows 11
- Test Tools:
    - Selenium
    - Pytest
    - Requests
- API Documentation: Can refer to [Petore Documentation](https://petstore.swagger.io/)

## 7. Defect Management
- Defect Reporting: Bugs will be tracked using Jira or a similar tool. Each defect will be assigned a severity (Critical, Major, Minor) and priority (High, Medium, Low).
- Defect Resolution: The development team will prioritize fixing defects based on severity and impact on user experience.
- Re-testing: Once a defect is fixed, it will be re-tested to ensure it has been resolved and no other issues have been introduced.

## Test Plan
### 1. Test Plan Details
- Test Plan ID: SPS-001
- Version: 1.0
- Date: 11/01/25

### 2. Introduction
- Purpose: The purpose of this test plan is to define the testing strategy, scope, and resources for the RESTful API testing activities related to the Swagger Petstore.
- Application Overview: Swagger Petstore is a demo RESTful API that simulates a pet store.
- Scope: The scope of this test plan includes functional testing and negative testing of the RESTful API using requests such as GET, POST, etc.

### 3. Test Items
The following components will be tested:
- Pet: Endpoints related to adding, editing, searching, and removing pets.
- Store: Endpoints related to getting a list of pets, adding a pet orders, finding orders, and deleting orders.
- User: Endpoints related to user login, creation, updates, and deletion.

### 4. Features to be Tested
- Login Functionality: Valid login and invalid login.
- Product Search and Sorting: Ability to browse, filter, and view products.
- Cart Operations: Adding/removing items, checking item quantities, and verifying cart total.
- Checkout Process: Ensuring that users can complete the order with valid (mock) payment information.
- UI/UX: Verify that UI elements like buttons, links, and forms work correctly.

### 5. Test Approach
Test Types:
- Functional Testing: Verify functionality of endpoints for Pet, Store, and User.
- Negative Testing: Verify handling and reponses to invalid data input.

Test Environment: Testing will be performed in:
- Browsers: Google Chrome
- Operating Systems: Windows 11

Automation Framework: Selenium will be used for automating browser interactions. Pytest will be used for test execution and reporting. Requests will be used for handling RESTful API components.

### 6. Test Criteria
Entry Criteria
- All development tasks are completed, the API endpoints are available and ready for testing.
- The test environment is set up, and the necessary tools are configured.

Exit Criteria
- All test cases have been executed, and the critical defects have been fixed.
- The application passes all functional and usability tests.
- No open critical or major severity defects are remaining.

### 7. Defect Management
Defects will be logged in BUGREPORT-2.md.

Defects will be categorized based on severity:
- Critical: Application crashes, major functionality broken.
- Major: Significant feature not working, high impact on usability.
- Minor: Cosmetic issues, minor bugs with low impact.

Defects will have a priority ranging from High, Medium, and Low.

## Decisions and Reasons
- Python was selected as the language as it is what DroneShield uses. It also allows me a chance to learn a new language on the go.
- Selenium was selected as the web automation tool as I am familiar with it and it can also be written in Python. It provides a simple way to interact with UI elements on web browsers.
- Pytest was selected as the testing framework as it is used for writing and executing test cases, and providing reporting if needed. It works in conjuction with Selenium and can be easily installed through Python/pip.
- Requests is a Python module for making HTTP requests and can be used for API testing without the need of additional programs like Postman.
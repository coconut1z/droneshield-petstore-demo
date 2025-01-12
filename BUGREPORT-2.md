# Swagger Petstore API testing - Bug report 2
Bug report component of part 2 of the Droneshield QA tech assessment.

## Bugs
### Received 500 status from expected 405 status for adding a new pet POST request
- ID: SPS-001
- Description: Response different from expected for adding a new pet with invalid data.
- Steps to reproduce:
    1. Edit payload so that id, such as under tags, is a string
    2. Send the post request with payload with invalid data
- Expected result: 405 response for payload with invalid input is expected.
- Actual result: Receiving a 500 response for payload with invalid input.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 404 status from 400 status for trying to delete a pet DELETE request
- ID: SPS-002
- Description: Response different from expected for attempting to delete a pet by providing invalid data.
- Steps to reproduce:
    1. Edit payload so that id is a string
    2. Send the delete request with payload with invalid data
- Expected result: 400 response for invalid ID supplied.
- Actual result: Receiving a 404 response for payload with invalid input.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 404 status from expected 400 status for fetching pet by id GET request
- ID: SPS-003
- Description: Response different from expected for attempting to fetch a pet by providing invalid id data.
- Steps to reproduce:
    1. Edit endpoint so that the provided id is a string
    2. Send the get request to this endpoint
- Expected result: 400 response for invalid ID supplied.
- Actual result: Receiving a 404 response for endpoint with invalid input.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 200 status from expected 400 status for fetching pet by status GET request
- ID: SPS-004
- Description: Response different from expected for attempting to fetch a pet by providing an invalid status value.
- Steps to reproduce:
    1. Edit parameter so that it is invalid, such as 1234 which is not listed as an available status
    2. Send the get request to this endpoint with the parameter
- Expected result: 400 response for invalid ID supplied.
- Actual result: Receiving a 200 response for endpoint with invalid status value.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 500 status from expected 400 status for updating a pet PUT request
- ID: SPS-005
- Description: Response different from expected for updating a pet with invalid data.
- Steps to reproduce:
    1. Edit payload so that the ids are strings
    2. Send the post request with payload with invalid data
- Expected result: 400 response for payload with invalid id expected.
- Actual result: Receiving a 500 response for payload with invalid input.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 500 status from expected 400 status for placing a store order POST request
- ID: SPS-006
- Description: Response different from expected for placing a store order with invalid data.
- Steps to reproduce:
    1. Edit payload so that the ids is a string
    2. Send the post request with payload with invalid data
- Expected result: 400 response for payload with invalid id expected.
- Actual result: Receiving a 500 response for payload with invalid input.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 404 status from expected 400 status for fetching a store order GET request
- ID: SPS-007
- Description: Response different from expected for fetching a store order with invalid id data.
- Steps to reproduce:
    1. Edit payload so that the id not a value that is >= 1 and <= 10, such as 100
    2. Send the post request with payload with the invalid endpoint
- Expected result: 400 response for endpoint with invalid id value expected.
- Actual result: Receiving a 404 response for endpoint with invalid id value.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 404 status from expected 400 status for deleting a store order GET request
- ID: SPS-008
- Description: Response different from expected for deleting a store order with invalid id data.
- Steps to reproduce:
    1. Edit payload so that the id not a value that is >= 1 and <= 10, such as a string
    2. Send the post request with payload with the invalid endpoint
- Expected result: 400 response for endpoint with invalid id value expected.
- Actual result: Receiving a 404 response for endpoint with invalid id value.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Able to create user without being logged in POST request
- ID: SPS-009
- Description: You are able to create a user without being logged in.
- Steps to reproduce:
    1. Create payload with valid user object data
    2. Send the post request with payload
- Expected result: Should not be able to create a new user.
- Actual result: Receiving a 200 response and user is successfully created.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Able to create user without any payload data POST request
- ID: SPS-010
- Description: You are able to create a user without any payload data.
- Steps to reproduce:
    1. Send the post request with an empty payload
- Expected result: Should not be able to create a new user.
- Actual result: Receiving a 200 response and user is successfully created.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Able to update a user without a username that doesn't exist PUT request
- ID: SPS-011
- Description: You are able to use an invalid username and make a successful update.
- Steps to reproduce:
    1. Edit endpoint with a username that doesn't exist, such as 123asdf1234!@#
    2. Send the put request with the invalid endpoint.
- Expected result: 404 response for providing endpoint for user that doesn't exist.
- Actual result: Receiving a 200 response and user is successfully updated.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Able to login with a user that doesn't exist GET request
- ID: SPS-012
- Description: You are able to use an invalid username and password to login successfully.
- Steps to reproduce:
    1. Provide invalid parameter details for username and password, such as invaliduser and fakepassword
    2. Send the get request with the invalid parameters.
- Expected result: 400 response for providing invalid login details.
- Actual result: Receiving a 200 response and user is successfully logged in.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Received 405 status from expected 404 status for deleting a non-existent user DELETE request
- ID: SPS-013
- Description: When you provide no username to delete you receive a 405 status instead of 404.
- Steps to reproduce:
    1. Don't provide any username for the endpoint.
    2. Send the delete request with the endpoint with no username.
- Expected result: 404 response for user not found.
- Actual result: Receiving a 405 response.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome
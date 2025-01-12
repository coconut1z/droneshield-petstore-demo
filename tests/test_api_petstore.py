import pytest
from utils.api_utils import get_request, post_request, put_request, delete_request

# Test to add a new pet to the store (POST request)
@pytest.mark.pet
def test_post_add_new_pet():
    endpoint = "pet"
    # Can clean up the tests by using a separate json file for the payloads, a potential enhancement
    payload = {
        "id": 3010,
        "category": {
            "id": 3010,
            "name": "dog"
        },
        "name": "Puppy",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 3010,
                "name": "unknown"
            }
        ],
        "status": "special-test-status"
    }
    response = post_request(endpoint, json=payload)
    response_json = response.json()
    # Certain values hard coded since there is only one pet being added
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['name'] == "Puppy", f"Expected Puppy but got {response_json['name']}"
    assert response_json['status'] == "special-test-status", f"Expected special-test-status but got {response_json['status']}"
    

# Negative test to try adding a new pet to the store with invalid data
@pytest.mark.pet
@pytest.mark.negative
def test_post_negative_add_new_pet():
    endpoint = "pet"
    payload = {
        "id": 1234,
        "category": {
            "id": 1234,
            "name": "dog"
        },
        "name": "Puppy",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": "theid",
                "name": "unknown"
            }
        ],
        "status": "1234"
    }
    response = post_request(endpoint, json=payload)
    assert response.status_code == 405, f"Expected status 405 but got {response.status_code}"


# Test to fetch a pet by its ID (GET request)
@pytest.mark.pet
def test_get_find_pet_by_id():
    pet_id = 3010  # Pet ID created above
    endpoint = f"pet/{pet_id}"
    response = get_request(endpoint)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert "id" in response.json(), "Response JSON does not contain pet ID"
    assert response.json()['id'] == pet_id, f"Expected pet ID {pet_id} but got {response.json()['id']}"
    
    
# Negative test to fetch a pet with an invalid ID (GET request)
@pytest.mark.pet
@pytest.mark.negative
def test_get_negative_find_pet_by_id():
    pet_id = "eight"
    endpoint = f"pet/{pet_id}"
    response = get_request(endpoint)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"


# Test to fetch a pet by its status (GET request)
@pytest.mark.pet
def test_get_find_pet_by_status():
    status = "special-test-status"    
    endpoint = "pet/findByStatus"
    params = { 'status': status }
    response = get_request(endpoint, params=params)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    # This reponse returns a list of objects, using the lazy way of just getting the first one by ensuring to have used a unique status, ideally don't do this
    assert "status" in response.json()[0], "Response JSON does not contain pet status"
    assert response.json()[0]['status'] == status, f"Expected {status} but got {response.json()['status']}"
    
    
# Negative test to fetch a pet with an invalid status (GET request)
@pytest.mark.pet
@pytest.mark.negative
def test_get_negative_find_pet_by_status():
    status = 1234
    endpoint = "pet/findByStatus"
    params = { 'status': status }
    response = get_request(endpoint, params=params)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"
    

# Test to update an existing pet (PUT request)
@pytest.mark.pet
def test_put_update_pet():
    pet_id = 3010
    endpoint = "pet"
    updated_payload = {
        "id": pet_id,
        "name": "Beany",
        "category": {
            "id": pet_id,
            "name": "golden retriever"
        },
        "photoUrls": ["string"],
        "tags": [{"id": pet_id, "name": "playful"}],
        "status": "adopted"
    }
    response = put_request(endpoint, json=updated_payload)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"    
    assert response_json['name'] == "Beany", f"Expected updated name to be Beany but got {response_json['name']}"
    assert response_json['status'] == "adopted", f"Expected updated status to be adopted but got {response_json['status']}"
    

# Negative test to update an existing pet with invalid data (PUT request)
@pytest.mark.pet
@pytest.mark.negative
def test_put_negative_update_pet():
    pet_id = "newpetid"
    endpoint = "pet"
    updated_payload = {
        "id": pet_id,
        "name": "Beany",
        "category": {
            "id": pet_id,
            "name": "golden retriever"
        },
        "photoUrls": ["string"],
        "tags": [{"id": pet_id, "name": "playful"}],
        "status": "adopted"
    }
    response = put_request(endpoint, json=updated_payload)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"    


# Test to delete a pet (DELETE request)
@pytest.mark.pet
def test_delete_pet():
    pet_id = 3010
    endpoint = f"pet/{pet_id}"
    response = delete_request(endpoint)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Verify the pet is deleted by trying to fetch it
    response = get_request(endpoint)
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
    
    
# Negative test to delete a pet with invalid data (DELETE request)
@pytest.mark.pet
@pytest.mark.negative
def test_delete_negative_pet():
    pet_id = "!@#!@#!@#!@"
    endpoint = f"pet/{pet_id}"
    response = delete_request(endpoint)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"


# Test to fetch the store inventory (GET request)
@pytest.mark.store
def test_get_store_inventory():
    endpoint = "store/inventory"
    response = get_request(endpoint)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert "sold" in response_json
    assert "available" in response_json
    

# Test to add a new order to the store (POST request)
@pytest.mark.store
def test_post_store_order():
    endpoint = "store/order"
    payload = {
        "id": 8,
        "petId": 3010,
        "quantity": 1,
        "shipDate": "2025-01-12T00:34:01.928Z",
        "status": "placed",
        "complete": "true"
    }
    response = post_request(endpoint, json=payload)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['id'] == 8, f"Expected 8 but got {response_json['id']}"
    assert response_json['status'] == "placed", f"Expected placed but got {response_json['status']}"
    
    
# Negative test to add a new order to the store with an invalid id (POST request)
@pytest.mark.store
@pytest.mark.negative
def test_post_negative_store_order():
    endpoint = "store/order"
    payload = {
        "id": "fakeid",
        "petId": 1,
        "quantity": 1,
        "shipDate": "2025-01-12T00:34:01.928Z",
        "status": "placed",
        "complete": "true"
    }
    response = post_request(endpoint, json=payload)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"
    

# Test to fetch an order by id from the store (GET request)
@pytest.mark.store
def test_get_store_order_by_id():    
    order_id = "8"
    endpoint = f"store/order/{order_id}"
    response = get_request(endpoint)    
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['id'] == 8, f"Expected 8 but got {response_json['id']}"
    assert response_json['status'] == "placed", f"Expected placed but got {response_json['status']}"
    

# Negative test to fetch an order by id from the store with an invalid id (GET request)
@pytest.mark.store
@pytest.mark.negative
def test_get_negative_store_order_by_id():    
    order_id = "-100"
    endpoint = f"store/order/{order_id}"
    response = get_request(endpoint)    
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"
    

# Test to delete a store order (DELETE request)
@pytest.mark.store
def test_delete_store_order_by_id():
    order_id = "8"
    endpoint = f"store/order/{order_id}"
    response = delete_request(endpoint)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Verify the order is deleted by trying to fetch it
    response = get_request(endpoint)
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
    

# Negative test to delete a store order with invalid order id (DELETE request)
@pytest.mark.store
@pytest.mark.negative
def test_delete_negative_store_order_by_id():
    order_id = "eleven"
    endpoint = f"store/order/{order_id}"
    response = delete_request(endpoint)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"
    
    # Verify the order is deleted by trying to fetch it
    response = get_request(endpoint)
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
    

# Test to create a new user (POST request)
@pytest.mark.user
def test_post_user_creation():
    endpoint = "user"
    payload = {
        "id": 2801,
        "username": "usernameconant",
        "firstName": "Conant",
        "lastName": "Feng",
        "email": "email@email.com",
        "password": "password1",
        "phone": "0412345678",
        "userStatus": 0
    }
    response = post_request(endpoint, json=payload)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['message'] == "2801", f"Expected 2801 but got {response_json['message']}"
    
    
# Negative test to create a new user with no data (POST request)
@pytest.mark.user
@pytest.mark.negative
def test_post_negative_user_creation():
    endpoint = "user"
    payload = {}
    response = post_request(endpoint, json=payload)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['message'] == "", f"Expected '' but got {response_json['message']}"


# Test to fetch a user by username (GET request)
@pytest.mark.user
def test_get_user_by_username():
    username = "usernameconant"
    endpoint = f"user/{username}"
    response = get_request(endpoint)    
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['id'] == 2801, f"Expected 2801 but got {response_json['id']}"
    assert response_json['username'] == username, f"Expected {username} but got {response_json['status']}"
    
    
# Negative test to fetch a user by invalid username (GET request)
@pytest.mark.user
@pytest.mark.negative
def test_get_negative_user_by_username():
    username = 123451234
    endpoint = f"user/{username}"
    response = get_request(endpoint)    
    response_json = response.json()
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
    assert response_json['message'] == "User not found", f"Expected User not found but got {response_json['message']}"


# Test to update a user's details (PUT request)
@pytest.mark.user
def test_put_update_user():
    username = "usernameconant"
    endpoint = f"user/{username}"
    updated_payload = {
        "id": 2801,
        "username": "usernameconant",
        "firstName": "Drone",
        "lastName": "Shield",
        "email": "email@email.com",
        "password": "password1",
        "phone": "0412345678",
        "userStatus": 0
    }
    response = put_request(endpoint, json=updated_payload)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    
    # Test the update was successful by getting the user and checking the updated values
    response = get_request(endpoint)
    response_json = response.json()
    assert response_json['firstName'] == "Drone", f"Expected Drone but got {response_json['firstName']}"
    assert response_json['lastName'] == "Shield", f"Expected Shield but got {response_json['lastName']}"
    

# Negative test to update a user's details by providing username that doesn't exist (PUT request)
@pytest.mark.user
@pytest.mark.negative
def test_put_negative_update_user():
    username = "123asdf1234!@#"
    endpoint = f"user/{username}"
    updated_payload = {
        "id": 4312,
        "username": "fakeusername",
        "firstName": "Drone",
        "lastName": "Shield",
        "email": "email@email.com",
        "password": "password1",
        "phone": "0412345678",
        "userStatus": 0
    }
    response = put_request(endpoint, json=updated_payload)
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"


# Test to login with a user (GET request)
@pytest.mark.user
def test_get_user_login():
    username = "usernameconant"
    password = "password1"
    endpoint = "user/login"
    params = { 'username': username,
               'password': password
               }
    response = get_request(endpoint, params=params)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert "logged in user session" in response_json['message'], f"Expected logged in user session but got {response_json['message']}"
    

# Negative test to login with invalid user details (GET request)
@pytest.mark.user
@pytest.mark.negative
def test_get_negative_user_login():
    username = "invaliduser"
    password = "fakepassword"
    endpoint = "user/login"
    params = { 'username': username,
               'password': password
               }
    response = get_request(endpoint, params=params)
    assert response.status_code == 400, f"Expected status 400 but got {response.status_code}"


# Test to logout with a user (GET request)
@pytest.mark.user
def test_get_user_logout():
    endpoint = "user/logout"
    response = get_request(endpoint)
    response_json = response.json()
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response_json['message'] == "ok", f"Expected ok but got {response_json['message']}"


# Test to delete a user (DELETE request)
@pytest.mark.user
def test_delete_user():
    username = "usernameconant"
    endpoint = f"user/{username}"
    response = delete_request(endpoint)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Verify the user is deleted by trying to fetch it
    response = get_request(endpoint)
    response_json = response.json()
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
    assert response_json['message'] == "User not found", f"Expected User not found but got {response_json['message']}"
    

# Negative test to delete a non-existent user (DELETE request)
@pytest.mark.user
@pytest.mark.negative
def test_delete_negative_user():
    username = ""
    endpoint = f"user/{username}"
    response = delete_request(endpoint)
    assert response.status_code == 404, f"Expected status 404 but got {response.status_code}"
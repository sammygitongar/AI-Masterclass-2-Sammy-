import requests
url ="https://jsonplaceholder.typicode.com"

response = requests.get(f"{url}/users")

data = response.json()


print("Response status code:", response.status_code)
print("Here are some user dummy data to be used for testing purposes:")
for user in data:
    print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
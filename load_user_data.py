import json

# Function to load the data
def load_data(filename):
    with open (filename , "r") as f:
        data = json.load(f)
    return data

data = load_data("data.json")
# print(data)


# writing a funtion to display users and their connections
def display_users(data):
    print("users and their connections\n")
    for user in data['users']:
        print(f"{user['name']} id is {user['id']} and friends are {user['friends']} and liked pages are {user['liked_pages']} ")

    print("\nPages information is \n")
    for page in data['pages']:
        print(f"id of {page['name']} is {page['id']}")

display_users(data)




import json

def clean_data(filename):
    # remove users with missing values
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    # Remove duplicate friends
    for user in data["users"]:
        user["friends"]=list(set(user["friends"]))
        
    # Remove in active users
    data["users"]=[user for user in data['users'] if user['friends'] or user['liked_pages']]

    # removing Duplicate pages
    unique_pages ={}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages']=list(unique_pages.values())

def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data

data = load_data("data2.json")
clean_data = clean_data(data)

json.dump(data,open("cleaned_data.json","w") , indent=4)
print("data has been cleanded successfully")
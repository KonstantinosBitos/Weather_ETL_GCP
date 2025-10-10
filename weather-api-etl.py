import requests

# Define the API endpoint
api_endpoint = "https://jsonplaceholder.typicode.com/posts"

# Make the GET request
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the response data
    for post in data:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    # Print an error message if the request failed
    print(f"Error: {response.status_code}")
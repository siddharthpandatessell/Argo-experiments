import requests
response = requests.get('www.google.com')
print(response.status_code)

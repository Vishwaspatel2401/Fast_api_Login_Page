import requests

url = "http://127.0.0.1:8000/login"

payload = {
    "username": "nick",
    "password": "BrpOzAixblWhDrEYxvJs4u3OMwf0QY2TiFLnNhLRcxqL2YpcM31mK"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())

"""
Using Trivia Database: Generate API Url
    https://opentdb.com/api.php?amount=10&type=boolean
"""
import requests

URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 12,
    "type": "boolean"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]








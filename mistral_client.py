import requests
import json
import os

#sends post request to Mistral API
#Input: API address and audio transcription
#returns audio transcription and LLM response

def mistral(server_url, prompt):
    data = {
        "Content-Type": "application/json",
        "messages": [
            {
            "role": "user",
            "content":prompt
            }
        ],
        "mode": "chat",
        "character": "Example"
        }

    # Sending a POST request to the API
    response = requests.post(server_url, json=data)

    if response.status_code == 200:
        response_data = response.json()
        content = response_data['choices'][0]['message']['content']


    else:
        print("Error:", response.status_code, response.text)

    return content

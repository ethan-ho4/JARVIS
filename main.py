from mistral_client import mistral

prompt= "what is the capital of china"
mistral_server_url = "http://127.0.0.1:5000/v1/chat/completions"

mistral_response = mistral(mistral_server_url, prompt)
print(mistral_response)



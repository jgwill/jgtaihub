import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import requests

class API:
    def __init__(self, api_key=None):
        if api_key:
            self.api_key = api_key
        else:
            self.load_api_key_from_env()


    def generate_response(self, question,model_name='gpt-3.5-turbo',max_tokens=1024):
        # Define the URL for the OpenAI Chat API
        #https://api.openai.com/v1/
        url = 'https://api.openai.com/v1/chat/completions'

        # Define the headers for the API request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        # Define the data for the API request
        data = {
            'messages': [{'role': 'user', 'content': question}],
            'model': model_name,
            'max_tokens': max_tokens
        }

        # Send the API request and get the response
        response = requests.post(url, headers=headers, json=data)
        my_text_response_as_json = response.json()
        print(response.json())
        # Return the response
        return response

    def send_request(self, question):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': question}
            ]
        }
        response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
        return response.json()
    

    def load_api_key_from_env(self):
        # Define possible locations for .env
        env_locations = [Path('.'), Path('..'), Path.home()]

        # Try to load .env from each location
        for loc in env_locations:
            env_path = loc / '.env'
            if env_path.exists():
                load_dotenv(dotenv_path=env_path)
                break

        # Get API key from environment variables
        self.api_key = os.getenv(
            'OPENAI_API_KEY__our_prototypes_240117',
            os.getenv('OPENAI_API_KEY'))
        #print(self.api_key)
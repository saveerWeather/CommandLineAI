from openai import OpenAI
import json
import os
#Custom BotHandler class to handle creating custom prompted GPT bots. Will implement custom override function intended for message generation.
class BotHandler:
    def __init__(self):
        self.api_key = self._load_api_key()
        self.client = OpenAI(api_key=self.api_key)
    def _load_api_key(self):
        api_key_path = os.path.join(os.path.dirname(__file__), '../config/api_key.json')
        try:
            with open(api_key_path, 'r') as f:
                data = json.load(f)
                api_key = data['api_key']
        except FileNotFoundError:
            raise FileNotFoundError(f"API key file not found at {api_key_path}. Please ensure it exists.")
        except KeyError:
            raise KeyError("API key file is missing the 'api_key' key. Please check the file format.")
        return api_key
    def create_bot(self,prompt,model="gpt-4", max_tokens=750,temperature=0.7):
        return _Bot(self.client,prompt,model,max_tokens,temperature)

class _Bot:
    def __init__(self,client,prompt,model="gpt-4", max_tokens=750,temperature=0.7):
        self.prompt = prompt
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = client

    def promptgpt(self,messages):
        response = self.client.chat.completions.create(
        messages=messages,
        model=self.model,
        max_tokens=self.max_tokens,
        temperature=self.temperature
        )
        return (response.choices[0].message.content)
    def getmessageheader(self):
        return [{"role": "system", "content": self.prompt}]
    def simple_response(self,message):
        return self.promptgpt(self.getmessageheader()+[{"role": "user", "content": message}])
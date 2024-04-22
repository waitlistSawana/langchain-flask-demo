import os
from flask import Flask, request, jsonify

app = Flask(__name__)

base_url = os.environ.get('OPEN_AI_BASE_URL')
api_key = os.environ.get('OPEN_AI_GPT4_API_KEY')


if __name__ == '__main__':
    app.run(debug=True)
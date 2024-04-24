# app.py (Flask REST API)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LANGCHAIN_QA_URL = "http://localhost:8501"  

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    query = data.get('question')

    response = requests.post(f"{LANGCHAIN_QA_URL}/answer", json={"question": query})
    answer = response.json().get('answer')

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

    
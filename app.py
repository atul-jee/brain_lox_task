from flask import Flask, request, jsonify
from langchain_helper import get_qa_chain, create_vector_db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Codebasics Q&A 🌱"

@app.route('/create-knowledgebase', methods=['POST'])
def create_knowledgebase():
    create_vector_db()
    return jsonify({"message": "Knowledge base created successfully"}), 201

@app.route('/ask-question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "Question is required"}), 400

    chain = get_qa_chain()
    response = chain(question)
    return jsonify({"answer": response["result"]})

if __name__ == '__main__':
    app.run(debug=True)

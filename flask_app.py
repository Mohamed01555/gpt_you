from flask import Flask, request, jsonify
from gpt4 import Completion
from asyncio import run
app = Flask(__name__)


async def get_answer(question):
    resp = await Completion().create(question)
    return resp
        
@app.route('/create-completion', methods=['POST'])
def create_completion():
    try:
        prompt = request.json['prompt']
        completion = run(get_answer(prompt))
        return jsonify({"completion": completion})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

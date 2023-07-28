from flask import Flask, request, jsonify
import openai
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for the entire Flask app

# Set up your OpenAI API key
openai.api_key = ""

@app.route('/')
def index():
    return "Flask server is running! Use the /chatgpt endpoint for API calls."

@app.route('/chatgpt', methods=['POST'])
@cross_origin()
def chatgpt():
    print("Received a request to /chatgpt")  # Debugging line
    try:
        prompt = request.json.get('prompt')
        print(f"Prompt received: {prompt}")  # Debugging line
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        
        chatgpt_response = response.choices[0]["message"]["content"].strip()
        print(f"Response from ChatGPT: {chatgpt_response}")  # Debugging line
        
        return jsonify({"response": chatgpt_response})
    except Exception as e:
        print("Error in Flask server:", e)
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(port=5000, debug=True)

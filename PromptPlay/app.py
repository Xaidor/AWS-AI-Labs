from flask import Flask, render_template, request, jsonify
import boto3
import os

app = Flask(__name__)

# Placeholder for Bedrock client (you'll need your credentials set up)
# For local testing, ensure AWS credentials are in your environment or use boto3's default setup
# bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def call_bedrock(prompt):
    # Simulated LangCoach-style response for now — you'll plug in Bedrock later
    response = f"Hi there! Let's practice together. You said: '{prompt}'. Here's a quick correction and tip: [Placeholder Tip]"
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    result = call_bedrock(prompt)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)

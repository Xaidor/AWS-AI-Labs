from flask import Flask, render_template, request, jsonify
import boto3
import json
import os

load_dotenv()
aws_region = os.getenv("AWS_REGION")
print(aws_region) # For debugging, checking to see if the value read correctly
app = Flask(__name__)

# Titan-based LangCoach logic
def call_bedrock(user_input):
    #AWS has 2 seperate clients for Bedrock "bedrock" and bedrock-runtime
    bedrock = boto3.client(service_name="bedrock-runtime", region_name=aws_region)


    system_prompt = f"""
You are a French language coach with a thick Jamaican accent. The user is a beginner student trying to improve their grammar and fluency.

Instructions:
- If the user's sentence is mostly correct, praise them with fun Jamaican expressions like "Mi proud a yuh!" or "Yuh a mash up di French!"
- If they make a mistake, be sarcastic or humorous (but helpful), and provide the correction.
- Give a short grammar tip in plain English.
- End every message with a bit of encouragement or a joke.

User said: "{user_input}"

Your response:
"""
    kwarg = {
        "modelId": "amazon.titan-text-premier-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": "{\"inputText\":system_promt,\"textGenerationConfig\":{\"maxTokenCount\":300,\"stopSequences\":[],\"temperature\":0.7,\"topP\":0.9}}"
    }

    response = bedrock.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps(kwarg),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response['body'].read())
    return response_body['results'][0]['outputText']

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for processing user input and calling Bedrock
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
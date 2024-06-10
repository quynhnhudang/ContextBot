from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    context = request.json.get('context', '')
    
    # Append user input to the context
    context += user_input + " "
    
    # Tokenize and generate response
    inputs = tokenizer.encode(context, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'response': response, 'context': context})

if __name__ == '__main__':
    app.run(debug=True)

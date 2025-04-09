from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

with open('chatbot_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    user_input_vectorized = vectorizer.transform([user_input])
    response = model.predict(user_input_vectorized)[0]
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)


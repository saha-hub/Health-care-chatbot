# 🏥 Health Care Chatbot

A simple AI-powered healthcare chatbot built using Flask and a machine learning model. This chatbot processes user input and responds with relevant healthcare information or guidance, making it a useful starting point for more advanced health assistant applications.

---

## 🚀 Features

- Lightweight Flask web application
- Machine Learning model for intent recognition
- Pre-trained model using Scikit-learn
- Interactive frontend for user chat
- Easy to extend with more intents and responses

---

## 🧠 How It Works

The chatbot uses a pre-trained machine learning model and a vectorizer stored in a Pickle file (`chatbot_model.pkl`). When a user types a message:

1. The input is received by the Flask backend.
2. The input is vectorized using the trained `vectorizer`.
3. The `model` predicts the most appropriate response or intent.
4. The chatbot displays the response back to the user on the web interface.

---

## 📁 Project Structure

```
healthcare-chatbot/
│
├── app.py                  # Main Flask application
├── chatbot_model.pkl       # Pickled vectorizer and ML model
├── healthcare_dataset.json # dataset
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # CSS styling
|   └── script.js           # JS script
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 🔧 Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Flask
- scikit-learn
- Pickle (standard in Python)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-chatbot.git
cd healthcare-chatbot
```

### 2. Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install:

```bash
pip install flask scikit-learn
```

### 3. Add the Model File

Ensure `chatbot_model.pkl` (containing the trained vectorizer and model) is in the root directory.

---

## 🧪 Run the Application

Start the Flask development server:

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to chat with the bot.

---

## 💬 Usage

- Type a healthcare-related question or message.
- Get an automatic response from the chatbot based on trained data.
- Example inputs:  
  - "What are the symptoms of diabetes?"  
  - "Give me tips for a healthy diet"  
  - "What should I do for a fever?"

---


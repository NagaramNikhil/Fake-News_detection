from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news_text = data.get("news_text", "")

    if not news_text:
        return jsonify({"prediction": "Error: No input received."})

    # Simple Fake News detection logic
    if "fake" in news_text.lower():
        prediction = "This news is likely FAKE."
    else:
        prediction = "This news seems REAL."

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)

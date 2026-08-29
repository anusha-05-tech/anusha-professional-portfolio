from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return jsonify({"message": "Anusha Portfolio API is running"})

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.post("/contact")
def contact():
    data = request.get_json()
    required = ["name", "email", "message"]
    if not data or not all(data.get(key) for key in required):
        return jsonify({"error": "Name, email and message are required"}), 400
    return jsonify({"message": f"Thank you, {data['name']}! Your message was received."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

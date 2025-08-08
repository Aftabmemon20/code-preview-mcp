import os
from flask import Flask, jsonify

app = Flask(__name__)

# Root route
@app.route("/")
def home():
    return jsonify({"status": "Server is running!", "message": "MCP Server is live on Render 🚀"})

# Example MCP API endpoint
@app.route("/preview", methods=["GET"])
def preview():
    return jsonify({"preview": "Here your code preview feature will work!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render will set this automatically
    app.run(host="0.0.0.0", port=port)

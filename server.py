from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/preview", methods=["POST"])
def preview_code():
    data = request.get_json()
    code = data.get("code", "")
    return jsonify({
        "status": "success",
        "preview": code
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

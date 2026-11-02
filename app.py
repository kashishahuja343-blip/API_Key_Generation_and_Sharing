from flask import Flask, request, jsonify

app = Flask(__name__)

# Three unique API keys for three consumers
API_KEYS = {
    "ROOT-TESTER-001-ABC123",
    "ROOT-TESTER-002-XYZ456",
    "ROOT-TESTER-003-PQR789"
}

@app.route('/process', methods=['POST'])
def process_text():

    # Get API key from request header
    api_key = request.headers.get('X-API-Key')

    # Validate API key
    if api_key not in API_KEYS:
        return jsonify({
            "error": "Invalid or missing API key"
        }), 401

    # Get JSON data
    data = request.get_json(silent=True)

    if not data or not isinstance(data.get('text'), str):
        return jsonify({
            "error": "Please provide text as a JSON string"
        }), 400

    # Process text into uppercase
    processed_text = data['text'].upper()

    return jsonify({
        "original_text": data['text'],
        "processed_text": processed_text,
        "message": "Text processed successfully"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
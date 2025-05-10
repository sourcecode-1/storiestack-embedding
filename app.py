#!/usr/bin/env python3

from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

# Initialize Flask and the sentence embedding model
app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route("/embed", methods=["POST"])
def embed_text():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    # encode() returns a NumPy array — convert to list for JSON
    embedding = model.encode(text).tolist()

    return jsonify({
        "text": text,
        "embedding": embedding
    })

if __name__ == "__main__":
    # On Render the PORT env var will be injected automatically,
    # but here we default to 7840 for local dev.
    import os
    port = int(os.getenv("PORT", 7840))
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)


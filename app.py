#!/usr/bin/env python3

import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

# 🔐 Fix permission error by redirecting HF cache to a safe location
os.environ['HF_HOME'] = '/tmp/huggingface'

# Initialize Flask and the sentence embedding model
app = Flask(__name__)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', cache_folder='/tmp/huggingface')


@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "Embedding service is running."})

@app.route("/embed", methods=["POST"])
def embed_text():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    embedding = model.encode(text).tolist()

    return jsonify({
        "text": text,
        "embedding": embedding
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7840))
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)


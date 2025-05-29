from flask import Flask, request, jsonify
import joblib
import numpy as np
import tensorflow as tf
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity



# Muat model dan tools saat startup
model = tf.keras.models.load_model("model/resep_model.h5")
vectorizer = joblib.load("model/vectorizer.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")
X = joblib.load("model/X.pkl") 

app = Flask(__name__)

@app.route("/api/v1/predict", methods=["POST"])
def predict():
    data = request.json
    input_ingredients = data.get("ingredients")

    if not input_ingredients or not isinstance(input_ingredients, list):
        return jsonify({
            "code": 400,
            "status": "error",
            "message": "Please send 'ingredients' in string list format."
        }), 400

    try:
        # Vektorisasi input
        input_text = " ".join(input_ingredients)
        input_vec = vectorizer.transform([input_text])
      # Cosine similarity antara input dan semua data X
        similarities = cosine_similarity(input_vec, X).flatten()
        top_indices = similarities.argsort()[-5:][::-1]  # Ambil 5 teratas

        # Threshold minimum
        threshold = 0.1
        results = []
        for idx in top_indices:
            score = float(similarities[idx])
            if score >= threshold:
                food_id = label_encoder.inverse_transform([idx])[0]
                results.append({
                    "food_id": int(food_id),
                    "score": score
                })

        # Cek jika hasil kosong
        if not results:
            return jsonify({
                "code": 404,
                "status": "not found",
                "message": "No food found that matches the given ingredients.",
                "data": []
            }), 404

        return jsonify({
            "code": 200,
            "status": "success",
            "data": results
        }), 200

    except Exception as e:
        return jsonify({
            "code": 500,
            "status": "error",
            "message": f"An error occurred on the server: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

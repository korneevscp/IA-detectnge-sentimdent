from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Pipelines HuggingFace pour sentiment + summarization
emotion_classifier = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")
summarizer = pipeline("summarization")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    
    # Analyse émotion
    emotions = emotion_classifier(text[:512])  # limit input length
    dominant_emotion = max(emotions, key=lambda x: x['score'])['label']

    # Résumé (limité à 150 tokens max)
    summary_results = summarizer(text, max_length=150, min_length=40, do_sample=False)
    summary = summary_results[0]['summary_text']

    # Intention (simplifié, on déduit de l’émotion ici)
    intention_map = {
        "joy": "Informer positivement",
        "sadness": "Exprimer tristesse ou préoccupations",
        "anger": "Exprimer frustration ou critique",
        "fear": "Alerter sur un danger ou une inquiétude",
        "surprise": "Révéler un fait inattendu",
        "disgust": "Exprimer rejet ou désapprobation"
    }
    intention = intention_map.get(dominant_emotion.lower(), "Analyser le contenu")

    # Score d’objectivité basique : si joie, surprise ou neutre => élevé, sinon faible
    if dominant_emotion.lower() in ["joy", "surprise"]:
        objectivity = 80
    elif dominant_emotion.lower() in ["anger", "fear", "disgust"]:
        objectivity = 40
    else:
        objectivity = 60

    alt_source = "https://fr.wikipedia.org"
    alt_label = "Wikipedia (source neutre)"

    return jsonify({
        "summary": summary,
        "emotion": dominant_emotion,
        "intention": intention,
        "objectivity": objectivity,
        "alt_source": alt_source,
        "alt_label": alt_label
    })

if __name__ == "__main__":
    app.run(port=5000)

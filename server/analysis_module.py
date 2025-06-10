import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(text):
    prompt = f"""
Analyse ce texte :
1. Quelle est l’émotion dominante ?
2. Quelle est l’intention probable ?
3. Résume en 2 phrases neutres.
4. Donne un score d’objectivité (0 à 100).
Texte :
{text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["choices"][0]["message"]["content"].split("\n")

    return {
        "emotion": content[0].replace("Émotion :", "").strip(),
        "intention": content[1].replace("Intention :", "").strip(),
        "summary": content[2].replace("Résumé :", "").strip(),
        "objectivity": int("".join(filter(str.isdigit, content[3])))
    }

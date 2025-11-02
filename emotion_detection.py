import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Calls Watson NLP Emotion Predict, parses the response, and returns
    a dictionary with the five target emotions and the dominant emotion.

    Args:
        text_to_analyze: The input text to analyze for emotions.

    Returns:
        A dictionary with keys: 'anger', 'disgust', 'fear', 'joy',
        'sadness', and 'dominant_emotion'.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)

    default_output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': ''
    }

    if response.status_code != 200:
        return default_output

    try:
        data = json.loads(response.text)
        emotions_raw = (
            data.get("emotionPredictions", [{}])[0]
            .get("emotion", {})
        )

        anger = emotions_raw.get('anger')
        disgust = emotions_raw.get('disgust')
        fear = emotions_raw.get('fear')
        joy = emotions_raw.get('joy')
        sadness = emotions_raw.get('sadness')

        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
        }

        available = {k: v for k, v in result.items() if v is not None}
        dominant = max(available, key=available.get) if available else ''
        result['dominant_emotion'] = dominant

        return result
    except Exception:
        return default_output

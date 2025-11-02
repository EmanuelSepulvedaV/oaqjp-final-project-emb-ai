import requests

def emotion_detector(text_to_analyze: str) -> str:
    """
    Calls Watson NLP Emotion Predict and returns the raw response text.

    Args:
        text_to_analyze: The input text to analyze for emotions.

    Returns:
        The response text from the Emotion Predict service.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)
    return response.text

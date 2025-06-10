from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def analyze(self, text):
        result = self.classifier(text)
        label = result[0]['label']
        score = result[0]['score']

        # NEUTRAL tahmini
        if score < 0.75:
            label = 'NEUTRAL'

        return {'sentiment': label, 'confidence': score}

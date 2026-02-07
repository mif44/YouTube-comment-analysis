from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")


    def analyze_batch(self, comments: list) -> list:

        if not comments:
            return []
        
        raw_result = self.classifier(comments)

        processed_results = []
        for res in raw_result:
            score = round(res["score"], 2)
            processed_results.append({"sentiment": res["label"], "score": score})

        return processed_results


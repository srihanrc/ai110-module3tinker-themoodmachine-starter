from mood_analyzer import MoodAnalyzer


def run_tests():
    analyzer = MoodAnalyzer()

    tests = [
        ("Positive", "I absolutely love this — it's fantastic!"),
        ("Negative", "I hate this so much, it's awful."),
        ("Neutral", "I went to the store to buy milk."),
        ("Positive repeated", "I'm soooo happy!!! :) 😂"),
        ("Negative repeated", "This is soooooo bad... I hate it 😭")
    ]

    for name, text in tests:
        print(f"--- {name} ---")
        print("Text:", text)
        print("Tokens:", analyzer.preprocess(text))
        print("Score:", analyzer.score_text(text))
        print("Label:", analyzer.predict_label(text))
        print("Explain:", analyzer.explain(text))
        print()


if __name__ == '__main__':
    run_tests()

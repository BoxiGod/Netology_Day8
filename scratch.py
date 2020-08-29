import json
from collections import Counter


def main():
    words = []
    with open('newsafr.json', encoding='utf-8') as f:
        news_afr = json.load(f)
        for news in news_afr['rss']['channel']['items']:
            list(map(lambda word: words.append(word) if len(word) > 6 else "", news['description'].split(" ")))
            list(map(lambda word: words.append(word) if len(word) > 6 else "", news['title'].split(" ")))
        print(Counter(list(map(lambda text: text.lower(), words))).most_common(10))


main()

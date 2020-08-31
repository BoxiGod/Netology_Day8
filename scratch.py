import json
from collections import Counter
from itertools import chain


def main():
    words = []
    with open('newsafr.json', encoding='utf-8') as f:
        news_afr = json.load(f)
        for news in news_afr['rss']['channel']['items']:
            for word in chain(news['description'].lower().split(), news['title'].lower().split()):
                if len(word) > 6:
                    words.append(word)
        print(Counter(words).most_common(10))


main()

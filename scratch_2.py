import json


def check_words(*name, words):
    for text in name:
        for word in text:
            if len(word) > 6:
                if word.lower() not in words.keys():
                    words[word.lower()] = 1
                else:
                    words[word.lower()] += 1


def main():
    words = {}
    with open('newsafr.json', encoding='utf-8') as f:
        news_afr=json.load(f)
        for news in news_afr['rss']['channel']['items']:
            check_words(news['title'].split(" "), news['description'].split(" "), words=words)
    for counter, key in enumerate(sorted(words, key=words.get, reverse=True)[:10]):
        print(key, words[key])


main()


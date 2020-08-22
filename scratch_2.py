import json


def main():
    words = {}
    with open('newsafr.json', encoding='utf-8') as f:
        news_afr=json.load(f)
        for news in news_afr['rss']['channel']['items']:
            title = news['title'].split(" ")
            description = news['description'].split(" ")
            for word in title:
                if len(word) > 6:
                    if word not in words.keys():
                        words[word] = 1
                    else:
                        words[word] += 1
            for word in description:
                if len(word) > 6:
                    if word not in words.keys():
                        words[word] = 1
                    else:
                        words[word] += 1
    for counter, key in enumerate(sorted(words, key=words.get, reverse=True)):
        if counter < 10:
            print(key, words[key])


main()

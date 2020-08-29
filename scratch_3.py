import xml.etree.ElementTree as ET


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
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    all_news = root.findall('channel/item')
    for news in all_news:
        check_words(news.find("title").text.split(" "), news.find("description").text.split(" "), words=words)
    for counter, key in enumerate(sorted(words, key=words.get, reverse=True)[:10]):
        print(key, words[key])


main()

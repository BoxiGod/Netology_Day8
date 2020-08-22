import xml.etree.ElementTree as ET


def main():
    words = {}
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    all_news = root.findall('channel/item')
    for news in all_news:
        title = news.find("title").text.split(" ")
        description = news.find("description").text.split(" ")
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
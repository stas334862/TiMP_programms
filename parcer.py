from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'form':
            print('See form')
            print(attrs)

if __name__ == "__main__":
    with open('index.html', encoding = 'utf-8') as fin:
        p = MyHTMLParser()
        p.feed(fin.read())
        p.close()

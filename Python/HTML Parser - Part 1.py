from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for ii in attrs:
            print('->', ii[0], '>', ii[1])
    def handle_endtag(self, tag):
        print("End :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for ii in attrs:
            print('->', ii[0], '>', ii[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"+
"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")

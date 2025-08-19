from bs4 import BeautifulSoup
import requests


# This is an example for how a webscraper works
def htmlparser():
    html_doc = """
    <html>
    <head>
    <title>My first Page</title>
    </head>

    <body>
    <p>My name is Manoj</p>
    <p>My name is P2</p>
    </body>
    </html>
    """

    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title)
    print(soup.find('p').string)


# Now well try to scrape from live website using url
def liveurl():

    url = "https://www.iplt20.com/players/virat-kohli/164"

    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all('div', class_ = "membr-details-img position-relative"))


liveurl()
htmlparser()
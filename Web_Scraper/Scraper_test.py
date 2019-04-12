from bs4 import BeautifulSoup
import urllib3
import requests

def main():
    #url = "https://www.youtube.com/watch?v=E9H933ttaYo"
    url = input("Enter the url of the youtube video: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    #output = open("text.html", "w")
    #for i, item in enumerate(soup.contents):
    #    output.write("{}: {}".format(i, item))

    viewList = soup.find_all("div", {"class": "watch-view-count"})
    print("{}: {}".format(soup.title.text, viewList[0].text))
    #output.close()

if __name__ == "__main__":
    main()
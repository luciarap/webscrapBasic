from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def execute():
    # url, z ktorej ideme scrapovat
    page_url = "https://www.fiit.stuba.sk"

    # nadviaze spojenie s webstrankou
    myClient = uReq(page_url)

    # funkcia parsuje html stranku aby sa s nou dalo pracovat
    pageSoup = soup(myClient.read(), "html.parser")

    myClient.close()

    # vsetky elementy ktore chcem
    containers = pageSoup.findAll("div", {"class": "cover"})
    spanContainer = pageSoup.findAll("span", {"class": "text"})
    outFile = "spravy.txt"


    f = open(outFile, "w")

    for container in containers:
        title_fiit = container.a.attrs['title']
        #text_fiit = container.span
        #print("title: " + title + "\n")
        #print("text: " + text + "\n")
        f.write(title_fiit+ "\n")

    for i in spanContainer:
        text_fiit = i.text
        f.write(text_fiit + "\n")

    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute()


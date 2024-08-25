import requests
from bs4 import BeautifulSoup
import summarize
import urllib
import say


def parse_web_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text or specific content
    paragraphs = soup.find_all('p')
    return " ".join(p.get_text(strip=True) for p in paragraphs)

def shouldIgnoreUrl(href):
    return href.startswith('/url?url=')

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    # Find all search result links (Google uses <a> tags with specific attributes)
    aTags = soup.find_all('a') 
    for a in aTags:
        href = a.get('href')
        if href and href.startswith('/url?'):
            if shouldIgnoreUrl(href):
                continue
            parts = href.split('url=')
            url = parts[1].split('&')[0]
            full_url = urllib.parse.unquote(url)
            links.append(full_url)
    # print(f"extracting text from {len(links)} links")
    # print("links : ", links)
    return links


def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    
    # extract links
    links = extract_links(response.text)


    maxLinks = 2
    # linksConsidered = 0
    linksConsidered = {}
    # Fetch and parse each page
    all_texts = []
    totaltext = ""
    urls = ""
    print("processing...", end="")
    for url in links:
        if url in linksConsidered or len(linksConsidered) >= maxLinks: break
        resp = requests.get(url)
        if resp == None or resp.text == "":
            # resp.raise_for_status()
            continue
        linksConsidered[url] = True
        urls += url+"\n"
        # print(f"extracting text from {url} ", end=" \t ")
        text = parse_web_page(resp.text)
        # print("done")
        lines = text.split(". ")
        wrdCount = 0
        takeLines = len(lines)
        for i in range(0, len(lines)):
            if wrdCount > 50:
                takeLines = i
                break
            lines[i] = lines[i]+". "
            wrdCount += len(lines[i].split())

        speakText = "".join(lines[:takeLines]) + "\n"
        totaltext += speakText
        print("...", end="")
    print()
    # print(totaltext)
    print("get ready to listen...")
    say.say_text("according to search results...\n" + totaltext)
    
    # to get summary un-comment below code and and comment above line
    # for i in range(0, len(all_texts)):
    #     all_texts[i] =  " ".join(all_texts[i].split()[:125])
    # full_text = " ".join(all_texts)
    # print("length of the tokens : ", len(full_text.split()))
    # print("fetching summary...please wait...")
    # summary = summarize.get_summary(full_text)
    # say.say_text(summary)
    return urls


if __name__ == "__main__":
    query = input("enter query, keep it short and sweet :) \n")
    results = google_search(query)
    print("this is the summary : ")
    print(results)





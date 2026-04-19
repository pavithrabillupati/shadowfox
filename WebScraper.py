import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException:
            print("Error fetching the webpage")

    def search_links(self, keyword):
        results = []
        links = self.soup.find_all("a")

        for link in links:
            text = link.text.strip()
            href = link.get("href")

            if text and href and keyword.lower() in text.lower():
                if href.startswith("/"):
                    href = self.url + href
                results.append((text, href))

        return results

    def scrape(self, keyword):
        self.fetch_page()
        if not self.soup:
            return
        
        results = self.search_links(keyword)

        print("\n========== SEARCH RESULTS ==========")
        print(f"Keyword: {keyword}\n")

        if results:
            for i, (text, link) in enumerate(results, 1):
                print(f"{i}. {text}")
                print(f"   Link: {link}\n")
        else:
            print("No matching links found.")

        print("===================================")


if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    keyword = input("Enter a keyword to search: ")

    scraper = WebScraper(url)
    scraper.scrape(keyword)
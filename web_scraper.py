import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.find('title').text if soup.find('title') else 'No title found'
        print(f"Title: {title}")

        # Extract all headings
        headings = soup.find_all(['h1', 'h2', 'h3'])
        print("\nHeadings:")
        for heading in headings:
            print(f"- {heading.text.strip()}")

        # Extract all links
        links = soup.find_all('a', href=True)
        print("\nLinks:")
        for link in links[:10]:  # Limit to first 10 links
            print(f"- {link.text.strip()}: {link['href']}")

    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_website(url)

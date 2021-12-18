from googlesearch import search
import os

# Schritt 1
from Downloader import download_files_from_websites
from main import download_path


def get_website_links(queries: set, amount: int) -> None:
    urls = []
    for query in queries:
        print("Queryterm:", query)
        for url in search(query, tld="co.in", num=amount, stop=amount, pause=2):
            urls.append(url)
            print(url)
        print("\n\n")
    urls = list(set(urls))
    print("Urls with amount: ", len(urls), " are: ", urls, "\n")
    with open(os.path.join(download_path, "urls.txt"), "w") as file:
        for url in urls:
            file.write(url + "\n")
    download_files_from_websites(urls)

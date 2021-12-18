#  Copyright Notice for YitongSuperProf
#  Copyright (c) at Carina Schoppe 2021
#  File created on 18.12.21, 16:08 by Carina Latest changes made by Carina on 18.12.21, 15:49 All contents of "Searcher.py" are protected by copyright. The copyright law, unless expressly indicated otherwise, is
#  at Carina Schoppe. All rights reserved
#  Any type of duplication, distribution, rental, sale, award,
#  Public accessibility or other use
#  requires the express written consent of Carina Schoppe.

import os

from googlesearch import search

# Schritt 1
from main import download_path


def get_website_links(queries: set, amount: int) -> None:
    from Downloader import download_files_from_websites
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

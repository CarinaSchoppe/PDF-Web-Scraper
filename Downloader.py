# Schritt 2
import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from Analysator import analyse_pdf_files_for_content
from main import analyse_straight, words, download_path


def download_files_from_websites(urls: set) -> None:
    folder_location = download_path
    for url in urls:
        print("url:", url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            if not soup.select("a[href$='.pdf']"):
                print("no pdf found")
            for link in soup.select("a[href$='.pdf']"):
                file_name = os.path.join(folder_location, link['href'].split('/')[-1])
                print("found a pdf:", file_name.replace(download_path + "\\", ""))
                if not os.path.isfile(file_name):
                    with open(file_name, 'wb') as file:
                        file.write(requests.get(urljoin(url, link['href'])).content)
                        print("File downloaded!")
                        if analyse_straight:
                            if analyse_pdf_files_for_content(filter_dict=words, file=file_name):
                                file.close()
                                try:
                                    os.remove(file_name)
                                    print("File deleted!\n")
                                except:
                                    print(f"Could not delete file {file}")
                else:
                    print("File already exists!")
        except:
            continue
        print("")
    print("all files downloaded")
    if not analyse_straight:
        print("analyse files")
        analyse_pdf_files_for_content(filter_dict=words)
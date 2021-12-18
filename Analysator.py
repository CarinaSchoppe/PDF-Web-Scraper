#  Copyright Notice for YitongSuperProf
#  Copyright (c) at Carina Schoppe 2021
#  File created on 18.12.21, 16:08 by Carina Latest changes made by Carina on 18.12.21, 16:06 All contents of "Analysator.py" are protected by copyright. The copyright law, unless expressly indicated otherwise, is
#  at Carina Schoppe. All rights reserved
#  Any type of duplication, distribution, rental, sale, award,
#  Public accessibility or other use
#  requires the express written consent of Carina Schoppe.

import os

import PyPDF2

import main
from main import download_path, words


# Schritt 3
def analyse_pdf_files_for_content(filter_dict: dict = words, file: str = None, analysor: bool = False) -> bool:
    if not analysor:
        if file is None:
            for data in os.listdir(download_path):
                if data.endswith(".pdf"):
                    print("analyse file:", data)
                    path = f"{download_path}\\{data}"
                    if analyse_pdf_files_for_content(filter_dict=words, file=path):
                        try:
                            os.remove(path)
                            print("file deleted")
                        except Exception:
                            print("Could not delete file!")
                print()
        elif file is not None:
            is_relevant = True
            try:
                pdf_reader = PyPDF2.PdfFileReader(file)
                for word in words:
                    counter = 0
                    for page in range(pdf_reader.numPages):
                        page_content = pdf_reader.getPage(page).extractText()
                        counter += page_content.count(word)
                    print(word, "found", counter, "times")
                    if counter < filter_dict[word]:
                        print("file is not relevant")
                        is_relevant = False
                        break
                if not is_relevant:
                    return True
                else:
                    print("file: ", file, " is relevant with: ", pdf_reader.getNumPages(), " pages.\n")
                    return False
            except Exception:
                print("Error opening the file. The file cant be read!\n")
                os.remove(file)
                print("File deleted!")
            if not is_relevant:
                return True
            else:
                print("file: ", file, " is relevant with: ", pdf_reader.getNumPages(), " pages.\n")
                return False
    elif analysor:
        try:
            with open(os.path.join(main.download_path, "pages.txt"), "w") as data_file:
                for data in os.listdir(main.download_path):
                    if data.endswith(".pdf"):
                        print("analyse file:", data)
                        page_counter = {data: []}
                        path = f"{main.download_path}\\{data}"
                        try:
                            pdfFile = PyPDF2.PdfFileReader(path)
                        except Exception:
                            print("Error opening the file. The file cant be read!\n")
                            os.remove(file)
                            print("File deleted!")
                        for page in range(pdfFile.numPages):
                            good_page = True
                            page_content = pdfFile.getPage(page).extractText()
                            for word in filter_dict:
                                word_counter = page_content.count(word)
                                if word_counter < filter_dict[word]:
                                    good_page = False
                            if good_page:
                                print("page is relevant")
                                page_counter[data].append(page)
                        if len(page_counter[data]) > 0:
                            data_file.write(f"{data}:\n")
                            for page in page_counter[data]:
                                data_file.write(f"- {page}\n")
                            data_file.write("\n")
                    print("\n")
        except Exception as e:
            print(e)

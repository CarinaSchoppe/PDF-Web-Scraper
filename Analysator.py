# Schritt 3
import os

import PyPDF2

from main import download_path, words


def analyse_pdf_files_for_content(filter_dict: dict = words, file: str = None) -> bool:
    if file is None:
        for data in os.listdir(download_path):
            if data.endswith(".pdf"):
                print("analyse file:", data)
                path = f"{download_path}\\{data}"
                if analyse_pdf_files_for_content(filter_dict=words, file=path):
                    try:
                        os.remove(path)
                        print("file deleted")
                    except:
                        print("Could not delete file!")
            print()
    else:
        is_relevant = True
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
        except:
            print("Error opening the file. The file cant be read!")
            os.remove(f"{download_path}\\{file}")
            print("File deleted!")
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

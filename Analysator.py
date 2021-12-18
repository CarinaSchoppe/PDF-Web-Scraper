# Schritt 3
import os

import PyPDF2

import main
from main import download_path, words


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
                        except:
                            print("Could not delete file!")
                print()
        elif file is not None:
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
    elif analysor:
        try:
            with open(os.path.join(main.folderLocation, "pages.txt"), "w") as data_file:
                for data in os.listdir(main.folderLocation):
                    if data.endswith(".pdf"):
                        print("analyse file:", data)
                        page_counter = {data: []}
                        path = f"{main.folderLocation}\\{data}"
                        pdfFile = PyPDF2.PdfFileReader(path)
                        for page in range(pdfFile.numPages):
                            good_page = True
                            page_content = pdfFile.getPage(page).extractText()
                            for word in filter_dict:
                                if word not in page_content:
                                    good_page = False
                            if good_page:
                                print("page is relevant")
                                page_counter[data].append(page)
                        if len(page_counter[data]) > 0:
                            data_file.write(f"{data}:\n")
                            for page in page_counter[data]:
                                data_file.write(f"- {page}\n")
                            data_file.write("\n")
        except Exception as e:
            print(e)

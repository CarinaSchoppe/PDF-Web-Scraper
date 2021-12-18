"""durchsuche webseiten mit einem namen oder reggex (z.B. wissenschaftsSeite.org)
suche dort auf der webseite nach weiterleitungs links -> durchsuche diese links und schau nach PDFs
downloade diese und "analysiere" sie (z.B. zeitungsartikel) und speichere sie dann ab oder lösch sie.
"""
from Searcher import get_website_links
from Util import getInputs
from Analysator import analyse_pdf_files_for_content

download_path = r"C:\Users\Carina\Downloads"
folderLocation = r"C:\Users\Carina\Downloads"
analyse_straight = True
analyse_folder = False
queries = {"Finite Element Methods", "Finite Element Analysis", "Finite Element"}
words = {"finite element": 3, "method": 2, "function": 2, "boundary condition": 2}
search_result_amounts = 50

if __name__ == "__main__":
    getInputs()
    print("\nInput is done starting the program!\n")
    if analyse_folder:
        analyse_pdf_files_for_content(file=None, filter_dict=words, analysor=True)
    else:
        get_website_links(queries, search_result_amounts)
    print("Program is done")

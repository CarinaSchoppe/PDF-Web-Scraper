"""durchsuche webseiten mit einem namen oder reggex (z.B. wissenschaftsSeite.org)
suche dort auf der webseite nach weiterleitungs links -> durchsuche diese links und schau nach PDFs
downloade diese und "analysiere" sie (z.B. zeitungsartikel) und speichere sie dann ab oder lösch sie.
"""
from Searcher import get_website_links
from Util import getInputs

download_path = r"C:\Users\Carina\Downloads"
analyse_straight = True
queries = {"Finite Element Methods", "Finite Element Analysis", "Finite Element"}
words = {"finite element": 3, "method": 2, "function": 2, "boundary condition": 2}
search_result_amounts = 50

if __name__ == "__main__":
    getInputs()
    print("\nInput is done starting the program!\n")
    get_website_links(queries, search_result_amounts)
    print("Program is done")

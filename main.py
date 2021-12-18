"""durchsuche webseiten mit einem namen oder reggex (z.B. wissenschaftsSeite.org)
suche dort auf der webseite nach weiterleitungs links -> durchsuche diese links und schau nach PDFs
downloade diese und "analysiere" sie (z.B. zeitungsartikel) und speichere sie dann ab oder lösch sie.
"""

download_path = r"C:\Users\Carina\Downloads"
folderLocation = r"C:\Users\Carina\Downloads"
analyse_straight = True
analyse_folder = False
queries = {"Finite Element Methods", "Finite Element Analysis", "Finite Element"}
words = {"finite element": 3, "method": 2, "function": 2, "boundary condition": 2}
search_result_amounts = 50

if __name__ == "__main__":
    from Util import getInputs

    getInputs()

    print("Program is done")

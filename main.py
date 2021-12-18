#  Copyright Notice for YitongSuperProf
#  Copyright (c) at Carina Schoppe 2021
#  File created on 18.12.21, 16:10 by Carina Latest changes made by Carina on 18.12.21, 16:10
#  All contents of "main.py" are protected by copyright.
#  The copyright law, unless expressly indicated otherwise, is
#  at Carina Schoppe. All rights reserved
#  Any type of duplication, distribution, rental, sale, award,
#  Public accessibility or other use
#  requires the express written consent of Carina Schoppe.


"""durchsuche webseiten mit einem namen oder reggex (z.B. wissenschaftsSeite.org)
suche dort auf der webseite nach weiterleitungs links -> durchsuche diese links und schau nach PDFs
downloade diese und "analysiere" sie (z.B. zeitungsartikel) und speichere sie dann ab oder lösch sie.
"""

download_path = r"C:\Users\Carina\Downloads"
analyse_straight = True
analyse_folder = False
queries = {"Finite Element Methods", "Finite Element Analysis", "Finite Element"}
words = {"finite element": 3, "method": 2, "function": 2, "boundary condition": 2}
search_result_amounts = 50

if __name__ == "__main__":
    from Util import getInputs

    getInputs()
    print("Program is done")

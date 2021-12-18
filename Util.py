import main
from Analysator import analyse_pdf_files_for_content
from Searcher import get_website_links


def getInputs() -> None:
    main.download_path = input("Enter the path to the folder where the files should be: ")
    if main.download_path == "":
        return getInputs()
    folder = input("Analyse folder? (y/n): ").lower()
    if folder != "y" and folder != "n":
        return getInputs()
    main.analyse_folder = folder == "y"
    if not main.analyse_folder:
        straight = input("Analyse straight? (y/n): ").lower()
        if straight != "y" and straight != "n":
            return getInputs()
        main.analyse_straight = straight == "y"
    if not main.analyse_folder:
        main.queries = input("Enter the queries (separated by comma): ")
        if main.queries == "" and not main.analyse_folder:
            return getInputs()
        main.queries = main.queries.split(",")
    filter_words = input("Enter the words that should be filtered (separated by comma): ")
    main.words.clear()
    if filter_words != "":
        filter_words = filter_words.split(",")
        for word in filter_words:
            main.words[word] = getNumer(word)

    if not main.analyse_folder:
        main.search_result_amounts = getInputNumer()
    print("\nInput is done starting the program!\n")
    if main.analyse_folder:
        analyse_pdf_files_for_content(file=None, filter_dict=main.words, analysor=True)
    else:
        get_website_links(main.queries, main.search_result_amounts)


def getNumer(word: str) -> int:
    try:
        x = int(input(f"Enter the amount of \"{word}\" that should be found: "))
        return x
    except Exception:
        print("Please enter a number!")
        return getNumer(word)


def getInputNumer() -> int:
    try:
        x = int(input("Enter the amount of search results: "))
        return x
    except Exception:
        print("Please enter a number!")
        return getInputNumer()

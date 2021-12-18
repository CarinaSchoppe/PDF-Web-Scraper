import main


def getInputs() -> None:
    main.folderLocation = input("Enter the folder location: ")
    if main.folderLocation == "":
        return getInputs()
    main.download_path = input("Enter the path to the folder where the files should be downloaded: ")
    if main.download_path == "":
        return getInputs()
    straight = input("Analyse straight? (y/n): ").lower()
    if straight != "y" and straight != "n":
        return getInputs()
    main.analyse_straight = straight == "y"
    folder = input("Analyse folder? (y/n): ").lower()
    if folder != "y" and folder != "n":
        return getInputs()
    main.analyse_folder = folder == "y"
    main.queries = input("Enter the queries (separated by comma): ")
    if main.queries == "":
        return getInputs()
    main.queries = main.queries.split(",")
    main.words = {}
    filter_words = input("Enter the words that should be filtered (separated by comma): ")
    if filter_words != "":
        filter_words = filter_words.split(",")
        for word in filter_words:
            main.words[word] = getNumer(word)
    main.search_result_amounts = getInputNumer()


def getNumer(word: str) -> int:
    try:
        x = int(input(f"Enter the amount of \"{word}\" that should be found: "))
        return x
    except:
        print("Please enter a number!")
        return getNumer(word)


def getInputNumer() -> int:
    try:
        x = int(input("Enter the amount of search results: "))
        return x
    except:
        print("Please enter a number!")
        return getInputNumer()

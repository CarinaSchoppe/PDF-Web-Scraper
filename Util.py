def getInputs() -> None:
    global download_path
    global analyse_straight
    global queries
    global words
    global search_result_amounts
    download_path = input("Enter the path to the folder where the files should be downloaded: ")
    if download_path == "":
        return getInputs()
    straight = input("Analyse straight? (y/n): ").lower()
    if straight != "y" and straight != "n":
        return getInputs()
    analyse_straight = straight == "y"
    queries = input("Enter the queries (separated by comma): ")
    if queries == "":
        return getInputs()
    queries = queries.split(",")
    words = {}
    filter_words = input("Enter the words that should be filtered (separated by comma): ")
    if filter_words != "":
        filter_words = filter_words.split(",")
        for word in filter_words:
            words[word] = getNumer(word)
    search_result_amounts = getInputNumer()


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

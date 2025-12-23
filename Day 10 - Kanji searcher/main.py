import requests

endpoint = "https://kanjiapi.dev/v1"

# function to retrieve data from the api
def get_kanji(kanji):
    url = requests.get(f"{endpoint}/kanji/{kanji}")
    if url.status_code == 200:
        return url.json() # returns a json/dictionary
    elif len(kanji)> 1:
        print("Failed to retrieve data, please enter only 1 character!")
        return 0
    elif url.status_code == 404:
        print(f"Failed to retrieve data, {kanji} not found!")
        return 0
    else:
        print("Failed to retrieve data, Something went wrong!")
        return 0
        

def main():
    print("------------ 漢字の探すアプリへ、ようこそ！ -----------------")
    while True:
        user_input = input("Enter kanji to be searched (出口 to exit): ")
        if user_input == "出口":
            print("このアプリを利用、ありがとう！")
            break

        kanji = get_kanji(user_input)
        if not kanji == 0: # 0 means the data was failed to be retrieved
            kanji_obj = {
                "Kanji": kanji["kanji"],
                "Onyomi": "、".join(kanji["on_readings"]),
                "Kunyomi": "、".join(kanji["kun_readings"]),
                "Meanings": ", ".join(kanji["meanings"]),
                "JLPT Level": f"N{kanji["jlpt"]}",
                "Mainichi Shinbun frequency": kanji["freq_mainichi_shinbun"]
            }
            
            print("----------------- Results -----------------")
            for key, value in kanji_obj.items():
                print(f"{key}: {value}")
            print("-------------------------------------------")


if __name__ == "__main__":
    main()
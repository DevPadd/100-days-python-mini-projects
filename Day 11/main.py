import requests

base_url = "https://candaan-api.vercel.app/api/text/random"
def get_jokes():
    url = requests.get(base_url)

    if url.status_code == 200:
        return url.json()["data"]
    else:
        return "duh pusing, abis amunisi lawakan wkwkwk"
question = "Mau gw kasih tau jokes lucu ga?"
while True:
    print(question)
    action = input("(mau/ga): ")
    if action == "ga":
        print("gaasik lo")
        break
    else:
        print(get_jokes())
        input("> WKWKWKWWKWKWK")
        question = "Mau gw kasih tau jokes lucu lagi ga?"

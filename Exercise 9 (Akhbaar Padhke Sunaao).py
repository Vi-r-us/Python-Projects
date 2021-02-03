import requests
import json


def bolo(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    country = input("Enter country name 'e.g-for india enter in'"
                  "\n(ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in "
                  "it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th "
                  "tr tw ua us ve za):\n")
    category = input("\nEnter category you want to listen"
                   "(business entertainment general health science sports technology):\n")
    ran = int(input("\nHow many news you want:\n"))
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=94e32393793c4b75a9780f50edf052e2")
    parsed = json.loads(r.text)
    for i in range(ran):
        print(f"\n\n{i+1} News is\n")
        print(parsed['articles'][i]['title'])
        bolo(parsed['articles'][i]['title'])
        print("The description of above news is...."+parsed['articles'][i]['description'])
        bolo("The description of above news is...."+parsed['articles'][i]['description'])
        print("For more information you can visit these:")
        print(parsed['articles'][i]['url'])
        print(parsed['articles'][i]['urlToImage'])

        if i ==(ran-1):
            continue
        bolo("\nThe next news is")
    else:
        bolo("Thanks.... for ....listening.......")

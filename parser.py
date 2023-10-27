import requests
import get_url.api
import json
import sys
while True:
    try:
        parse = requests.get(get_url.api.URL).json()
        with open('data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(parse, indent=4))

        answ = input("Json found! Save file? Y/N also if you want open it press R... ")
        if answ.lower() == "y":
            break

        elif answ.lower() == "r":
            with open('data.json', 'r', encoding='utf-8') as file:
                get = json.load(file)
                first = get[0]
                for value, item in first.items():
                    print(value, item)
        elif answ.lower() == "n":
            break
        else:
            continue

    except Exception as error:
        print(f"Sorry it seems that this is not json!")
        exit = input("Stop process?")
        if exit.lower() == "y":
            break








 
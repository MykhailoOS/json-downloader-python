import parser as p

while True:
    def show_elements():
        for i in p.parse:
            for value, items in i.items():
                print(value, items)


    func = show_elements()
    ask = input("Exit?")
    if ask.lower() == "y":
        break


    if __name__ == 'main':
        print(func)

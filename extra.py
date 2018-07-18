def linearSearch(list, item):
    for i in range(0, len(list)):
        if list[i] == item:
            return print(str(item) + "was found at postion " + str(i))
    return print("-1. The item was not found.")

def main():
    while(True):
        game = input("\nPress 1 for Linear search\n \nPress 2 for Binary search\n \nPress 3 for Bubble sort\n \nPress 4 to exit: \n")
        if game == "1":
            linearSearch()
        elif game == "2":
            binary()
        elif game == "3":
            bubble()
        elif game == "4":
            print("Good, Bye!")
            exit()

main()
linearSearch()

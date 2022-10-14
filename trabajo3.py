
def clothes ():
    print("It's cold?")
    option = input("Yes/no: ")
    while (option != "y") and (option != "n"):
            print("Ding dong, your opinion is wrong")
            option = input("Yes/no: ")
    if option == "y":
        choose = "Yes"
        print("It's sunny?")
        option = input("Yes/no: ")
        while (option != "y") and (option != "n"):
                print("Ding dong, your opinion is wrong")
                option = input("Yes/no: ")
        if option == "y":
            choose = "Yes"
            print("You dont need anything")
            print("ypu should use a jacket")
        elif option == "n":
            choose = "No"
            print("its raining?")
            option = input("Yes/no: ")
            while (option != "y") and (option != "n"):
                    print("Ding dong, your opinion is wrong")
                    option = input("Yes/no: ")
            if option == "y":
                choose = "Yes"
                print("Wear an oilskin")
                print("Wear a rain coat")
            elif option == "n":
                choose = "No"
                print("You dont need anything")
                print("You should wear a coat")

    elif option == "n":
        choose = "No"
        print("¿It's sunny?")
        option = input("Yes/no: ")
        if option == "y":
            choose = "Yes"
            print("You should wear a coat")
            print("you can wear a cap")
        elif option == "n":
            choose = "No"
            print("It's raining?")
            option = input("Yes/no: ")
            while (option != "y") and (option != "n"):
                    print("Ding dong, your opinion is wrong")
                    option = input("Yes/no: ")
            if option == "y":
                choose = "Yes"
                print("you should wear an oilskin")
                print("wear a rain cap")
            elif option == "n":
                choose = "No"
                print("you can wear a jacket")
                print("you can wear a cap")

clothes()
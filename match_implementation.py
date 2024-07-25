status=int(input())
match status:
        case 400: print("1")
        case 404: print("2")
        case 418: print("3")
        case _:   print("nothing matched")

while True:
    name, saturation = input().split()
    if name == "#" and saturation == "0":
        break
    saturation = int(saturation)
    
    if saturation < 90:
        print(name +" "+ "Internar")
    else:
        print(name +" "+ "Alta")
    
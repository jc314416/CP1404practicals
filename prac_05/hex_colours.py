HEX_COLOURS = {"AliceBlue": "#fof8ff", "BlancheAlmond": "#ffebcd", "CadetBlue": "#5f9ea0", "DarkGoldenrod": "#b8860b",
               "ForestGreen": "#228b22", "HotPink": "#ff69b4", "IndianRed": "#cd5c5c", "LawnGreen": "#7cfc00",
               "magenta": "#ff00ff", "orange1": "#ffa500", "PaleTurquoise": "#afeeee"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print("{:<12} is {:<}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")

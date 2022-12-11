COLOR_NAME_HEX = {"ABSOLUTE ZERO": "#0048ba", "ALICEBLUE": "#f0f8ff", "AMBER": "#ffbf00", "AQUA": "#ooffff",
                  "BRILLIANT ROSE": "#ff55a3", "BUFF": "#f0dc82", "CADMIUM YELLOW": "#fff600", "CARNELIAN": "#b31b1b",
                  "COSMIC LATTE": "#fff8e7", "DARKGREEN": "#006400"}
print(COLOR_NAME_HEX)

color_hex = input("Enter color name: ").upper()
while color_hex != "":
    if color_hex in COLOR_NAME_HEX:
        print(color_hex, "is", COLOR_NAME_HEX[color_hex])
    else:
        print("Invalid color name")
    color_hex = input("Enter color name: ").upper()
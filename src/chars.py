# Raster images of the numbers 1 to 10 in 6x10 arrays

chars = {
    '0': [
        " #### ",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        " #### ",
    ],
    '1': [
        "  ##  ",
        " # #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        " #### ",
    ],
    '2': [
        " #### ",
        "#    #",
        "     #",
        "     #",
        "    # ",
        "   #  ",
        "  #   ",
        " #    ",
        " #    ",
        "######",
    ],
    '3': [
        " #### ",
        "#    #",
        "     #",
        "     #",
        " #### ",
        "     #",
        "     #",
        "     #",
        "#    #",
        " #### ",
    ],
    '4': [
        "   ## ",
        "  # # ",
        " #  # ",
        "#   # ",
        "#   # ",
        "######",
        "    # ",
        "    # ",
        "    # ",
        "    # ",
    ],
    '5': [
        "######",
        "#     ",
        "#     ",
        "##### ",
        "     #",
        "     #",
        "     #",
        "     #",
        "#    #",
        " #### ",
    ],
    '6': [
        " #### ",
        "#    #",
        "#     ",
        "#     ",
        "##### ",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        " #### ",
    ],
    '7': [
        "######",
        "     #",
        "     #",
        "     #",
        "    # ",
        "   #  ",
        "  #   ",
        "  #   ",
        "  #   ",
        "  #   ",
    ],
    '8': [
        " #### ",
        "#    #",
        "#    #",
        "#    #",
        " #### ",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        " #### ",
    ],
    '9': [
        " #### ",
        "#    #",
        "#    #",
        "#    #",
        " #####",
        "     #",
        "     #",
        "     #",
        "#    #",
        " #### ",
    ]
}

if __name__ == "__main__":
    for number, raster in numbers.items():
        print(f"Number {number}:")
        for line in raster:
            print(line)
        print()
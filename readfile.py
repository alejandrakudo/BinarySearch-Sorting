'''
Read a file of data line by line -- you will need to modify this code to
make it work with the required input file.  You will need to use the absolute
path to your file in order for the file to be found when you run the program.
'''


def readFile():
    with open("C:/Users/wendy/desktop/QueensHopeful.txt", "r") as in_file:
        for line in in_file:
            print line
            

readFile()



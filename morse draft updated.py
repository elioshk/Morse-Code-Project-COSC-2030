#Design_Draft.txt
#Group members:
#Eli Oceanak, Galen Damosso, Fred Wittman, Josh Mallone, Trevor

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.left = None
        self.right = None
        
dummyRoot = Node(None, None)
table = {}
        
def insert(root, node):
    if len(node.key) > 1:
        currSymbol = node.key.pop(0)
        if "-" == currSymbol: 
            if root.right is None:
                root.right = Node("-", None)
                insert(root.right, node)
            else:
                insert(root.right, node) 
        elif "." == currSymbol:
            if root.left is None:
                root.left = Node(".", None)
                insert(root.left, node)
            else: 
                insert(root.left, node)
        else: print("Error!  Improper symbol")
            
    elif len(node.key) == 1:
        currSymbol = node.key[0]
        if "-" == currSymbol:
            if root.right is None:
                root.right = node
                #print(node.val)
            else:
                root.right.val = node.val
                #print(node.val)
        elif "." == currSymbol:
            if root.left is None:
                root.left = node
               # print(node.val)
               # print(node.key)
            else:
                root.left.val = node.val
                #print(node.val)
    else:
        print("Error!  No morse code detected in element!")
                              
def createTree(infile):
    file = open(infile, "r")
    for line in file:
        key = list(line[2:])
        key.pop();
        value = list(line[0])
        nodeToInsert = Node(key, value)
        insert(dummyRoot, nodeToInsert)
    file.close()

def createTable(infile):# this creates a key value table for the english to morse conversion, which is 
    file = open(infile, "r")# allowed in the instructions. Only the morse to english conversion requires a tree.
    for line in file:
        morse = line[2:]
        alpha = line[0]
        table[alpha] = morse
    file.close()
  
def search(root, key):
    if len(key) == 0:
        if root.val == None:
            return "FLAG"
        else:
            return root.val
    curr = key.pop(0)
    if curr == "-":
        root = root.right
        return search(root, key)
    if curr == ".":
        root = root.left
        return search(root, key)
        
def morseToEnglish(infile, outfile, root):
    ifile = open(infile, "r")
    ofile = open(outfile, "w")
    
    for line in ifile:
        symbols = list(line)
        symbols.pop()
        letter = []
        i = 0
        while i < (len(symbols)):
            if i < (len(symbols) - 3) and symbols[i] == " " and symbols[i + 1] == " " and symbols[i + 2] == " ":
                ofile.write("".join(search(dummyRoot, letter)))
                print("".join(search(dummyRoot, letter)))
                ofile.write(" ")
                letter.clear()
                i = i + 2
            elif symbols[i] == " ":
                ofile.write("".join(search(dummyRoot, letter)))
                letter.clear()
            else:
                letter.append(symbols[i])
                
            i = i + 1 
            
    ifile.close()
    ofile.close()

def englishToMorse(infile, outfile):
    ifile = open(infile, "r")
    ofile = open(outfile, "w")
    for line in ifile:
        for word in line.split():
            for x in word:# for each letter in each word in each line, write that letter's morse equivalent but with a space after.
                ofile.write(table[x.lower()].strip() + " ")
            ofile.write("  ")

# This was the most simple way to ask which function of the program the user would like.
x = input("Please enter 0 if you would like to decode a morse file to English, and 1 if you would like to decode English to morse: ")
if x == "0":
    createTree("MorseTable.txt")
    morseToEnglish(input("Please Enter the name of the file you wish to convert from morse to english: "), "output.txt", dummyRoot)
    print("file successfully read and translated. The output will be in the python directory under 'output.txt'")
if x == "1":
    createTable("MorseTable.txt")
    englishToMorse(input("Please Enter the name of the file you wish to convert from English to morse: "), "output.txt")
    print("file successfully read and translated. The output will be in the python directory under 'output.txt'")


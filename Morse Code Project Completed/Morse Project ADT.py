#Design_Draft.txt
#Group members:
#Eli Oceanak, Galen Damosso, Fred Wittman, Josh Mallone, Trevor

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.left = None
        self.right = None
        
        
def insert(root, node):
    """This function inserts a node with a key element consisting of a single character, either '-' or '.', and a value prescribed
    by the value in 'MorseTable' associated with the node's position in the binary search tree, into the binary search tree."""
    
    # This 'if' block inserts new nodes with key values, but cannot insert new nodes with both keys and values.
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
            
    # Once the correct node has been found, this 'elif' block gives it the appropriate value.
    elif len(node.key) == 1:
        currSymbol = node.key[0]
        if "-" == currSymbol:
            if root.right is None:
                root.right = node
            else:
                root.right.val = node.val
        elif "." == currSymbol:
            if root.left is None:
                root.left = node
            else:
                root.left.val = node.val
                
    # If the correct node has not been found by the time the key has been decremented to 0, non-Morse characters were included
    # in the key.  Print error message.
    else:
        print("Error!  Keys must be composed entiredly of Morse characters!")


def createTree(infile, root):
    """createTree creates a binary search tree from the table of key-value pairs and a root element.  It returns the root."""
    
    file = open(infile, "r")
    for line in file:
        key = list(line[2:].rstrip("\n"))
        value = list(line[0])
        nodeToInsert = Node(key, value)
        insert(root, nodeToInsert)
    file.close()
    return root


def search(root, key):
    """search uses a binary search algorithm to return the value associated with the key argument from the binary search tree."""
    
    # Once the key has been decremented to 0 elements, either the correct value has been found or the Morse sequence does
    # not correspond with a value in the binary search tree.  In the latter case, return an appropriate flag.  In the former
    # case, just return the value.
    if len(key) == 0:
        if root == None:
            return list("(FLAG: INVALID MORSE SEQUENCE)")
        else:
            return root.val
        
    # This is the recursive part of the function.  It traces the value that corresponds with the key argument in the same
    # way that the binary search tree was created.
    curr = key.pop(0)
    if curr == "-":
        root = root.right
        return search(root, key)
    if curr == ".":
        root = root.left
        return search(root, key)
    
def buildDict(morseTable):
    """buildDict constructs a dictionary from the key-value pairs found in 'MorseTable' and returns it."""
    
    dict = {}
    mTable = open(morseTable, "r")
    for lines in mTable:
        lines1 = lines.rstrip("\n\s")
        key = lines1[0]
        value = lines1[1:]
        dict[key] = value
    mTable.close()
    return dict
        
def morseToEnglish(infile, outfile, root):
    """morseToEnglish translates the Morse code content of a file to English and writes it to an out-file."""
    
    ifile = open(infile, "r")
    ofile = open(outfile, "w")
    
    for line in ifile:
        letter = []
        i = 0
        
        # This 'while loop' processes each line of the Morse file.
        while i < len(line):
            
            # This 'if' prevents the index, i, from going out of range.  It deals with the last i.
            if i == (len(line) - 1):
                if line[i - 1] == " ":
                    if letter:
                        ofile.write("".join(search(root, letter)) + " ")
                        letter.clear()
                        return
                else:
                    return
            
            # This 'if' block maps a single space to a new letter, and two or more spaces to a space.
            if line[i] == " ":
                j = 0
                while(line[i] == " "):
                    i = i + 1
                    j = j + 1
                if j == 1:
                    if letter:
                        ofile.write("".join(search(root, letter)))
                        letter.clear()
                    i = i - 1
                else:
                    if letter:
                        ofile.write("".join(search(root, letter)))
                        letter.clear()
                    ofile.write(" ")
                    i = i - 1
            
            # If an element of the line is a Morse character ('.' or ','), append it to a list. 
            elif line[i] == "-" or line[i] == ".":
                letter.append(line[i])
                
            elif i == (len(line) - 1):
                if letter:
                    ofile.write("".join(search(root, letter)))
            
            # If line[i] is not a space or a Morse character, it is invalid.
            else:
                ofile.write("(FLAG: INVALID CHARACTER AT THIS POSITION)")
                
            i = i + 1 
            
    ifile.close()
    ofile.close()
    
def englishToMorse (table, infile, outfile):
    """englishToMorse converts the English language contents of an in-file to Morse code, via a table look-up, and writes it to an outfile"""
    
    ifile = open(infile, "r")
    ofile = open(outfile, "w")

    for line in ifile:
        for word in line.split():
            for x in word:# for each letter in each word in each line, write that letter's morse equivalent but with a space after.
                if x.lower().strip() in table:
                    ofile.write(table[x.lower()].strip() + " ")
                else:
                    ofile.write(" Char not represented in dictionary ")
            ofile.write("  ") # after each morse word, add 2 spaces for consistency

    
    ifile.close()
    ofile.close()
    
# Declare the global variables.
    
treeRoot = Node(None, None)
treeRoot = createTree("MorseTable.txt", treeRoot)
table = buildDict("MorseTable.txt")

    
def userInterface ():
    """userInterface allows a user to easily use the other functions to translate between Morse/English."""
    
    print("Welcome to the Morse/English translator!  Type 'exit' at any time to stop translating.")
    
    while(True):# Error correction on opening files
        user_request = input("If you would like to translate from English to Morse code, type 'E2M'.  If you would like to translate from Morse code to English, type 'M2E'. ")
        while(str(user_request).lower() != "E2M".lower() and str(user_request).lower() != "M2E".lower()):
            if user_request == "exit":
                return
            user_request = input("If you would like to translate from English to Morse code, type 'E2M'.  If you would like to translate from Morse code to English, type 'M2E'. ")
        
        infile = input("Please provide the name of the input file with a .txt extension. ")
        while True:
            if infile == "exit":
                return
            try: ifile = open(infile)
            except IOError as errno:
                infile = input("Sorry, that's not a valid file name.  Enter a new file name or type 'exit' to quit. ")
                continue
            else:
                break
            
        outfile = input("Please provide the name of the output file with a .txt extension. ")
        while True:
            if outfile == "exit":
                return
            try: ofile = open(outfile)
            except IOError as errno:
                outfile = input("Sorry, that's not a valid file name.  Enter a new file name or type 'exit' to quit. ")
                continue
            else:
                break
                
        table = buildDict("MorseTable.txt")
            
        if(user_request == "E2M".lower()):
            englishToMorse(table, infile, outfile)
            print("File successfully converted.")
        
        if(user_request == "M2E".lower()):
            morseToEnglish(infile, outfile, treeRoot)
            print("File successfully converted.")

userInterface()

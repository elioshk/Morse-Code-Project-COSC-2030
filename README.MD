##### Frederick Wittman, Eli Oceanak, Josh Malone, Galen Damosso, Trevor Evenson
##### Dr. Hill
##### COSC 2030-01
##### 30 April 2019


# Morse/English Converter Data Type

## ADT Summary

This abstract data type converts text files in Morse or English into the other.  The Morse to English conversion is done using a binary tree, with the dots and dashes of Morse acting as left and right node pathways. The English to Morse is done using a simple dictionary lookup.

## Data Items and Operations

### Data Items

This steganography ADT does includes 2 global variables, a binary tree starting at a root node, and a dictionary table. These variables and other major data types used in the encoding/decoding of Morse and English files are listed below, along with their purpose:

#### infile
"infile" is the name that will be input by the user of the text file they wish to convert. "infile" should hold either morse code or english to be converted.

#### outfile
"outfile" is the file the user wishes to write the converted text to. This can be any text file, though it must be created and in the directory beforehand.

#### MorseTable
"MorseTable" is the file that holds the conversion chart for Morse and English. It is used to fill up the following items with data.

#### node
The node data type is comprised of 2 variable values, "key" and "val", where "val" is the alpha value the node holds, and "key" is the morse value.

#### treeRoot
This is the root node of an entire binary tree of english values. The tree is followed in the order of the dots and dashes, which follow the left and right children respectively

#### table
"table" is the name of the dictionary of english and morse codes. This is made in key:value pairs which works well for conversion between the two.

### Operations

#### createTree (in_file, root)
* Parameters: a text file as a read file of the Morse/English conversion table, and a root node for the base of the tree.
* Pseudocode:
  1. Opens the in_file
  2. Pulls a line from in_file
  3. Splits the line into an alpha value and a morse value
  4. Inserts a new node using the insert() function, passing the root and a new node with the alpha and morse values in it as parameters
  5. Repeats from step 2 until the file is out of usable lines
  6. Closes in_file

#### insert (root, node)
* Parameters: A root node for the binary tree, and a node to insert
* Pseudocode:
  1. Checks if the length of the morse value in the node parameter is above 1
  True:
  1. Pops off the first value of the morse value in the node
  2. If the popped character is "-", the function will create a new node as a right child the the previous and recursively call itself
  3. The same thing happens on the left node pointer if the popped character is "."
  False:
  1. Checks if the length of the morse value is 1
  2. Checks if the node on the correct side of the previous exists
  3. If it doesn't, inserts a new node on the left or right side of the previous, using either "-" or "." to decide.
     Passes the new node the alpha value
  4. if the node exists, the function changes it's alpha value to the original node paramater's alpha value.
 

#### buildDict (morseTable)
* Parameter: the "MorseTable.txt" text file
* Pseudocode:
1. Opens the morseTable txt file
2. Reads in a line from morseTable and strips the white space off of them
3. Inserts the alpha and morse values into the table global variable using key:value pairs
4. Repeats from step 2 until out of usable lines
5. Closes the morseTable txt file.

#### search (root, key)
* Parameters: root node for the binary tree for morse to english, an alpha value in "key"
* Pseudocode:
1. Checks the length of the morse value stored in the passed in node
2. If the length is 0, either returns the alpha value stored in "key" of the node, or an error message displaying there is no value to return.
3. If the length is greater than 0, pops off the first value of the morse string stored in the passed in node.
4. Depending on if the value popped was either a "." or "-", the function recursively calls itself passing in the right or left node pointer of the root paramater.

#### morseToEnglish(infile, outfile, root)
* Parameter: two text file directories, one for input and one for output, and a root node for the binary tree
* Pseudocode:
1. Opens the infile and outfile as read and write respectively
2. Goes through every line in the infile, and creates a new array and resets a counter variable each time.
3. Adds "." and "-"s to the array each time encountered
4. Writes to the outfile, using the "."s and "-"s to go through the binary tree starting at the root paramater, outputting the correct alpha value into the file.
5. Repeats from step 2 until the file is out of usable lines.

#### englishToMorse(table, infile, outfile)
* Parameter: the table variable that contains an english-morse dictionary, and two text files for input and output.
* Pseudocode:
1. Opens the infile and outfile as read and write respectively.
2. Goes through every line in the infile, converts all the characters to lowercase, and strips off whitespace to the right of each line.
3. Goes through each letter in the line, converting to morse and writing to the outfile, and writes a space if the letter is a space.

#### userInterface()
* userInterface() creates a simple mehtod for user interaction, asking whether the user would like to convert Morse to English or vice-versa. The method also will ask for input of an input and output file, which will be assumed to be in the same directory as the project. A full file directory elsewhere will also work, however.

* After finishing the conversion, the method will immediately prompt for another conversion. typing "exit" at any time will allow the user to exit the program.

## Example
Consider the the output when the following input is given:

```English to Morse is chosen: infile = "E2MTest2.txt, outfile = "output.txt"``` 

Below is a comparison of sections of the text file of the input, and the output file.

![alt text](https://github.com/frederickwittman95/Group-project-1/blob/master/photos/after_encode.PNG "Logo Title Text 1")
![alt text](https://github.com/frederickwittman95/Group-project-1/blob/master/photos/before_encode.PNG "Logo Title Text 1")

Here is the output when the encoded pixels have been decoded:

![alt text](https://github.com/frederickwittman95/Group-project-1/blob/master/photos/output.PNG "Logo Title Text 1")

## Suggestions for Improvement

* Modify the encode, decode, and ascii_to_binary functions to allow the stenography ADT to process messages with multiple lines.
* Add code to read pixels directly from, and write directly to, PNG images.

## Citation

Special thanks to jfs of stackoverflow, whose code was the inspiration for the core of the ascii_to_binary and bin_to_ascii functions.

[jfs answer](https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa)

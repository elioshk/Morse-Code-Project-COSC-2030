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
  1. 
  2. With use of an index variables to point to the appropriate pixel element and to stop reading at the end of the secret message, read through the file and add the bits that correspond to the ASCII characters to a list.
  3. Translate the bits to ASCII characters and write the secret message to the out-file.
  4. Write the length of the message in bits and the degree of overflow in bits to the out-file.

#### ascii_to_bin (message_file)
* Parameter: a text file
* ascii_to_bin reads a line from its parameter and returns the line's contents as a list of binary numbers.  The list of binary numbers corresponds to the appropriate ASCII characters.  The core of the ascii_to_bin function is the from_bytes function.

#### binary_to_ascii (binary_number)
* Parameter: a string
* binary_to_ascii takes a string of binary numbers as its parameter and returns a string of the corresponding ASCII characters.  The core of the binary_to_ascii function is the from_bytes function.

#### hex_to_bin (hex_number)
* Parameter: a string
* hex_to_bin takes a hexidecimal number, cast as a string, and returns a binary number cast as a string.

#### bin_to_hex (bin_number)
* Parameter: a string
* bin_to_hex takes a binary number, cast as a string, and returns a hexidecimal number cast as a string.

#### dec_to_hex (dec_number)
* Parameter: a string
* dec_to_hex takes a decimal number, cast as a string, and returns a hexidecimal number cast as a string.

#### hex_to_dec (hex_number):
* Parameter: a string
* hex_to_dec takes a hexidecimal number, cast as a string, and returns a decimal number cast as a string. 

## Example
Consider the the output when the following functions are called:

```encode("pixel_in.txt", "pixel_out.txt", "message_in.txt")``` 

```decode("pixel_out.txt", "message_out.txt")```

Below is a comparison of sections of the image file before and after the secret message has been encoded.  Notice that the pixel values have subtly changed in accordance with the scheme described above.  Additionally, note that the green and blue elements of the first pixel reflect the total number of bits in the message to be encoded, in this case "Dr. Hill", and the degree of overflow in bits, respectively.

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

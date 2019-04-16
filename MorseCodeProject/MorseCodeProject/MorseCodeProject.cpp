// MorseCodeProject.cpp
// Eli Oceanak, Galen Damosso, Fred Wittman, Josh Mallone, Trevor

#include "pch.h"
#include <iostream>
#include <string>

using std::string

class Node { // General Node class
	string value; // Either a letter or string of dots and dashes
	Node* left;
	Node* right;
}

void insertNode(Node* temp, Node tree) {} // Insert a Node into the tree

void createTree(string inputFile) {} // Opens input file, reads in characters and creates a tree based on the file

string promptUser() {}// Prompts the user for a filename

string findLetter(string morse) {} // Search the morse tree for a letter and input it into the file.

string findMorse(string letter) {} // Searches the english tree and spits out a morse value

string decodeEnglish(string[] morse) {} // Uses findMorse to take a string of morse letters and output it into english

string decodeMorse(string[] letters) {} // Uses findLetter to take a string of english and spit it out as morse

string[] read(string inputFile) {} // Reads a file and puts out an array of strings

void output(string outputFile) {} // Writes the output to a file.


int main()
{

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

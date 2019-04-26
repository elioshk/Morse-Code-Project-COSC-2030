// MorseCodeProject.cpp
// Eli Oceanak, Galen Damosso, Fred Wittman, Josh Mallone, Trevor

#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h> 
#include <stdio.h>   

using namespace std;

struct node { // General Node class
	string alpha; // Either a letter or string of dots and dashes
	string morse;
	struct node *left, *right;
};

struct node *nextNode(string alpha, string morse) {
	struct node *temp = (struct node*)malloc(sizeof(struct node));
	temp->alpha = alpha;
	temp->morse = morse;
	temp->left = temp->right = NULL;
	return temp;
}

struct node* insertNode(struct node *previous, string alpha, string morse) {
	if (previous == NULL) {
		return nextNode(alpha, morse);
	}
	if (int(alpha[0]) < int(previous->alpha[0])) {
		previous->left = insertNode(previous->left, alpha, morse);
	}
	else if(int(alpha[0]) >= int(previous->alpha[0])){
		previous->right = insertNode(previous->right, alpha, morse);
	}
	return previous;
} // Insert a Node into the tree

void createTree(string inputFile) {} // Opens input file, reads in characters and creates a tree based on the file

string promptUser() {
	return "";
}// Prompts the user for a filename

string findMorse(string letter) {
	return "";
} // Searches the english tree and spits out a morse value

string decodeEnglish(string morse) {
	return "";
} // Uses findMorse to take a string of morse letters and output it into english

string decodeMorse(string letters) {
	return "";
} // Uses findLetter to take a string of english and spit it out as morse

string read(string inputFile) {
	return "";
} // Reads a file and puts out an array of strings

void output(string outputFile) {
	return;
} // Writes the output to a file.


int main()
{
	cout << "Hello and welcome to the morse to english translator.\n"
		<< "Please input the name of the text file for the conversion table: ";
	string tablefile;
	cin >> tablefile;
	ifstream table;
	table.open(tablefile);
	string alpha;
	string morse;
	struct node *root = NULL;
	cout << "test";
	table >> alpha >> morse;
	cout << endl << alpha << " " << morse << endl;
	root = insertNode(root, alpha, morse);
	cout << "test";
	while (!table.eof()) {
		table >> alpha >> morse;
		insertNode(root, alpha, morse);
	}
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

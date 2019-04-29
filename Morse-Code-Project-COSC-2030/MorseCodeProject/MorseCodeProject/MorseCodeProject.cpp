// MorseCodeProject.cpp
// Eli Oceanak, Galen Damosso, Fred Wittman, Josh Mallone, Trevor

#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h> 
#include <stdio.h>   
#include <vector>

using namespace std;

struct node { // General Node class
	int *test;
	string alpha; // Either a letter or string of dots and dashes
	struct node *left, *right;
};

struct node* nextNode(string alphaVal) {
	struct node *temp = new node; // (struct node*)malloc(sizeof(struct node));
	temp->alpha = alphaVal;
	temp->left = temp->right = NULL;
	return temp;
	
}

/*struct node* insertNode(struct node *previous, string alphaVal, string morseVal) {
	if (previous == NULL) {
		return nextNode(alphaVal, morseVal);
	}
	if (int(alphaVal[0]) < int(previous->alpha[0])) {
		previous->left = insertNode(previous->left, alphaVal, morseVal);
	}
	else if(int(alphaVal[0]) >= int(previous->alpha[0])){
		previous->right = insertNode(previous->right, alphaVal, morseVal);
	}
	return previous;
}*/ // Insert a Node into the tree

struct node* insertNode(struct node *previous, string alphaVal, string morseVal) {\
	if (morseVal == "") {
		return nextNode(alphaVal);
	}
	if (morseVal[0] == '.') {
		previous->left = insertNode(previous->left, alphaVal, morseVal.substr(1));
	}
	else if (morseVal[0] == '-') {
		previous->right = insertNode(previous->right, alphaVal, morseVal.substr(1));
	}
	return previous;
}

void insertNode2(struct node *&previous, string alphaVal, string morseVal) {
		if (morseVal == "") {
			previous->alpha = alphaVal;
		}
	if (morseVal[0] == '.') {
		insertNode(previous->left, alphaVal, morseVal.substr(1));
	}
	else if (morseVal[0] == '-') {
		insertNode(previous->right, alphaVal, morseVal.substr(1));
	}
	return;
}
	
	string promptUser() {
	return "";
}// Prompts the user for a filename


/*string findMorse(string letter, node* root) {
	while (root != NULL) {
		if (root->alpha[0] == letter[0]) {
			return root->morse;
		}
		if (int(root->alpha[0]) <= int(letter[0])) {
			cout << "right\n";
			return findMorse(letter, root->right);
		}
		if (int(root->alpha[0]) > int(letter[0])) {
			cout << "left\n";
			return findMorse(letter, root->left);
		}
	}
	return "morse for " + letter + "could not be found";
}*/ // Searches the english tree and spits out a morse value

string decodeEnglish(string morse, node* root) {
	while (morse != "") {
		if (morse[0] == '-') {
			cout << "right\n";
			return decodeEnglish(morse.substr(1), root->right);
		}
		if (morse[0] == '.') {
			cout << "left\n";
			return decodeEnglish(morse.substr(1), root->left);
		}
	}
	return root->alpha;
} // Uses findMorse to take a string of morse letters and output it into english

string decodeMorse(string word, string morse[], string alpha[]) {
	int ct = word.length();
	string temp = "";
	for (int j = 0; j < ct; j++) {
		for (int i = 0; i < 100; i++) {
			if (alpha[i] == word.substr(0, 1)) {
				temp += morse[i];
				temp += " ";
			}
		}
		word = word.substr(1);
	}
	temp += "   ";
	return temp;
} // Uses findLetter to take a string of english and spit it out as morse

string read(string inputFile) {
	return "";
} // Reads a file and puts out an array of strings

void output(string outputFile) {
	return;
} // Writes the output to a file.



void inorder(struct node *root)
{
	if (root != NULL)
	{
		inorder(root->left);
		cout << root->alpha << endl;
		inorder(root->right);
	}
}

void swap(string *xp, string *yp)
{
	string temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void bubbleSort(string arr[], int n)
{
	int i, j;
	for (i = 0; i < n - 1; i++)
		// Last i elements are already in place    
		for (j = 0; j < n - i - 1; j++)
			if (arr[j].length() > arr[j + 1].length())
				swap(&arr[j], &arr[j + 1]);
}

int main()
{
	cout << "Hello and welcome to the morse to english translator.\n"
		<< "Please input the name of the text file for the conversion table: ";
	string tablefile;
	cin >> tablefile;
	ifstream table;
	table.open(tablefile);
	string alphaVal;
	string morseVal;
	struct node *root = new node;
	string morsetable[100];
	string alphatable[100];
	int ct = 0;
	while (!table.eof()) {
		table >> alphaVal >> morseVal;
		alphatable[ct] = alphaVal;
		morsetable[ct] = morseVal;
		for (int i = 0; i < morseVal.length(); i++) {
			insertNode(root, alphaVal, morseVal.substr(0,i));
		}
		//cout << alphaVal;
		ct++;
	}
	cout << "test" << endl;
	table.close();
	table.open(tablefile);
	while (!table.eof()) {
		table >> alphaVal >> morseVal;
		insertNode2(root, alphaVal, morseVal);
		cout << alphaVal << endl;
		ct++;
	}
	ct = 0;
	//cout << decodeEnglish(test, root) << endl;
	return 0;
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

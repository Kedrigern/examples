/* Atuhor: Ondřej Profant
 * Year: 2010
 * email: ondrej.profant at gmail.com
 */

#include <stdlib.h>
#include <iostream>
#include <queue>
#include <list>
#include <string>
#include <sstream>

#include "rbTreePublic.h"
#include "rbTreePrivate.h"
#include "node.h"

using namespace std;

void treeTest( void );
void test( void );

int main(int argc, char * argv[] ) {

	treeTest( ) ;
 
 return 0;
}

void treeTest( ) {
	string log;
	RBtree< int > t( 9 );
	char choice;
	int key;
	t.insert( 5 );
	t.insert( 15 );

	while( true ) {
		system("clear");
		stringstream tmp;
		
		cout << "----------------------------------------" << endl;
		cout << "Vyberte možnost:\n 1) Insert\t2) Find \t3) Succ \t4) Pred\t5) MinMax \t6)Del \t7) Sada testů\tx) Konec\n----------------------------------------" << endl;
		cout << "Poslední akce: " << log << endl;
		cout << "Počet prvků: " << t.size() << endl;
		cout << "----------------------------------------" << endl;
		cout << "Strom inorder: "; t.print();
		cout << "Level-order: "; t.print(3);
		cout << "----------------------------------------" << endl;
		cout << "Možnost: "; cin >> choice;
		log="";
		switch( choice ) {
			case '1':
			case 'i':
			case 'I':
				cout << "Insert: ";
				cin >> key;
				t.insert( key );
				tmp << "Insert: " << key;
				log += tmp.str();
				break;
			case '2':
			case 'f':
			case 'F':
				cout << "Find: ";
				cin >> key;
				tmp << "find(" << key << ") = " ;
				log += tmp.str();
				if( t.find( key ) ) log += "true";
				else log += "false";
				break;
			case '3':	
			case 's':
			case 'S':
				cout << "Succ: ";
				cin >> key;
				cout << "tu";
				tmp << "succ(" << key << ") = " << t.succ( key ) ;
				log += tmp.str();
				break;	
			case '4':
			case 'p':
			case 'P':
				cout << "Pred: ";
				cin >> key;
				tmp << "pred(" << key << ") = " << t.pred(key) ;
				log += tmp.str();
				break;
			case '5':
			case 'm':
			case 'M':
				tmp << "min: " << t.min() << " max: " << t.max() ;
				log = tmp.str();
				break;
			case '6':
			case 'd':
			case 'D':	
				cout << "[NONE] Delete: ";
				cin >> key;
				t.erase( key );
				tmp << "Delete: " << key;
				log = tmp.str();
				break;
			case '7':
			case 't':
			case 'T':
				test();
			default :
				return;
		}
	}
}

void test() {
cout << "TEST 1\nSestavím: " << endl << 
"    6" << endl <<
"   / \\" << endl <<
"  4   8" << endl;
RBtree<int> t( 6 );
t.insert( 4 );
t.insert( 8 );
t.print();
cout << "Červené uzly mají kolem sebe dvojtečky. Vkládám 7." << endl;
t.insert( 7 );
t.print();

cout << "---------------" << endl;

cout << "\nTEST 2\nSestavime:\n" <<
"       D           7                     3 \n" <<
"      /           /  	                / \\ \n" <<
"     O           3     Má vzniknout:   1   7\n"<<
"    /           /   \n" <<
"   New         1   \n" <<
"D černý, O a New červené.\n";
RBtree<int> t2( 7 );
t2.insert( 3 );
t2.print();
t2.insert( 1 );
t2.print();
cout << "---------------" << endl;

cout << "\nTEST 2b\nSestavime to samé, ale uzel budu připojovat zprava (přidám 4)\n";
RBtree<int> t2b( 7 );
t2b.insert( 3 );
t2b.print();
t2b.insert( 4 );
t2b.print();
cout << "---------------" << endl;

cout << "\nTEST 3\nSestavime:\n" <<
" D      2   \n" <<
"  \\      \\  \n" <<
"   O      5  \n" <<
"    \\      \\  \n" <<
"    New     6 \n";
RBtree<int> t3( 2 );
t3.insert( 5 );
t3.print();
t3.insert( 6 );
t3.print();
cout << "---------------" << endl;

cout << "\nTEST 3b\nSestavime to samé, ale uzel budu připojovat zprava (přidám 4)\n";
RBtree<int> t4( 2 );
t4.insert( 5 );
t4.print();
t4.insert( 4 );
t4.print();
cout << "---------------" << endl;
}
 

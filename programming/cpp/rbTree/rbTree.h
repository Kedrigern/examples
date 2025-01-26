/* Atuhor: Ondřej Profant
 * Year: 2010
 * Email: ondrej.profant at gmail.com
 * About: Headers file of data structure red-black tree.
 * 				Implementation is in 2 files - rbTreePublic.h and rbTreePublic.h (.h because include templates)
 */

#ifndef _rbTREE_H
#define _rbTREE_H
#include "node.h"

template<class T>
class RBtree {
private:	
	void leftRotation(Node<T> *);

	void rightRotation(Node<T> *); 

	void deleteCase1( Node<T> * );

	void deleteCase2( Node<T> * );

	void deleteCase3( Node<T> * );

	void deleteCase4( Node<T> * );

	void deleteCase5( Node<T> * );

	void deleteCase6( Node<T> * );

	void swapValue( Node<T>* , Node<T>* );

	void swapBnodeRleaf( Node<T>*, Node<T>* );

	void insertRepair( Node<T> * );

	Node<T> * sourozenec( Node<T> *);

	Node<T> * findIt( int ); 
	
	Node<T> * predP( int);
	
	void delet( Node<T>* );
	
public:
	Node<T> * root;
	
	int count;
	
	RBtree( int i );
	~RBtree( );

  Node<T> * succP( int);

	bool empty( );
	
	int erase( int );

	void clear();
	
	void insert( int );

	bool find( int );

	void print();

	void print( int );

	int size();
	
	int succ( int );
	
	int pred( int );
	
	int max( void );
	
	int min( void );
};
#endif

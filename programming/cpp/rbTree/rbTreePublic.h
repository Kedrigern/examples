/* Atuhor: Ondřej Profant
 * Year: 2010
 * email: ondrej.profant at gmail.com
 */

#ifndef _rbTREEpub_CPP
#define _rbTREEpub_CPP

#include "node.h"
#include "rbTree.h"

template<class T>
RBtree< T >::RBtree( int i ) {
		root = new Node< T >( i );
		count = 1;
		root->cerveny = false;
}

template<class T>
RBtree< T >::~RBtree( ){
		this->root->delRecursivly();
		delete this->root;
	}

template<class T>	
void RBtree<T>::insert( int key ) {
		if( count == 0 ) {
			this->root = new Node<T>( key );
			this->root->cerveny = false;
			this->count = 1;
			return;
		}

		Node<T> *papa = findIt( key );
		Node<T> *newN;

		if( papa->key.first == key ) return; 	// item is alredy in this structure
		else {
			++count;
			if( key < papa->key.first ) {
				papa->lSon = new Node<T>( key );
				papa->lSon->parent = papa;
				newN=papa->lSon;
			}	else {
				papa->rSon = new Node<T>( key );
				papa->rSon->parent = papa;
				newN=papa->rSon;
			}
		}

		/* repar Red-Black structure */
		insertRepair( newN );
}

template<class T>
int RBtree<T>::size() {
	return count;
}

template<class T>
int RBtree<T>::erase( int key ) {
	if( count == 0) return 0;

	Node<T>* del = findIt( key );

	if( del == NULL ) return 0;
	if( del->key.first != key ) return 0;
	if( count == 1 && root->key.first == key ) {
		count = 0;
		this->root = NULL;
		delete del;
	}
	
	--count;
	
	delet( del );

	return 1;
}

template<class T>
bool RBtree<T>::empty( ) {
	if( count == 0 ) return true;
	else return false;
}

template<class T>
void RBtree<T>::clear() {
	root->delRecursivly();
	delete root;
	count = 0;
}

template<class T>
int RBtree<T>::min() {
		Node<T>* tmp = this->root;
		while( tmp->lSon != NULL ) 
		{ tmp = tmp->lSon;}
		
		return tmp->key.second;
	}

/*
template<class T>
Iterator<T> RBtree<T>::begin() {
	Node<T>* tmp = this->root;
	while( tmp->lSon != NULL ) 
		{ tmp = tmp->lSon;}
		
	return Iterator<T>( tmp );
}*/

template<class T>
int RBtree<T>::max() {
		Node<T>* tmp = this->root;
		while( tmp->rSon != NULL ) 
		{ tmp = tmp->rSon;}
		
		return tmp->key.second;
}

/*
template<class T>
Iterator<T> RBtree<T>::end() {
	return Iterator<T>( NULL );
}
*/
#endif

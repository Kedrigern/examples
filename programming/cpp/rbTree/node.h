/* Atuhor: Ondřej Profant
 * Year: 2010
 * Email: ondrej.profant at gmail.com
 * About: Node in data structures tree. Some basic functions (like recursivly print in somes traversals).
 */

#ifndef _NODE_H
#define _NODE_H
#include <utility>
#include <iostream>

template<class T>
struct Node {
 Node<T> *parent, *lSon, *rSon;
 bool cerveny;

 std::pair<int ,T > key;

 Node( int );
 
 void delRecursivly();

 void print();
 
 void printInOrder();
 
 void printPreOrder();
 
 void printPostOrder();
};

template<class T>
Node<T>::Node( int i ) {
	/* here will be some sofisticated funkction value -> key */
		key = std::make_pair( i, i );
		parent = NULL;
		lSon = NULL;
		rSon = NULL;
		cerveny = true; 
 }


template<class T>
void Node<T>::delRecursivly() {
	  if( lSon != NULL ) { 
			lSon->delRecursivly();
			delete lSon;
		}
	  if( rSon != NULL ) {
		  rSon->delRecursivly();
		  delete rSon;
	  }
}


template<class T>
void Node<T>::print() {
  std::cout << "[value: " << key.second;
  if( parent == NULL ) std::cout << " non ]" << std::endl;
  else std::cout << " otec value: " << parent->key.second << " ]" << std::endl;
 }


template<class T>
void Node<T>::printInOrder() {
	if( this->lSon != NULL ) { this->lSon->printInOrder() ; }

	if( this->cerveny ) std::cout << "\e[1;31m" << this->key.second << "\e[0m ";
	else 	std::cout << this->key.second << ' ';
	 
	if( this->rSon != NULL ) { this->rSon->printInOrder() ; }

	 return;
 }


template<class T>
void Node<T>::printPreOrder() {
	std::cout << this->key.second << ' ';	
	 
	if( this->lSon != NULL ) { this->lSon->printPreOrder() ; }
	 
	if( this->rSon != NULL ) { this->rSon->printPreOrder() ; }

	return; 
 }


template<class T>
void Node<T>::printPostOrder() {
	if( this->lSon != NULL ) { this->lSon->printPostOrder() ; }

	if( this->rSon != NULL ) { this->rSon->printPostOrder() ; }

	std::cout << this->key.second << ' ';

	return;
 }
#endif

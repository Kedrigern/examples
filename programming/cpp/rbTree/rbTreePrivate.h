/* Atuhor: Ondřej Profant
 * Year: 2010
 * email: ondrej.profant at gmail.com
 */

#ifndef _rbTREEpri_CPP
#define _rbTREEpri_CPP
#include <iostream>
#include <queue>
#include <list>

#include "node.h"
#include "rbTree.h"

template<class T>
void RBtree<T>::insertRepair( Node<T> * newN ) {

		if( ! newN->parent->cerveny ) return;	// everything is ok

		bool IamLeft;
		Node<T>* papa = newN->parent;
		if( papa->lSon == newN ) { IamLeft = true; }
		else IamLeft = false;
		Node<T> *grandpa = papa->parent;			// must exists because root is black node;
		Node<T> *uncle;
		
		if( papa == grandpa->rSon ) uncle = grandpa->lSon;		// maybe NULL
		else uncle = grandpa->rSon;
		
		/* first case: uncle is red, not matter on my position to father */
		if( uncle != NULL && uncle->cerveny ) {
			grandpa->cerveny = true;
			uncle->cerveny = false;
			papa->cerveny = false;
			root->cerveny = false;

			if( grandpa->parent != NULL && grandpa->parent->cerveny ) {
				insertRepair( grandpa );
			}
			return;
		}
		

		 /* second case: we can modifikate to third case
		 * uncle is black
		 * linie grandpa-papa-newN is not linear*/
		if( (! 	IamLeft && grandpa->lSon == papa ) ||
				(		IamLeft && grandpa->rSon == papa ) )
			{
			if( grandpa->lSon == papa) {
				leftRotation( papa ); 
			} else {
				rightRotation( papa ) ;
			}

			IamLeft = ! IamLeft;
		} 
		
		/* third case: we rotate the tree
		 * Hang papa to grandpa->parent */
		if( grandpa->parent == NULL ) { // is grandpa root?
			papa->parent = NULL;
			this->root = papa;
		} else {
			if( grandpa->parent->lSon == grandpa ) {
				grandpa->parent->lSon = papa;
			} else grandpa->parent->rSon = papa;
		}
		grandpa->parent = papa;

		if( IamLeft ) {
			grandpa->lSon = papa->rSon;
			if( papa->rSon != NULL ) papa->rSon->parent = grandpa;
			papa->rSon = grandpa;
		} else {
			grandpa->rSon = papa->lSon;
			if(grandpa->rSon != NULL ) grandpa->rSon->parent = grandpa;
			papa->lSon = grandpa;
		}

		newN->cerveny = true;
		papa->cerveny = false;
		grandpa->cerveny = true;
		if(uncle != NULL) uncle->cerveny = false;
		root->cerveny = false;
  }

template<class T>
bool RBtree<T>::find( int key) {
		if( (findIt( key ))->key.first == key ) return true;
		else return false;
  }

	 /* Print all tree
	  * 
	  * argument:
	  * 	0 inorder
	  * 	1 postorder
	  *   2 preorder
	  *   3 level-order
	  */
template<class T>
void RBtree<T>::print() {
	RBtree::print( 0 );
}

template<class T>
void RBtree<T>::print( int how ) {
		if( root == NULL ) {
			std::cout << "_|_" << std::endl;
			return;
		}
		
		switch( how ) {
		case 0:	
			root->printInOrder();
			break;
		case 1:
			root->printPostOrder();
			break;
		case 2:
			root->printPreOrder();
			break;
		case 3:
			std::cout << std::endl;
			std::queue<Node<T>*> myFifo;
			std::queue<int> breaks;
			Node<T>* tmp = this->root;
			
			/* breaks */
			breaks.push( tmp->key.second );
			while( true ) {
				if( tmp->rSon != NULL) tmp = tmp->rSon;
				else { 
					if( tmp->lSon != NULL ) tmp = tmp->lSon;
					else break; 
				} 
				breaks.push( tmp->key.second );
			}
			
			/* level order */
			tmp = this->root;
			myFifo.push( tmp );
			while( myFifo.size() > 0 ) {
				tmp = myFifo.front();
				myFifo.pop();	
				
				if( tmp->cerveny ) std::cout << "\e[1;31m";
				std::cout << tmp->key.second << "\e[0m ";
				if(tmp->key.second == breaks.front() ) { std::cout << std::endl; breaks.pop(); }
				
				if(tmp->lSon != NULL) myFifo.push( tmp->lSon );
				if(tmp->rSon != NULL) myFifo.push( tmp->rSon );
			}
			break;
		}
		std::cout << std::endl;
	}

	/* succesor of value i in set represented by the tree */
template<class T>
int RBtree<T>::succ( int i ) {
		Node<T> * f = succP( i );
		if( f != NULL ) return succP( i )->key.second;
		else return 0;
	}

	template<class T>
int RBtree<T>::pred( int i ) {
		Node<T> * f = predP( i );
		if( f != NULL ) return predP( i )->key.second;
		else return 0; // TODO: better indication of error
	}

template<class T>
void RBtree<T>::swapBnodeRleaf( Node<T>* p , Node<T>* c) {
	if( p == NULL || c == NULL ) return;

	c->parent = p->parent;
	if( c->parent != NULL ) {
		if( c->parent->lSon == p ) c->parent->lSon = c;
		else c->parent->rSon = c;
	}
	p->parent = c;
	p->lSon = NULL;
	p->rSon = NULL;

	if( p->key.first < c->key.first ) { c->lSon = p; }
	else c->rSon = p;

	c->cerveny = false;
	p->cerveny = true;
}

template<class T>
void RBtree<T>::leftRotation(Node<T>* b) {
		if( b == NULL ) return;
		if( b->lSon == NULL ) return;
		if( b->rSon == NULL ) return;
		
		Node<T>* a = b->lSon;
		Node<T>* c = b->rSon;
		
		/* hag the C */
		c->parent = b->parent;
		if( c->parent != NULL ) {
			if(c->parent->lSon == b ) c->parent->lSon=c;
			else c->parent->rSon = c;
		}
		
		/* hag the B */	
		b->parent = c;

		b->lSon = a;
		a->parent = b;
		
		b->rSon = c->lSon;
		if( b->rSon != NULL ) b->rSon->parent = b;
			
		c->lSon = b;
		if( c->parent == NULL ) this->root = c;
	}

template<class T>
void RBtree<T>::rightRotation(Node<T>* b) {
		if( b == NULL ) return;
		if( b->lSon == NULL ) return;
		if( b->rSon == NULL ) return;	
		
		Node<T>* a = b->lSon;
		Node<T>* c = b->rSon;
		
		/* hag the A */
		a->parent = b->parent;
		if( a->parent != NULL ) {
			if( a->parent->lSon == b ) a->parent->lSon = a;
			else a->parent->rSon = a;
		} else {
			this->root = a;
		}
		
		/* hag the B */
		b->parent = a;
		
		b->rSon = c;
		c->parent = b;
		
		b->lSon = a->rSon;
		if( b->lSon != NULL ) b->lSon->parent = b;
		
		a->rSon = b;
	}

template<class T>
void RBtree<T>::delet( Node<T>* del ) {
		int key = del->key.first;
		Node<T>* a;

		/* root */
		if( del->rSon == NULL && del->lSon == NULL && del->parent == NULL) {
			root = NULL;
			count = 0;
			return;
		}
		
		/* Generaly interior - swap value to leaf and them delete these leaf */
		/* 2 children */
		if( ( (del->rSon) != NULL ) && ( (del->lSon) != NULL ) ) {
			a = succP( key );
			if( a == NULL ) a = predP( key );

			swapValue( a, del );
		} else {
			a = del;
		}

	
		
		bool IamLeft;
		if( a->parent != NULL ) {
			if( a->parent->lSon == a ) IamLeft = true;
			else IamLeft = false;
		};
		
		/* red "leaf" - delete is ok */
		if( a->cerveny ) {
			
			/* A is leaf */
			if( a->lSon == NULL && a->rSon == NULL ) {
				
				if( IamLeft ) a->parent->lSon = NULL;
				else a->parent->rSon = NULL;
				
				delete a;
				return;
			}
		}

		Node<T> * child;
		if( a->lSon != NULL && a->rSon == NULL ) child = a->lSon;
		else child = a->rSon;

		/* black node with red son, I can replace */
		if(child != NULL) {
		if( ! a->cerveny && child->cerveny ) {
			swapValue( child, a );
			if( a->lSon == child ) a->lSon = NULL;
			else a->rSon = NULL;
			delete child;
			return;
		} }

		Node<T>* s = sourozenec( a );
		if( s != NULL ) {
			if( IamLeft && s->lSon != NULL && s->lSon->cerveny && s->rSon == NULL) {
				 swapBnodeRleaf( s , s->lSon );
			}
			if( !IamLeft && s->rSon != NULL && s->rSon->cerveny && s->lSon == NULL ) {
				 swapBnodeRleaf( s, s->rSon );
			}
		}

		deleteCase1( a );

		if( a->parent != NULL ) {
			if( a->parent->lSon == a ) a->parent->lSon = NULL;
			else a->parent->rSon = NULL;
		}
		
		delete a;
		return;
	}

template<class T>
void RBtree<T>::deleteCase1( Node<T>* a) {
	if( a->parent != NULL ) {
		deleteCase2( a );
	}
}

template<class T>
void RBtree<T>::deleteCase2( Node<T>* a) {
	Node<T> *b = sourozenec( a );
	
	if( b->cerveny ) {
		a->parent->cerveny = true;
		b->cerveny = false;
		if( a == a->parent->lSon )
			leftRotation( a->parent );
		else
			rightRotation( a->parent );
	}
	deleteCase3( a );
}

template<class T>
void RBtree<T>::deleteCase3( Node<T>* a) {
	Node<T> *b = sourozenec( a );
	if( b == NULL ) {
			return;
	}
	
	if(	( ! a->parent->cerveny ) &&		// father black
			( ! b->cerveny ) &&						// brother black
			(
				( b->lSon == NULL ) ||
				( ! b->lSon->cerveny )
			)	&&
			(
				( b->rSon == NULL ) ||
				( ! b->rSon->cerveny )
			)
		) {
		b->cerveny = true;
		deleteCase1( a->parent );
	} else
		deleteCase4( a );
}

template<class T>
void RBtree<T>::deleteCase4( Node<T>* a) {
	if( a->parent == NULL) { /*TODO*/ }
	
	Node<T> *b = sourozenec( a );
	
	if(	( a->parent->cerveny ) &&
			( ! b->cerveny ) &&
			( ! b->lSon->cerveny ) &&
			( ! b->rSon->cerveny )
		) {
		b->cerveny = true;
		a->parent->cerveny = false;
	} else
		deleteCase5( a );
}

template<class T>
void RBtree<T>::deleteCase5( Node<T>* a) {
	if( a->parent == NULL) { /*TODO*/ }
	
	Node<T> *b = sourozenec( a );
	
	if( ! b->cerveny &&
				b->lSon != NULL &&
				b->rSon != NULL ) {
		if( 	(a == a->parent->lSon) &&
				(! b->rSon->cerveny) &&
				(  b->lSon->cerveny)
			) {
				b->cerveny = true;
				b->lSon->cerveny = false;
				rightRotation( a );
			} else if( 	(a == a->parent->rSon) &&
						(! b->lSon->cerveny ) &&
						( b->rSon->cerveny ) 
					) {
							b->cerveny = true;
							b->rSon->cerveny = false;
							leftRotation( a );
			}
	}
	deleteCase6( a );
}

template<class T>
void RBtree<T>::deleteCase6( Node<T>* a) {
	if( a->parent == NULL) { /*TODO*/ }
	
	Node<T> *b = sourozenec( a );
	
	b->cerveny = a->parent->cerveny;
	a->parent->cerveny = false;
	
	if( a == a->parent->lSon ) {
		b->rSon->cerveny = false;
		leftRotation( a->parent );
	} else {
		if( b->lSon != NULL ) b->lSon->cerveny = false;
		if( b->rSon != NULL ) b->rSon->cerveny = false;
		rightRotation( a->parent );
	}
}

template<class T>
void RBtree<T>::swapValue( Node<T>* a, Node<T>* b) {
	int tmp = a->key.first;
	T tmp2 = a->key.second;
	a->key.first = b->key.first;
	a->key.second = b->key.second;
	b->key.first = tmp;
	b->key.second = tmp2;
}

template<class T>
Node<T> * RBtree<T>::sourozenec( Node<T> * x ) {
	if( x->parent != NULL ) {
		if( x->parent->lSon == x ) return x->parent->rSon;
		else return x->parent->lSon;
	} else return NULL;
}

//private find, return pointer to the node or to father of it postion
template<class T>
Node<T> * RBtree<T>::findIt( int key ) {	
   Node<T> * aktual = root; // reference

   while( aktual->key.first != key ) {
      if( key < aktual->key.first ) {
				if( aktual->lSon == NULL ) break;
				else aktual = aktual->lSon;
      }
      else {
				if( aktual->rSon == NULL ) break;
				else aktual = aktual->rSon;
      }
    }	
   return aktual;
}

template<class T>
Node<T> * RBtree<T>::succP( int key ) {
	Node<T>* aktual = findIt( key );
	bool IamLeft;

	if( aktual->rSon != NULL ) {
		aktual = aktual->rSon;
		while( aktual->lSon != NULL ) { 
			aktual = aktual->lSon; }
		return aktual;
	} else {
		if( aktual->parent != NULL ) {
			if( aktual->parent->lSon == aktual ) { IamLeft = true; }
			else { IamLeft = false; }
		} else return NULL;
		
		if( IamLeft ) return aktual->parent;
		else {
			while( aktual->parent->rSon == aktual ) {
				aktual = aktual->parent;
				if( aktual->parent == NULL) break;
			}
		}
		return aktual->parent;
	}
}

template<class T>
Node<T> * RBtree<T>::predP( int key ) {
	
		Node<T>* aktual = findIt( key );
		bool IamLeft;
		
		if( aktual->lSon != NULL ) {
			aktual = aktual->lSon;
			while( aktual->rSon != NULL ) {
				aktual = aktual->rSon; }
			return aktual;
		}
		else {
			if( aktual->parent != NULL ) {
				if( aktual->parent->lSon == aktual ) IamLeft = true;
				else IamLeft = false;
			} else return NULL;
			
			if(!IamLeft) return aktual->parent;
			else
				aktual = aktual->parent;
				while( aktual->parent->rSon == aktual ) {
					aktual = aktual->parent;
					if( aktual->parent == NULL) break;
			}
			if( aktual->key.second > key ) return NULL;
			return aktual;
		}
	}


#endif

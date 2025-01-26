
#include <mutex>
#include <iostream>
#include "resourcePool.h"

ResourcePool::ResourcePool(int count) : forks(count, true) {}

int ResourcePool::getAvailableFork() {
	fork_mutex.lock();
	for(int i=0; i < (int) forks.size(); i++) {
		if(forks[i]) {
			fork_mutex.unlock();
			forks[i] = false;
			return i+1;
		}
	}
	fork_mutex.unlock();
	return 0;
}

int ResourcePool::getFork(int fork) {
	if( forks.size() < (size_t) fork && fork < 0) {
		return 0; // TODO throw exception
	}
	fork_mutex.lock();
	int result = forks[fork-1] ? fork : 0;
	fork_mutex.unlock();
	return result;
}

bool ResourcePool::isFree(int fork) {
	return forks[fork-1];
}

void ResourcePool::returnFork(int fork) {
    if(fork == 0 ) return;
    if( forks.size() < (size_t) fork) return;  // TODO throw exception

    fork_mutex.lock();
    forks[fork-1] = true;
    fork_mutex.unlock();
}


void ResourcePool::restart(void) {
	forks.assign(forks.size(), true);
}

size_t ResourcePool::size() {
	return forks.size();
}

size_t ResourcePool::numberOfUsedForks() {
	int result = 0;
	for(bool b: forks) {
		if(!b) ++result;
	}
	return result;
}

size_t ResourcePool::numberOfFreeForks() {
	return forks.size() - numberOfUsedForks();
}

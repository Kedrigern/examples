#ifndef RESOURCE_POOL_H
#define RESOURCE_POOL_H

#include <mutex>
#include <vector>
#include <cstddef>

/**
 * Very simple resource pool.
 * Resources are just number.
 */
class ResourcePool {
	std::vector<bool> forks;

public:
	std::mutex console;
	std::mutex fork_mutex;

        /**
         * @param count initial number of forks (resources)
         */
	ResourcePool(int count = 5);

        /**
         * @return fork (resource, represents by number) or 0 if there isn't free forks
         */
	int getAvailableFork(void);

        /**
         * @param fork
         * @return fork (resource, represents by number) or 0 if the fork isn't free
         */
	int getFork(int fork);

	bool isFree(int fork);

	void returnFork(int fork);

	void restart(void);

	size_t size();

	size_t numberOfUsedForks();

	size_t numberOfFreeForks();
};

#endif

#ifndef GLOBAL_LOGIC_H
#define GLOBAL_LOGIC_H

#include <iostream>
#include <vector>
#include <thread>

#include "philosopher.h"

/**
 * Antipatern class hold the app logic.
 */
class globalLogic {
	/** Constants **/
	const size_t defaultResources = 5;
	const size_t defaultPhilosophers = 5;

	/** Variables **/
	ResourcePool* p_rp;
	std::vector<Philosopher> p_philosophers;

public:
	globalLogic();

        /**
         * @param philosophers  number of philosophers
         * @param resources     number of resources
         * @param timeToDie     how long philosopher can starve
         * @param delay         delay start of simulation
         */
        globalLogic(int philosophers, int resources, int timeToDie, bool delay = false, bool polite = false);

        ~globalLogic(void);

	bool restartAll(void);

	void run(void);

        std::string toString(void);
};


#endif

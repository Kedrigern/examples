#ifndef PHILOSOPHER_H
#define PHILOSOPHER_H

#include <string>
#include <vector>
#include <iostream>
#include <ctime>

#include "resourcePool.h"

/**
 * Sets of events for notice about state
 */
enum Events {
    ready,
    getFirst,
    getSecond,
    getThird,
    getAnother,
    dying
};

class Waiter;

/**
 * @author Ondřej Profant
 *
 * Represents eating philosophers who need two forks (resources) to be satisfied.
 *
 * Implements more strategies how to solve problem of dining philosophers
 * {@link http://en.wikipedia.org/wiki/Dining_philosophers_problem}.
 * Forks (resources) are managed by {@code ResourcePool}
 */
class Philosopher {
        const int waitingTime = 2;

	std::string name;
	int timeToDie = 3;
        int timeToDieMax = 3;
        bool returnFork = false;
        bool initialDelay = false;

        /**
         * static is very important for sharing this source between threads
         */
        static ResourcePool* p_rp;
public:
	Philosopher(void);

	std::string getName(void);

	void setName(std::string name);

	void setInitialDelay(bool initialDelay = true);

	void setReturnFork(bool returnFork = true);

	void setTimeToDie(int time);

	void setResourcePool(ResourcePool* rp);

	std::string toString(void);

	/**
	 * Restart class to default state
	 */
	void restart(void);

	/**
	 * Run the simulation
	 */
	void operator() (void);

private:
        /**
         * Returns unique name for philosopher. Name is unique in program (across threads)
         */
	std::string getUniqueName(void);

        /**
         * Help function. Say information about state of philosopher. Is thread safety.
         * @param event         some predefined events
         * @param negation      say negation
         */
        void say(Events event, bool negation = false);
};


#endif

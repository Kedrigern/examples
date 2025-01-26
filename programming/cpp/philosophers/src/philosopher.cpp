
#include <thread>
#include <mutex>
#include <chrono>
#include <iostream>
#include <sstream>

#include "philosopher.h"

using namespace std;

ResourcePool* Philosopher::p_rp;

Philosopher::Philosopher(void) {
    name = this->getUniqueName();
}

string Philosopher::getName(void) {
    return name;
}

void Philosopher::setName(string name) {
    name = name;
}

void Philosopher::setInitialDelay(bool initialDelay) {
    this->initialDelay = initialDelay;
}

void Philosopher::setReturnFork(bool returnFork) {
    this->returnFork = returnFork;
}

void Philosopher::setTimeToDie(int time) {
    timeToDieMax = time;
    timeToDie = time;
}

string Philosopher::toString(void) {
    stringstream ss;
    ss << "Philosopher {" << endl
        << "\tname: " << getName() << endl
        << "\ttimeToDie: " << this->timeToDie << endl
        << "\tinitial delay: " << (this->initialDelay ? "true" : "false") << endl
        << "\tpolite (return fork): " << (this->returnFork ? "true" : "false") << endl
        << "\tRP size: " << this->p_rp->size()
#if DEBUG
        << " (adress: " << this->p_rp << ")" << endl
        << "\taddress: " << this
#endif
            << endl
        << "}" << endl;
    return ss.str();
}

string Philosopher::getUniqueName() {
    static int counter = -1;
    static vector<string> names = {"Aristoteles", "Bacon", "Comte", "Descartes", "Epikuros", "Fichte", "Gödel"};

    if (counter < (int) names.size()) {
        counter++;
        return names[counter];
    } else {
        return "Anonym";
    }
}

void Philosopher::setResourcePool(ResourcePool* rp) {
    Philosopher::p_rp = rp;
}

void Philosopher::restart(void) {
    timeToDie = timeToDieMax;
    initialDelay = false;
    returnFork = false;
}

void Philosopher::operator() (void) {
    int resource1 = 0;
    int resource2 = 0;

    if (initialDelay) {
        this_thread::sleep_for(chrono::seconds(waitingTime*3));
    }

    while (timeToDie > 0) {
        if (!resource1) {

            resource1 = p_rp->getAvailableFork();

            say(getFirst, resource1 == 0);

            this_thread::sleep_for(chrono::seconds(waitingTime));
        }

        if (!resource2) {
            resource2 = p_rp->getAvailableFork();
            say(getSecond, resource2 == 0);

            this_thread::sleep_for(chrono::seconds(waitingTime/2));
        }

        if (resource1 && resource2) {
            break;
        }
        --timeToDie;
    }
    if (resource1 && resource2) {
        say(dying, true);
    } else {
        say(dying);
    }

    if(returnFork) {
        p_rp->returnFork(resource1);
        p_rp->returnFork(resource2);
    }
}

void Philosopher::say(Events event, bool negation) {
    p_rp->console.lock();
    cout << getName() << ": ";
    switch (event) {
        case ready:
            cout << "Jsem pripraven";
            break;
        case getFirst:
            cout << (negation ? "ne" : "") << "mam prvni vidlicku.";
            break;
        case getSecond:
            cout << (negation ? "ne" : "") << "mam druhou vidlicku.";
            break;
        case getThird:
            cout << (negation ? "ne" : "") << "mam treti vidlicku.";
            break;
        case dying:
        default:
            if(negation) {
                cout <<  "SUCCCESS Jsem syty, timeToDie byl: " << timeToDie;
            } else {
                cout <<  "FAIL Umiram hlady";
            }
            break;
    }
    cout << endl;
    p_rp->console.unlock();
}

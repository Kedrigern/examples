#include "globalLogic.h"
#include "philosopher.h"
#include <sstream>

using namespace std;

globalLogic::globalLogic() : p_philosophers( defaultPhilosophers ) {
        p_rp = new ResourcePool( defaultResources );
        for(Philosopher p: p_philosophers) {
            p.setResourcePool(p_rp);
        }
}

globalLogic::globalLogic(int philosophers, int resources, int timeToDie, bool delay, bool polite)
: p_philosophers( philosophers ) {
        p_rp = new ResourcePool( resources );

        for(size_t i = 0; i < p_philosophers.size(); ++i) {
            p_philosophers[i].setTimeToDie(timeToDie);
            p_philosophers[i].setResourcePool(p_rp);
            if(polite) {
                p_philosophers[i].setReturnFork();
            }
        }
        if( delay ) {
                p_philosophers[0].setInitialDelay();
        }
}

globalLogic::~globalLogic() {
        p_philosophers.clear();
        delete p_rp;
}

bool globalLogic::restartAll(void) {
        p_rp->restart();
        for(Philosopher p: p_philosophers) {
            p.restart();
        }
        return false;
}

void globalLogic::run(void) {

    cout << "Creating 1 resource pool with " << p_rp->size() << " forks." << endl;

    cout << "Creating " << p_philosophers.size() << " philosophers. Names: ";
    for(Philosopher p : p_philosophers) {
            cout << p.getName() << ", ";
    }
    cout << endl << endl;

    if( p_philosophers.size() >= 5 ) {
        thread t1(p_philosophers[0]);
        thread t2(p_philosophers[1]);
        thread t3(p_philosophers[2]);
        thread t4(p_philosophers[3]);
        thread t5(p_philosophers[4]);

        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();
     }
}

std::string globalLogic::toString(void) {
    stringstream ss;
    ss << "Global {" << endl
                << "\tPhilosophers size: " << p_philosophers.size() << endl
                << "\tResources size: " <<  p_rp->size() << " (adress: " <<  p_rp << ")" <<  endl
                //<< "\tdelay: " << (delay ? "true" : "false") << " (initial delay of first philosopher)" << endl
                //<< "\tpolite: " << (polite ? "true" : "false") << " (returning forks)" << endl
                //<< "\ttimeToDie: " << timeToDie << " (round that philosopher can starve)" << endl
                << "}" << endl << endl;
    for(Philosopher p: p_philosophers) {
        ss << p.toString() << endl;
    }
    return ss.str();
}

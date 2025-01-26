#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <unistd.h>
#include <getopt.h>
#include "globalLogic.h"

void help(std::string name) {
    std::cout << name << " ilustrate dining philosophers problem." << std::endl
        << "Params:" << std::endl
        << "\t-r <num>\t--resources\tnumber of resources (forks)" << std::endl
        << "\t-n <num>\t--philosophers\tnumber of philosophers (consuments)" << std::endl
        << "\t-s <num>\t--starving\tnumber of round that can philosopher starve" << std::endl
        << "\t-d \t\t--delay\t\tdelay first philosopher" << std::endl
        << "\t-p \t\t--polite\tphilosophers are polite and returning forks (even if they die)" << std::endl
        << "\t-h\t\t--help\t\tthis help" << std::endl
        << "Licence:" << std::endl
        << "\tGPL version 3, see http://www.gnu.org/licenses/" << std::endl
        << "Authors:" << std::endl
        << "\tOndřej Profant, ondrej.profant <> gmail.com, https://github.com/Kedrigern" << std::endl;
}

int main(int argc, char* argv[]) {
    int c;
    int resources = 5;
    int philosophers = 5;
    int starving = 3;
    bool delay = false;
    bool polite = false;

    static struct option long_options[] = {
        {"philosophers", required_argument, 0, 'n'},
        {"resources", required_argument, 0, 'r'},
        {"starving", required_argument, 0, 's'},
        {"polite",  no_argument, 0, 'p'},
        {"delay",  no_argument, 0, 'd'},
        {"help", no_argument, 0, 'h'},
        {0, 0, 0, 0}
    };
    /* getopt_long stores the option index here. */
    int option_index = 0;
    while ((c = getopt_long(argc, argv, "r:n:s:hpd", long_options, &option_index)) != -1) {
        switch (c) {
            case 'r':
                resources = atoi(optarg);
                break;
            case 'n':
                philosophers = atoi(optarg);
                break;
            case 's':
                starving = atoi(optarg);
                break;
            case 'd':
                delay = true;
                break;
            case 'p':
                polite = true;
                break;
            case 'h':
                help(std::string(argv[0]));
                return EXIT_SUCCESS;
                break;
        }
    }

    globalLogic* gl = new globalLogic(philosophers, resources, starving, delay, polite);

#if DEBUG
    std::cout << gl->toString();
#endif

    gl->run();

    gl->~globalLogic();

    return EXIT_SUCCESS;
}

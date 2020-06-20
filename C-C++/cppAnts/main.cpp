#include <iostream>

class Ants{
    public:
    std::string name;

    void printname(){
        std::cout << "Ants name: " << name << std::endl;
    }
};

int main(int argc, char* argv[])
{
    Ants* Colony = new Ants[10];
    std::cout << sizeof(Colony) << std::endl;
    return 0;
}
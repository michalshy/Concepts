#include <iostream>
#include "MemoryAllocation/StaticDynamicProblems.hpp"
#include "Variables/Variables.hpp"
#include "Containers/Containers.hpp"

struct Configuration
{
    bool Variables = 0;
    bool MemoryAllocation = 0;
    bool Containers = 1;
};



int main()
{
    Configuration c;
    if(c.Variables)
        VarMain();
    if(c.MemoryAllocation)
    {
        Holder h;
        h.AddByPointer();
        std::cout<<h.GetSize()<<std::endl;
        h.PrintValues();
    }
    if(c.Containers)
    {
        ContainersMain();
    }
}
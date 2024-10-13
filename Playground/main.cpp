#include <iostream>
#include "MemoryAllocation/StaticDynamicProblems.hpp"
#include "Variables/Variables.hpp"

struct Configuration
{
    bool Variables = 1;
    bool MemoryAllocation = 1;
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
}
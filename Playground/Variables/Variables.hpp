#include <iostream>
//Helpful library to check limits of types
#include <limits>
#include <cstdio>

constexpr int MEANING_OF_LIFE{42};

/**
 * Naming convention in C++ of variables:
 * Case sensitive
 * Meaningful names
 * Do not be afraid to use long names (intelliSense will cover it, but use it reasonable)
 * No type
 * No "No" or "Not"
 * snake_case (or camelCase?)
 */

void VarInit()
{
    //Different type of initializations
    int a; //uninitialized
    int b = 2;
    int c{}; //initialized to 0
    int d{2};
    int e(2); //old style
    //Print to check
    std::cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<std::endl;
}

template<class T>
void printSize(T checkType)
{
    std::cout<<"Size of "<<checkType<<" is "<<sizeof(checkType)<<std::endl;
}

/**
 * Provides fundamental types and their size printed
 */
void VarTypes()
{
    std::cout<<"---TYPES---"<<std::endl;
    bool a = true;
    printSize(a);
    char b = '\n';
    printSize(b);
    int c{2};
    printSize(c);
    short d{};
    printSize(d);
    long e{};
    printSize(e);
    long long f{std::numeric_limits<long long>::max()};
    printSize(f);
    unsigned int g = 2U;
    printSize(g);
    unsigned short h{};
    printSize(h);
    unsigned long i = 24ul;
    printSize(i);
    unsigned long long j = 18446744073709551615ull;
    printSize(j);
    float k = 13.91f;
    printSize(k);
    double l = 2.42e-10;
    printSize(l);
    std::cout<<"---END TYPES---"<<std::endl;
}

void Constants()
{
    std::cout<<"---START CONSTS---"<<std::endl;
    int a = 42;
    const int b = 23;
    const int c = a;
    const int d = b;

    constexpr int e = 23;
    constexpr int f = e;
    //constexpr int h = d - illegal
    //constexpr int i = a - illegal
    std::cout<<"---END CONSTS---"<<std::endl;
}

/**
 * Initialize your variables
 * Underflow (23u - 43u)
 */

void VarMain()
{
    VarInit();
    VarTypes();

    /**
     * Live coding
     */
    printf("---VAR MAIN---\n");
    auto alternativeMeaningOfLife{MEANING_OF_LIFE};
    alternativeMeaningOfLife += 42;
    const auto& borrowedMeaning{alternativeMeaningOfLife};
    printf("Meaning of live is: %d\n", borrowedMeaning);
    alternativeMeaningOfLife = 8 % 5;
    printf("Meaning of live is: %d\n", borrowedMeaning);
    printf("---END VAR MAIN---\n");
}
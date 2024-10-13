#include <iostream>
#include <utility>
#include <array>
#include <vector>
#include <string>

//very nice
using std::string_literals::operator""s;

//kinda container
void Pair()
{
    std::pair<int, int> pair{42, 1};
    std::pair p2{1, 1.0f};

    std::cout<<p2.first<<" "<<p2.second<<std::endl;
}

//sequence containers
void Array()
{
    std::array <int, 3> arr = {1,2,3};
    //std::array <int, 3> arr = {1,2,3,4}; - illegal
    std::array arr2{1,2,3};
    std::array arr3 = {1,2,3};

    if(!arr.empty())
    {
        std::cout<<arr.size()<<std::endl;
        std::cout<<arr.at(0)<<std::endl;
        std::cout<<arr.front()<<std::endl;
    }
}

/**
 * dynamic table
 * cannot be constexpr?
 */
void Vector()
{
    std::vector vec1{1,2,3};
    std::vector vec2 = {1,2,3};
    std::vector<int> vec3;

    vec1.clear();
    vec1.emplace_back(10); //same as push back rn
    vec1.push_back(1);

    vec2.resize(2);
    std::cout<<"vec2 back "<<vec2.back()<<std::endl; //2

    vec3.resize(3,2);
    std::cout<<"vec3 front "<<vec3.front()<<" and vec3 back "<<vec3.back()<<std::endl; //both 2

    /**
     * optimize vector resizing? !!!!!!!!!!!!!!!!!!!
     * use RESERVE
     */

    //i know ill add 100 elements to the vector
    int cycles = 100;
    vec1.reserve(cycles);
    //fast
    for(int i = 0; i < cycles; i++)
    {
        vec1.emplace_back(i);
    }
    std::cout<<"done";
    //slow
    for(int i = 0; i < cycles; i++)
    {
        vec1.emplace_back(i);
    }
    std::cout<<"done";
    std::cout<<std::endl;
}

/**
 * STRING CANNOT BE CONSTEXPR
 */
void Strings()
{
    std::string alexy = "cool guy"s;
    alexy += " i like him"s;
    std::cout<<alexy<<std::endl;

    /**
     * CONVERSION
     * std::to_string
     * std::stoi
     * std::stof
     * std::stod
     * std::stoul
     * ...
     */
}

/**
 * VERY COOL FEATURE FROM CPP17
 */
void AggregateInitialization()
{
    const std::array arr{1,2,3};
    //auto is mandatory
    const auto [a,b,c] = arr;
    //a = 1, b = 2, c = 3
    std::cout<<a<<" "<<b<<" "<<c<<std::endl;

    const std::pair p{"Hello"s, "World"s};
    const auto & [hello, world] = p;
    std::cout<<p.first<<", "<<p.second<<std::endl;
}

/**
 * Other containers
 * std::deque
 * std::list
 * std::forward_list
 */


//Main function of containers submodule
int ContainersMain()
{
    std::cout<<"---CONTAINERS---"<<std::endl;
    
    Pair();
    Array();
    Vector();
    Strings();
    AggregateInitialization();
    
    std::cout<<"---END CONTAINERS---"<<std::endl;
    return 0;
}

/**
 * REMARKS
 * creating container with string will result in compiler using C-STYLE char array, add suffix for this (not always)
 * {} in vector will create elemets inside, (x,y) will create vector of size x with y values
 * vector<bool> is complicated
 */
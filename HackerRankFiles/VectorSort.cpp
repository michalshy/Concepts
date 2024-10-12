#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

template<class T>
void printV(std::vector<T> v)
{
    for(auto el : v)
    {
        std::cout<<el<<" ";
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    std::vector<int> v;
    int s = 0;
    std::cin>>s;
    for(int i = 0; i < s; i++)
    {
        int temp;
        std::cin>>temp;
        v.push_back(temp);
    } 
    sort(v.begin(), v.end());
    printV(v);
    return 0;
}

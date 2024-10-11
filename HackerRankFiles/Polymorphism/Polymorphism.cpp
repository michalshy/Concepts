#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

static int students = 1;
static int professors = 1;

class Person
{   
    std::string name;
    int age;
    
    public:
    
    virtual void getdata() = 0;
    virtual void putdata() = 0;
    
    void setName(std::string _name)
    {
        name = _name;
    }
    void setAge(int _age)
    {
        age = _age;
    }
    std::string getName()
    {
        return name;
    }
    int getAge()
    {
        return age;
    }
};

class Student : public Person
{
    int cur_id;
    int marks[6];
    
    public:
 
    Student()
    {
        cur_id = students;
        students++;
    }
    
    void getdata() override
    {
        std::string tempS;
        int tempI;
        std::cin>>tempS;
        setName(tempS);
        std::cin>>tempI;
        setAge(tempI);
        for(int i = 0; i < 6; i++)
        {
            std::cin>>tempI;
            marks[i] = tempI;
        }
    }
    
    void putdata() override
    {
        int marksSum = 0;
        for(int i = 0; i < 6; i++)
        {
            marksSum += marks[i]; 
        }
        std::cout << getName() << " " << getAge() << " " << marksSum << " " << cur_id << std::endl; 
    }
};

class Professor : public Person
{
    int publications;
    int cur_id;
    
    public:
    
    Professor()
    {
        cur_id = professors;
        professors++;
    }
    
    void getdata() override
    {
        std::string tempS;
        int tempI;
        std::cin>>tempS;
        setName(tempS);
        std::cin>>tempI;
        setAge(tempI);
        std::cin>>publications;
    }
    
    void putdata() override
    {
        std::cout << getName() << " " << getAge() << " " << publications << " " << cur_id << std::endl; 
    }
    
};

int main(){

    int n, val;
    std::cin>>n; //The number of objects that is going to be created.
    const int t = n;
    Person *per[t];

    for(int i = 0;i < n;i++){

        std::cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}

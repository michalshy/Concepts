#include <string>
#include <vector>

std::string FunctionToTest()
{
    return "dxr";
}

class Node
{
    int index;
public:
    Node() = delete;
    Node(int _i)
    {
        index = _i;
    }
    int GetIndex()
    {
        return index;
    }
};

/*
* Holds values, which later will be checked if object persist after storing pointer on it out of its scope.
*/
class Holder
{
    std::vector<Node*> values;
public:
    explicit Holder() = default;

    void AddByPointer()
    {
        for(int i = 0; i < 100; i++)
        {
            Node *n = new Node(i);
            values.push_back(n);
        }
    }

    int GetSize()
    {
        return values.size();
    }

    void PrintValues()
    {
        for(int i = 0; i < 100; i++)
        {
            std::cout<<values[i]->GetIndex()<<" ";
        }
    }
};

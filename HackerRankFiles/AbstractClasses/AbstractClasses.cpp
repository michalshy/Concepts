#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>

// A generic smart pointer class
template <class T> class SmartPtr {
    T* ptr; // Actual pointer
public:
    // Constructor
    explicit SmartPtr(T* p = NULL) { ptr = p; }

    // Destructor
    ~SmartPtr() { delete (ptr); }

    // Overloading dereferencing operator
    T& operator*() { return *ptr; }

    // Overloading arrow operator so that
    // members of T can be accessed
    // like a pointer (useful if T represents
    // a class or struct or union type)
    T* operator->() { return ptr; }
    T* GetRaw(){ return ptr; }
};

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   std::map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function
};

void println(std::string msg)
{
   std::cout<<msg<<std::endl;
}

class LRUCache : public Cache
{
   public:
   LRUCache() = delete;
   LRUCache(int _capacity)
   {
      head = nullptr;
      tail = nullptr;
      cp = _capacity;
   }
   int get(int k);
   void set(int k, int v);
};

int LRUCache::get(int k)
{
   if (mp.find(k) != mp.end()) {
            Node* node = mp[k];

            if (node->prev != NULL) {
                node->prev->next = node->next;
                if (node->next != NULL)
                    node->next->prev = node->prev;
                else
                    tail = node->prev;
                node->prev = NULL;
                node->next = head;
                head->prev = node;
                head = node;
            }

            return node->value;
   }
   return -1;
}

void LRUCache::set(int k, int v)
{
      if (mp.find(k) != mp.end()) {
         Node* node = mp[k];
         node->value = v;   
         
         if (node->prev != nullptr) {
               node->prev->next = node->next;
               if (node->next != nullptr)
                  node->next->prev = node->prev;
               else
                  tail = node->prev;
               node->prev = nullptr;
               node->next = head;
               head->prev = node;
               head = node;
         }
      } else {
         SmartPtr<Node> n(new Node(nullptr, head, k, v));
         if(head != nullptr)
         {
            println("1st con");
            head->prev = n.GetRaw();
            head = n.GetRaw();
         }
         else
         {
            head = n.GetRaw();
         }
         if(tail == nullptr)
         {
            println("2nd con");
            tail = n.GetRaw();
         }
         if(tail->prev == nullptr)
         {
            head->next = tail;
            tail->prev = head;
         }
         if(mp.size() == cp)
         {
            println("3rd con");
            mp.erase(tail->key);
            tail = tail->prev;
            tail->next = nullptr;
         }
         mp[k] = n.GetRaw();
      }
      Node * t = head;
      while(t->next != nullptr)
      {
         std::cout<<t->key<<std::endl;
         t = t->next;
      }
      std::cout << t->key;
}

int main() {
   int n, capacity,i;
   std::cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      std::string command;
      std::cin >> command;
      if(command == "get") {
         int key;
         std::cin >> key;
         std::cout << l.get(key) << std::endl;
      } 
      else if(command == "set") {
         int key, value;
         std::cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}

#include "Logger.hpp"



void CLogger::Log(const std::string & msg)
{
    printf("Logged: %s", msg);
}
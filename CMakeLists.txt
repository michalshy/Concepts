cmake_minimum_required(VERSION 3.29)

project(
  Concepts
  VERSION 1.0
  LANGUAGES C CXX)



include_directories(src
src/Modules
src/Modules/Logger)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)

set(Logger_DIR src)
find_package(Logger REQUIRED)

include(CTest)

add_subdirectory(src)

add_executable(Concepts main.cpp)
target_link_libraries(Concepts Logger)

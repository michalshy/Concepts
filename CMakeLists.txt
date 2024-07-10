cmake_minimum_required(VERSION 3.30)

project(
  Concepts
  VERSION 1.0
  LANGUAGES C CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)

set(Logger_DIR src)
find_package(logger REQUIRED PATHS src/build)

include(CTest)

add_executable(Concepts main.cpp)
target_link_libraries(Concepts logger)

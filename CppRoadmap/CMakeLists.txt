cmake_minimum_required(VERSION 3.30)

project(
  Roadmap
  VERSION 1.0
  LANGUAGES C CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)

include(CTest)

add_executable(Roadmap src/main.cpp)

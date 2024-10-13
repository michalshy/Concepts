cmake_minimum_required(VERSION 3.30)

project(Playground)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(EXECUTABLES
"MemoryAllocation/StaticDynamicProblems.hpp"
"Variables/Variables.hpp"
"Containers/Containers.hpp")

add_executable(Playground
    main.cpp
${EXECUTABLES}

)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(TestPlayground

    Tests/TestsMemory.cc
    ${EXECUTABLES}
)

target_link_libraries(
  TestPlayground
  GTest::gtest_main
)
include(GoogleTest)
gtest_discover_tests(TestPlayground)


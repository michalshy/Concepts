#include <gtest/gtest.h>
#include <string>
#include "../MemoryAllocation/StaticDynamicProblems.hpp"

std::string dxr = FunctionToTest();

// Demonstrate some basic assertions.
TEST(CheckDexor, BasicAssertions) {
  // Expect equality.
  EXPECT_EQ(dxr, "dxr");
}
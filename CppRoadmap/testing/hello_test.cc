#include <gtest/gtest.h>
#include "../src/Test.hpp"

// Demonstrate some basic assertions.
TEST(AddTest, AddTestHeh) {

  TestLols t;
  // Expect two strings not to be equal.
  EXPECT_NE(t.Add(22,11), 32);
  // Expect equality.
  EXPECT_EQ(t.Add(22,11), 33);
}
#include "cmdline/cmdline.h"
#include <gtest/gtest.h>
#include <pthread.h>
#include <stdlib.h>

TEST(testcmdline, testparser)
{
    int argc = 3;
    char *argv[] = {"cur_exec_path", "-i", "hhhh"};
    cmdline::parser parser;
    parser.add<std::string>("input", 'i', "input of this test", true);
    parser.parse_check(argc, argv);
    auto got_param = parser.get<std::string>("input");
    EXPECT_EQ(got_param, "hhhh");
}
int main(int argc, char *argv[])
{

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

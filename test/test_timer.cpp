#include "TimerUtils/timer_utils.h"
#include <gtest/gtest.h>
#include <pthread.h>
#include <stdlib.h>

TEST(TestTimer, timertest)
{
    {
        TIMER_UTILS_TICK(timertest)
        usleep(10000); // sleep 10 ms
    }
    auto time_statistic = TimerUtils::Timer::getStatistic<std::chrono::milliseconds>();
    EXPECT_EQ(time_statistic.size(), 1);
    EXPECT_EQ(time_statistic.count("timertest"), 1);
    EXPECT_NE(time_statistic["timertest"], 0.F);
    for (auto p : time_statistic)
    {
        std::cout << p.first << "\t" << p.second << std::endl;
    }
}

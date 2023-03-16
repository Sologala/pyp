#include <TimerUtils/timer_utils.h>
#include <cmdline/cmdline.h>
#include <gtest/gtest.h>
#include <threadpool/threadpool.hpp>

TEST(ThreadPool, testTask)
{
    constexpr long long worker_num = 10;
    constexpr long long task_cnt = 10000000;
    constexpr long long task_cnt_pre_th = task_cnt / worker_num;

    long long sum = 0;
    std::vector<std::vector<long long>> all_tasks(worker_num);

    for (long long i = 1; i <= task_cnt; i++)
    {
        all_tasks[i % worker_num].push_back(i);
    }

    ThreadPool thpool((size_t)worker_num);

    std::vector<std::future<long long>> futures;
    for (auto &task : all_tasks)
    {
        auto opt = thpool.enqueue(
            [&](const std::vector<long long> &t) {
                long long s = 0;
                for (auto n : t)
                {
                    s += n;
                }
                return s;
            },
            task);
        futures.push_back(std::move(opt));
    }
    long long res = 0;
    for (auto &f : futures)
    {
        using namespace std::chrono_literals;
        f.wait_for(10ms);
        if (f.valid())
        {
            res += f.get();
        }
    }
    long long ground_thruth = (1 + task_cnt) * task_cnt / 2;
    EXPECT_EQ(ground_thruth, res);
}

#ifndef __TIMER_UTILS_H__
#define __TIMER_UTILS_H__
#include <chrono>
#include <deque>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

#ifdef ENABLE_TIMER_UTILS

#define TIMER_UTILS_TICK(name_) TimerUtils::Timer name_##__LINE__(#name_);

#else

#define TIMER_UTILS_TICK(name_) void(0);

#endif
namespace TimerUtils
{
class Timer
{
  public:
    using TimeStatisticType = std::unordered_map<std::string, double>;
    Timer(std::string name) : name_(name), tocked_(false)
    {
        TimeStatisticImpl::instance().tick(name_);
    }
    ~Timer()
    {
        TimeStatisticImpl::instance().tock(name_);
    }
    template <typename T>

    static std::enable_if_t<std::chrono::__is_duration<T>::value, TimeStatisticType> getStatistic()
    {
        TimeStatisticType ret;

        for (const auto &p : TimeStatisticImpl::instance().cost_time_)
        {
            double sum = 0;
            for (const auto &dur : p.second)
            {
                sum += std::chrono::duration_cast<T>(dur).count();
            }
            ret[p.first] = static_cast<double>(sum) / std::max(1UL, p.second.size());
        }
        return ret;
    }

  private:
    std::string name_;
    bool tocked_;
    class TimeStatisticImpl
    {

      public:
        static TimeStatisticImpl &instance()
        {
            static TimeStatisticImpl instance;
            return instance;
        }
        void tick(std::string name)
        {
            auto t = std::chrono::system_clock::now();
            tick_time_[name] = t;
        }
        void tock(std::string name)
        {
            auto t = std::chrono::system_clock::now();
            if (tick_time_.count(name))
            {
                auto dur = t - tick_time_[name];
                tick_time_.erase(name);

                cost_time_[name].push_back(dur);
                if (cost_time_[name].size() > max_save_cost_time_)
                {
                    cost_time_[name].pop_front();
                }
            }
        }
        std::unordered_map<std::string, std::chrono::system_clock::time_point> tick_time_;
        std::unordered_map<std::string, std::deque<std::chrono::nanoseconds>> cost_time_;
        const size_t max_save_cost_time_ = 20;

      private:
        TimeStatisticImpl(){};
        ~TimeStatisticImpl(){};
    };
};

} // namespace TimerUtils

#endif

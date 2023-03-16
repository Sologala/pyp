#include <unistd.h>

#include <iostream>
#include <pyp/fmt/fmt.hpp>
#include <pyp/timer/timer.hpp>

#include "pyp/cmdline/cmdline.h"
#include "pyp/yaml/yaml.hpp"
using namespace std;
#include <thread>
int main(int argc, char** argv) {
    cmdline::parser parse;
    parse.add<int>("cnt", 'c', "the cnt of loop", false, 10);
    parse.add<std::string>("yaml", 'y', "the file of yaml", false, "../a.yaml");
    int cnt = parse.get<int>("cnt");
    parse.parse_check(argc, argv);

    {
        std::string yaml_file = parse.get<string>("yaml");
        fmt::print("test\t yaml parse\n {}", yaml_file);
        Yaml::Node root;
        Yaml::Parse(root, yaml_file);

        // test vector
        std::vector<float> arr = root["arr_int"].AsVector<float>();
        cout << arr.size() << endl;
        for (auto v : arr) {
            cout << v << endl;
        }

        // test path
        std::string path = root["path"].AsPath();
        fmt::print("target Path is {}\n", path);
    }

    {
        {
            MyTimer::Timer _("sleep");
            usleep(10000);
        }

        std::cout << MyTimer::Timer::COUNT["sleep"].ns() << "\t" << MyTimer::Timer::COUNT["sleep"].ms() << "\t"
                  << MyTimer::Timer::COUNT["sleep"].s() << "\t" << MyTimer::Timer::COUNT["sleep"].fps() << "\t"
                  << std::endl;
    }
}

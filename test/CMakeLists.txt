find_package(GTest REQUIRED)
add_executable(test_timer test_timer.cpp)
target_link_libraries(test_timer pyp::TimerUtils GTest::gtest_main -pthread)

add_executable(test_cmdline test_cmdline.cpp)
target_link_libraries(test_cmdline pyp::cmdline pyp::TimerUtils GTest::gtest_main -pthread)

add_executable(test_threadpool test_thredpool.cpp)
target_link_libraries(test_threadpool pyp::cmdline pyp::TimerUtils pyp::threadpool GTest::gtest_main -pthread)


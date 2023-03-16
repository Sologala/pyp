cmake_minimum_required(VERSION 3.5)
project(pyp VERSION 0.0.1)
set(PRIJECT_NAMESPACE ${PROJECT_NAME}::)
set(CMAKE_EXPORT_COMPILE_COMMANDS on)
if(ENABLE_TESTING)
    add_definitions(-DENABLE_TIMER_UTILS)
endif()
add_subdirectory(timer)
add_subdirectory(cmdline)


if(ENABLE_TESTING)
    find_package(GTest REQUIRED)
    add_executable(test_timer ./test/test_timer.cpp)
    target_link_libraries(test_timer TimerUtils GTest::gtest_main -pthread)

    add_executable(test_cmdline ./test/test_cmdline.cpp)
    target_link_libraries(test_cmdline cmdline TimerUtils GTest::gtest_main -pthread)

endif()




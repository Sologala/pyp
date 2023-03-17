cmake_minimum_required(VERSION 3.5)
project(pyp VERSION 0.0.1)
set(PRIJECT_NAMESPACE ${PROJECT_NAME})
set(CMAKE_EXPORT_COMPILE_COMMANDS on)
set(CMAKE_INSTALL_PREFIX /home/wen/installed)

if(ENABLE_TESTING)
    add_definitions(-DENABLE_TIMER_UTILS)
endif()
add_subdirectory(cpp/timer)
add_subdirectory(cpp/cmdline)
add_subdirectory(cpp/threadpool)

if(ENABLE_TESTING)
    add_subdirectory(test)
endif()




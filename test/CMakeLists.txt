cmake_minimum_required(VERSION 3.9)
project(test VERSION)
set(CMAKE_PREFIX_PATH "$ENV{HOME}/.local")
find_package(pyp REQUIRED)

add_executable(
    test
    ./test.cpp
)
target_link_libraries( 
    test
    pyp::cmdline
    pyp::timer
    pyp::fmt
    pyp::yaml
)

add_executable(
    testfmt
    ./test_fmt.cpp
)
target_link_libraries( 
    testfmt
    pyp::cmdline
    pyp::timer
    pyp::fmt
    pyp::yaml
)
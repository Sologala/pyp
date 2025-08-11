cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)


add_library(_dynamic_lib SHARED ./src/dyn_lib/dynamic_lib.cpp)
target_include_directories(_dynamic_lib PUBLIC ./src/dyn_lib/)    
install(TARGETS _dynamic_lib DESTINATION ${SKBUILD_PROJECT_NAME})


pybind11_add_module(_core MODULE ./src/cpp/test.cpp)
target_link_libraries(_core PRIVATE _dynamic_lib)
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})

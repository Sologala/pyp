project(cmdline)
cmake_minimum_required(VERSION 3.0)

add_library(${PROJECT_NAME} INTERFACE)
add_library (${PRIJECT_NAMESPACE}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME} INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>)

INSTALL(DIRECTORY include DESTINATION include )

install(TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}Targets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    PUBLIC_HEADER DESTINATION include)

install(EXPORT ${PROJECT_NAME}Targets 
    FILE ${PROJECT_NAME}Targets.cmake
    NAMESPACE ${PRIJECT_NAMESPACE}::
    DESTINATION lib/cmake)

install(FILES "cmake/${PROJECT_NAME}Config.cmake"
        DESTINATION lib/cmake)



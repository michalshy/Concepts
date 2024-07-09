cmake_minimum_required(VERSION 3.20)

project(Logger VERSION 1.0.0 DESCRIPTION "example lib")



add_library(Logger SHARED
    Logger/Logger.cpp
)

set_target_properties(Logger PROPERTIES VERSION ${PROJECT_VERSION})

set_target_properties(Logger PROPERTIES PUBLIC_HEADER Logger/Logger.h)

configure_file(mylib.pc.in mylib.pc @ONLY)

target_include_directories(Logger PRIVATE .)

include(GNUInstallDirs)

install(TARGETS Logger
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(FILES ${CMAKE_BINARY_DIR}/mylib.pc
DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)

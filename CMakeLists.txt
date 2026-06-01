cmake_minimum_required(VERSION 3.21)
project(respo_cpp_env LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

option(ENABLE_ASAN "Enable AddressSanitizer" OFF)

if(ENABLE_ASAN)
  add_compile_options(-fsanitize=address -fno-omit-frame-pointer)
  add_link_options(-fsanitize=address)
endif()

add_executable(sample_app cpp/src/main.cpp)
set_target_properties(sample_app PROPERTIES OUTPUT_NAME "sample_app")

add_executable(smoke_test cpp/tests/smoke_test.cpp)
set_target_properties(smoke_test PROPERTIES OUTPUT_NAME "smoke_test")

include(CTest)
enable_testing()
add_test(NAME smoke_test COMMAND smoke_test)

find_program(CLANG_FORMAT_EXE NAMES clang-format)
if(CLANG_FORMAT_EXE)
  file(GLOB_RECURSE CPP_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/cpp/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/cpp/src/*.hpp"
    "${CMAKE_SOURCE_DIR}/cpp/tests/*.cpp"
    "${CMAKE_SOURCE_DIR}/cpp/tests/*.hpp")
  add_custom_target(clang-format
    COMMAND ${CLANG_FORMAT_EXE} --dry-run --Werror ${CPP_SOURCES}
    COMMENT "Checking C++ formatting with clang-format")
endif()

find_program(CLANG_TIDY_EXE NAMES clang-tidy)
if(CLANG_TIDY_EXE)
  add_custom_target(clang-tidy
    COMMAND ${CLANG_TIDY_EXE}
      ${CMAKE_SOURCE_DIR}/cpp/src/main.cpp
      ${CMAKE_SOURCE_DIR}/cpp/tests/smoke_test.cpp
      --
      -std=c++23
      -I${CMAKE_SOURCE_DIR}/cpp/src
    COMMENT "Running clang-tidy on C++ sources")
endif()

cmake_minimum_required(VERSION 3.0)
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)

project(ecal_cpp_notes)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(eCAL REQUIRED PATHS C:/eCAL)
find_package(Protobuf REQUIRED)

add_subdirectory("notes/hello_world/cpp/hello_world_publisher")
add_subdirectory("notes/hello_world/cpp/hello_world_subscriber")


add_subdirectory("notes/hello_world_proto/cpp/hello_world_proto_publisher")
add_subdirectory("notes/hello_world_proto/cpp/hello_world_proto_subscriber")

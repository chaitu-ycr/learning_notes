project(hello_world_proto_rec)

set(source_files
  main.cpp
)

set(protobuf_files
    ${CMAKE_CURRENT_SOURCE_DIR}/../proto_messages/hello_world.proto
)

add_executable(${PROJECT_NAME} ${source_files})

PROTOBUF_TARGET_CPP(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/../proto_messages/ ${protobuf_files})

target_link_libraries(${PROJECT_NAME}
  eCAL::core
  protobuf::libprotobuf
)
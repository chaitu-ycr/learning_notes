project(hello_world_rec)

set(source_files
  main.cpp
)

add_executable(${PROJECT_NAME} ${source_files})

target_link_libraries(${PROJECT_NAME}
  eCAL::core
)
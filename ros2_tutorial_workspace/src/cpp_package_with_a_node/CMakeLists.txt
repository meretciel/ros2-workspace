cmake_minimum_required(VERSION 3.8)
project(cpp_package_with_a_node)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(cpp_package_with_a_library REQUIRED)

# <start>Custom Application Related Section</start>
set(RCLCPP_LOCAL_BINARY_NAME print_forever_node)

add_executable(${RCLCPP_LOCAL_BINARY_NAME}
    src/print_forever_node_main.cpp
    src/print_forever_node.cpp
)


# Set up dependencies
ament_target_dependencies(${RCLCPP_LOCAL_BINARY_NAME}
    rclcpp
)

target_link_libraries(${RCLCPP_LOCAL_BINARY_NAME})

target_include_directories(${RCLCPP_LOCAL_BINARY_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

target_compile_features(${RCLCPP_LOCAL_BINARY_NAME} PUBLIC
    c_std_99 cxx_std_17)

install(TARGETS ${RCLCPP_LOCAL_BINARY_NAME} DESTINATION
    lib/${PROJECT_NAME})
unset(RCLCPP_LOCAL_BINARY_NAME)
# <end>Custom Application Related Section</end>


# <start>Executable: sample_class_local_node</start>
set(LOCAL_BINARY_NAME sample_class_local_node)

add_executable(${LOCAL_BINARY_NAME}
    "src/sample_class_local_node_main.cpp"
)

# Set up dependencies
ament_target_dependencies(${LOCAL_BINARY_NAME}
    rclcpp
    "cpp_package_with_a_library"
)

target_link_libraries(${LOCAL_BINARY_NAME}
)

target_include_directories(${LOCAL_BINARY_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

target_compile_features(${LOCAL_BINARY_NAME} PUBLIC
    "c_std_99"
    "cxx_std_17"
)

install(TARGETS ${LOCAL_BINARY_NAME} DESTINATION
    lib/${PROJECT_NAME})

unset(LOCAL_BINARY_NAME)

# <end>Executable: sample_class_local_node</end>



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

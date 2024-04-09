cmake_minimum_required(VERSION 3.8)
project(more_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

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

find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/AddressBook.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)

# can neatly list all of your interfaces, and generate all lists at once
#
# set(msg_files
#   "msg/Message1.msg"
#   "msg/Message2.msg"
# )
# set(srv_files
#   "srv/Service1.srv"
#   "srv/Service2.srv"
# )
# rosidl_generate_interfaces(${PROJECT_NAME}
#   ${msg_files}
#   ${srv_files}
# )

# Build the publisher
find_package(rclcpp REQUIRED)
add_executable(publish_address_book src/publish_address_book.cpp)
ament_target_dependencies(publish_address_book rclcpp)
install(
  TARGETS
  publish_address_book
  DESTINATION lib/${PROJECT_NAME}
)

# Link against the interface
# This CMake code is only required when you want to use interfaces
# in the same package as the one in which they are defined
rosidl_get_typesupport_target(cpp_typesupport_target
  ${PROJECT_NAME} rosidl_typesupport_cpp)
target_link_libraries(publish_address_book "${cpp_typesupport_target}")

ament_package()

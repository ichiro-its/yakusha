cmake_minimum_required(VERSION 3.5)

project(yakusha)

if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

if(BUILD_TESTING)
  find_package(rosidl_default_generators REQUIRED)

  rosidl_generate_interfaces(${PROJECT_NAME}_interfaces
    "msg/arrays/Arrays.msg"
    "msg/arrays/BoundedDynamicArrays.msg"
    "msg/complex/NonFloats.msg"
    "msg/complex/Numbers.msg"
    "msg/primitives/Floats.msg"
    "msg/primitives/Integers.msg"
    "msg/primitives/NonNumbers.msg"
    "msg/primitives/UnsignedIntegers.msg")
endif()

ament_python_install_package(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  find_package(ament_lint_auto REQUIRED)

  ament_add_pytest_test(${PROJECT_NAME}_tests "test")

  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

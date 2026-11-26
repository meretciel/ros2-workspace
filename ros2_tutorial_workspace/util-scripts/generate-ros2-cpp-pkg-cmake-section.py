from dataclasses import dataclass, field
from copy import deepcopy

EXECUTABLE_TEMPLATE = """\
# <start>Executable: [=[executable_name]=]</start>
set(LOCAL_BINARY_NAME [=[executable_name]=])

add_executable(${LOCAL_BINARY_NAME}
    [=[executable_cpp_files]=]
)

# Set up dependencies
ament_target_dependencies(${LOCAL_BINARY_NAME}
    rclcpp
    [=[ros2_dependencies]=]
)

target_link_libraries(${LOCAL_BINARY_NAME})

target_include_directories(${LOCAL_BINARY_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

target_compile_features(${LOCAL_BINARY_NAME} PUBLIC
    [=[compile_features]=]
)

install(TARGETS ${LOCAL_BINARY_NAME} DESTINATION
    lib/${PROJECT_NAME})
    
unset(LOCAL_BINARY_NAME)

# <end>Executable: [=[executable_name]=]</end>
"""


SHARED_LIBRARY_TEMPLATE = """\
# <start>Shared Library</start>

# Shared library is accessed via the package. Therefore the
# target name is the project name
add_library(${PROJECT_NAME} SHARED
    [=[library_cpp_files]=]
)

ament_target_dependencies(${PROJECT_NAME}
    rclcpp
    [=[ros2_dependencies]=]
)

target_include_directories(${PROJECT_NAME} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)
ament_export_dependencies(rclcpp)
[=[export_ros2_dependencies]=]

target_link_libraries(${PROJECT_NAME})

install(
    DIRECTORY include/
    DESTINATION include
)

install(
    TARGETS ${PROJECT_NAME}
    EXPORT export_${PROJECT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)
# <end>Shared Library</end>
"""

DEFAULT_COMPILER_FEATURES = ["c_std_99", "cxx_std_17"]


@dataclass
class ExecutableConfig:
    package_name: str
    executable_name: str
    executable_cpp_files: list[str]
    ros2_dependencies: list[str]
    compile_features: list[str] = field(default_factory=lambda: deepcopy(DEFAULT_COMPILER_FEATURES))

@dataclass
class SharedLibraryConfig:
    package_name: str
    library_cpp_files: list[str]
    ros2_dependencies: list[str]
    compile_features: list[str] = field(default_factory=lambda: deepcopy(DEFAULT_COMPILER_FEATURES))


def make_quote_items(items, delimiter="\n", indent=4):
    v = [f'"{item}"' for item in items]
    return (delimiter + " " * indent).join(v)


def transcribe_executable_config(cfg: ExecutableConfig):
    ros2_dependencies = [item for item in cfg.ros2_dependencies if item != 'rclcpp']
    output = EXECUTABLE_TEMPLATE.replace("[=[executable_name]=]", cfg.executable_name)
    output = output.replace("[=[executable_cpp_files]=]", make_quote_items(cfg.executable_cpp_files))
    output = output.replace("[=[ros2_dependencies]=]", make_quote_items(ros2_dependencies))
    output = output.replace("[=[compile_features]=]", make_quote_items(cfg.compile_features))
    return output

def transcribe_shared_library_config(cfg: SharedLibraryConfig):
    ros2_dependencies = [item for item in cfg.ros2_dependencies if item != 'rclcpp']
    export_dependencies = ["ament_export_dependencies(item)" for item in ros2_dependencies]

    actions = [
        ("[=[library_cpp_files]=]", make_quote_items(cfg.library_cpp_files)),
        ("[=[ros2_dependencies]=]", make_quote_items(ros2_dependencies)),
        ("[=[export_ros2_dependencies]=]", "\n".join(export_dependencies)),
        ("[=[compile_features]=]", make_quote_items(cfg.compile_features))
    ]
    output = SHARED_LIBRARY_TEMPLATE
    for origin, replacement in actions:
        output = output.replace(origin, replacement)
    return output

def transcribe(cfg):
    match cfg:
        case ExecutableConfig():
            return transcribe_executable_config(cfg)
        case SharedLibraryConfig():
            return transcribe_shared_library_config(cfg)
        case _:
            raise RuntimeError

configs = [
    ExecutableConfig(
        package_name= "cpp_package_with_a_node",
        executable_name="sample_class_local_node",
        executable_cpp_files=[
            "src/sample_class_local_node_main.cpp",
        ],
        ros2_dependencies=[
            "cpp_package_with_a_library"
        ],
    ),

    SharedLibraryConfig(
        package_name="cpp_package_with_a_library",
        library_cpp_files=[
            "src/sample_class.cpp",
            "src/sample_class_local_node.cpp"
        ],
        ros2_dependencies=[],
    )
]

print()
for cfg in configs:
    print("-" * 40 + f" Package: {cfg.package_name} " + "-" * 40)
    result = transcribe(cfg)
    print(result)
    print()

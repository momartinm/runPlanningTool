# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/momartin/tools/myoptic/optic-base/optic/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/momartin/tools/myoptic/optic-base/optic/src

# Utility rule file for doc.

# Include the progress variables for this target.
include optic/CMakeFiles/doc.dir/progress.make

doc: optic/CMakeFiles/doc.dir/build.make

.PHONY : doc

# Rule to build all files generated by this target.
optic/CMakeFiles/doc.dir/build: doc

.PHONY : optic/CMakeFiles/doc.dir/build

optic/CMakeFiles/doc.dir/clean:
	cd /home/momartin/tools/myoptic/optic-base/optic/src/optic && $(CMAKE_COMMAND) -P CMakeFiles/doc.dir/cmake_clean.cmake
.PHONY : optic/CMakeFiles/doc.dir/clean

optic/CMakeFiles/doc.dir/depend:
	cd /home/momartin/tools/myoptic/optic-base/optic/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/momartin/tools/myoptic/optic-base/optic/src /home/momartin/tools/myoptic/optic-base/optic/src/optic /home/momartin/tools/myoptic/optic-base/optic/src /home/momartin/tools/myoptic/optic-base/optic/src/optic /home/momartin/tools/myoptic/optic-base/optic/src/optic/CMakeFiles/doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : optic/CMakeFiles/doc.dir/depend


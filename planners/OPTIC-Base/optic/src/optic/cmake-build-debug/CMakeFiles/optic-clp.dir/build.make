# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

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
CMAKE_COMMAND = /home/momartin/ide/clion-2017.2.2/bin/cmake/bin/cmake

# The command to remove a file.
RM = /home/momartin/ide/clion-2017.2.2/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/momartin/tools/optic/src/optic

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/momartin/tools/optic/src/optic/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/optic-clp.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/optic-clp.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/optic-clp.dir/flags.make

CMakeFiles/optic-clp.dir/opticMain.o: CMakeFiles/optic-clp.dir/flags.make
CMakeFiles/optic-clp.dir/opticMain.o: ../opticMain.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/momartin/tools/optic/src/optic/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/optic-clp.dir/opticMain.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/optic-clp.dir/opticMain.o -c /home/momartin/tools/optic/src/optic/opticMain.cpp

CMakeFiles/optic-clp.dir/opticMain.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/optic-clp.dir/opticMain.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/momartin/tools/optic/src/optic/opticMain.cpp > CMakeFiles/optic-clp.dir/opticMain.i

CMakeFiles/optic-clp.dir/opticMain.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/optic-clp.dir/opticMain.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/momartin/tools/optic/src/optic/opticMain.cpp -o CMakeFiles/optic-clp.dir/opticMain.s

CMakeFiles/optic-clp.dir/opticMain.o.requires:

.PHONY : CMakeFiles/optic-clp.dir/opticMain.o.requires

CMakeFiles/optic-clp.dir/opticMain.o.provides: CMakeFiles/optic-clp.dir/opticMain.o.requires
	$(MAKE) -f CMakeFiles/optic-clp.dir/build.make CMakeFiles/optic-clp.dir/opticMain.o.provides.build
.PHONY : CMakeFiles/optic-clp.dir/opticMain.o.provides

CMakeFiles/optic-clp.dir/opticMain.o.provides.build: CMakeFiles/optic-clp.dir/opticMain.o


CMakeFiles/optic-clp.dir/solver-clp.o: CMakeFiles/optic-clp.dir/flags.make
CMakeFiles/optic-clp.dir/solver-clp.o: ../solver-clp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/momartin/tools/optic/src/optic/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/optic-clp.dir/solver-clp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/optic-clp.dir/solver-clp.o -c /home/momartin/tools/optic/src/optic/solver-clp.cpp

CMakeFiles/optic-clp.dir/solver-clp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/optic-clp.dir/solver-clp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/momartin/tools/optic/src/optic/solver-clp.cpp > CMakeFiles/optic-clp.dir/solver-clp.i

CMakeFiles/optic-clp.dir/solver-clp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/optic-clp.dir/solver-clp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/momartin/tools/optic/src/optic/solver-clp.cpp -o CMakeFiles/optic-clp.dir/solver-clp.s

CMakeFiles/optic-clp.dir/solver-clp.o.requires:

.PHONY : CMakeFiles/optic-clp.dir/solver-clp.o.requires

CMakeFiles/optic-clp.dir/solver-clp.o.provides: CMakeFiles/optic-clp.dir/solver-clp.o.requires
	$(MAKE) -f CMakeFiles/optic-clp.dir/build.make CMakeFiles/optic-clp.dir/solver-clp.o.provides.build
.PHONY : CMakeFiles/optic-clp.dir/solver-clp.o.provides

CMakeFiles/optic-clp.dir/solver-clp.o.provides.build: CMakeFiles/optic-clp.dir/solver-clp.o


# Object files for target optic-clp
optic__clp_OBJECTS = \
"CMakeFiles/optic-clp.dir/opticMain.o" \
"CMakeFiles/optic-clp.dir/solver-clp.o"

# External object files for target optic-clp
optic__clp_EXTERNAL_OBJECTS =

optic-clp: CMakeFiles/optic-clp.dir/opticMain.o
optic-clp: CMakeFiles/optic-clp.dir/solver-clp.o
optic-clp: CMakeFiles/optic-clp.dir/build.make
optic-clp: libOpticCommon.a
optic-clp: /usr/lib/x86_64-linux-gnu/libCbcSolver.so
optic-clp: /usr/lib/x86_64-linux-gnu/libCbc.so
optic-clp: /usr/lib/x86_64-linux-gnu/libCgl.so
optic-clp: /usr/lib/x86_64-linux-gnu/libOsiClp.so
optic-clp: /usr/lib/x86_64-linux-gnu/libOsi.so
optic-clp: /usr/lib/x86_64-linux-gnu/libClp.so
optic-clp: /usr/lib/x86_64-linux-gnu/libCoinUtils.so
optic-clp: CMakeFiles/optic-clp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/momartin/tools/optic/src/optic/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable optic-clp"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/optic-clp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/optic-clp.dir/build: optic-clp

.PHONY : CMakeFiles/optic-clp.dir/build

CMakeFiles/optic-clp.dir/requires: CMakeFiles/optic-clp.dir/opticMain.o.requires
CMakeFiles/optic-clp.dir/requires: CMakeFiles/optic-clp.dir/solver-clp.o.requires

.PHONY : CMakeFiles/optic-clp.dir/requires

CMakeFiles/optic-clp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/optic-clp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/optic-clp.dir/clean

CMakeFiles/optic-clp.dir/depend:
	cd /home/momartin/tools/optic/src/optic/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/momartin/tools/optic/src/optic /home/momartin/tools/optic/src/optic /home/momartin/tools/optic/src/optic/cmake-build-debug /home/momartin/tools/optic/src/optic/cmake-build-debug /home/momartin/tools/optic/src/optic/cmake-build-debug/CMakeFiles/optic-clp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/optic-clp.dir/depend


import os.path

from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class RANGEV3Conan(ConanFile):
    name = "range_v3"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["RANGE_V3_TESTS"] = "OFF"
        tc.variables["RANGE_V3_EXAMPLES"] = "OFF"
        tc.variables["RANGE_V3_PERF"] = "OFF"
        tc.variables["RANGE_V3_DOCS"] = "OFF"
        tc.variables["RANGE_V3_HEADER_CHECKS"] = "OFF"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join(self.package_folder, "lib/cmake/range-v3/"))
        self.cpp_info.set_property("cmake_file_name", "range-v3")

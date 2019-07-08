#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class ImmerConan(ConanFile):
    name = "immer"
    version = "0.6.2"
    url = "https://github.com/slepasteur/conan-immer.git"
    homepage = "https://github.com/arximboldi/immer"
    author = "Simon Lepasteur <slepasteur@gmail.com>"
    description = "Postmodern immutable and persistent data structures for C++"
    license = "MIT"
    exports = ["LICENSE.md"]
    _source_folder = "%s-%s" % (name, version)

    def source(self):
        git = tools.Git(folder=self._source_folder)
        git.clone("https://github.com/arximboldi/immer.git", branch="v%s" % self.version)

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_folder)
        self.copy(pattern="*.h", dst=os.path.join("include", "immer"), src=os.path.join(self._source_folder, "immer"))
        self.copy(pattern="*.hpp", dst=os.path.join("include", "immer"), src=os.path.join(self._source_folder, "immer"))

    def package_id(self):
        self.info.header_only()

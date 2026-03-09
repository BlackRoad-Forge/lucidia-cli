"""Tests for the Lucidia virtual filesystem."""

import os
import sys
import shutil
import tempfile
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from components.virtual_fs import VirtualFS


@pytest.fixture
def vfs(tmp_path):
    """Create a VirtualFS rooted in a temp directory."""
    fs = VirtualFS(root=str(tmp_path))
    return fs


class TestVirtualFS:
    def test_initial_directory(self, vfs):
        """VFS should start at the root."""
        assert vfs.cwd == "/"

    def test_mkdir(self, vfs):
        result = vfs.mkdir("testdir")
        assert os.path.isdir(os.path.join(vfs.root, "testdir"))

    def test_ls_empty(self, vfs):
        result = vfs.ls()
        assert isinstance(result, (list, str))

    def test_write_and_cat(self, vfs):
        vfs.write("test.txt", "hello world")
        content = vfs.cat("test.txt")
        assert "hello world" in str(content)

    def test_cd_and_back(self, vfs):
        vfs.mkdir("subdir")
        vfs.cd("subdir")
        assert "subdir" in vfs.cwd
        vfs.cd("..")

    def test_rm(self, vfs):
        vfs.write("delete_me.txt", "temp")
        vfs.rm("delete_me.txt")
        filepath = os.path.join(vfs.root, "delete_me.txt")
        assert not os.path.exists(filepath)

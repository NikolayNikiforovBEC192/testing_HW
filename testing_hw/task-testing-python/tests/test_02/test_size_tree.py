import tempfile
import os
from tree_utils_02.size_tree import SizeTree

with tempfile.TemporaryDirectory(dir=os.getcwd()) as a:
    with tempfile.TemporaryDirectory(dir=a) as b:
        with tempfile.TemporaryDirectory(dir=b) as c:
            size = SizeTree().construct_filenode(a, is_dir=False).size
            assert 4096 == size

            size = SizeTree().construct_filenode(a, is_dir=True).size
            assert 4096 == size

            size = SizeTree().update_filenode(file_node=SizeTree().construct_filenode(a, is_dir=True)).size
            assert 4096 == size

            size = SizeTree().update_filenode(file_node=SizeTree().construct_filenode(a, is_dir=False)).size
            assert 4096 == size

            new_node = SizeTree().construct_filenode(a, is_dir=True)
            new_node.children.append(SizeTree().construct_filenode(a, is_dir=True))

            size = SizeTree().update_filenode(new_node).size
            assert 4096*2 == size







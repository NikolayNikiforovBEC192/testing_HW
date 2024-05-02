import tempfile
import os
from tree_utils_02.tree import Tree
import pytest


with tempfile.TemporaryDirectory(dir=os.getcwd()) as a:
    with tempfile.TemporaryDirectory(dir=a) as b:
        with tempfile.TemporaryDirectory(dir=b) as c:
            treee_node = Tree().get(a, True)
            assert True == treee_node.is_dir

            treee_node = Tree().get(a, dirs_only = False)
            assert True == treee_node.is_dir

            with pytest.raises(AttributeError) as e:
                 Tree().get('eshkereeeeee', dirs_only = True, recurse_call=True)
            assert 'Path not exist' in str(e)

            file = open(os.path.join(a, '2.txt'), 'w')
            assert False == Tree().get(os.path.join(a, '2.txt'), dirs_only=False).is_dir

            with pytest.raises(AttributeError) as e:
                 Tree().get(os.path.join(a, '2.txt'), dirs_only=True)
            assert 'Path is not directory' in str(e)

            assert not Tree().get(os.path.join(a, '2.txt'), dirs_only=True, recurse_call=True)


            assert True == Tree().construct_filenode(a, True).is_dir

            node = Tree().construct_filenode(a, True)
            assert True == Tree().update_filenode(node).is_dir


            treee_node = Tree().get(a, True)
            assert not Tree().filter_empty_nodes(treee_node, a)

            treee_node = Tree().get(a, True)
            treee_node.is_dir = False
            assert not Tree().filter_empty_nodes(treee_node, a)


with tempfile.TemporaryDirectory(dir=os.getcwd()) as a:
    with pytest.raises(ValueError) as e:
         treee_node = Tree().get(a, True)
         Tree().filter_empty_nodes(treee_node)
    assert 'Code should not be executed here!' in str(e)
            


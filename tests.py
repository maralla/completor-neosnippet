import sys
import types


class MockComletor(object):
    pass


class Vim(object):
    def Function(self, func):
        return lambda: {
            b'a': {b'word': b'hello', b'description': b'hello world'},
            b'b': {b'word': b'def', b'description': b'def world'},
            b'c': {b'word': b'defm', b'description': b'hello def'},
        }


sys.path.append('./pythonx')
completor = types.ModuleType('completor')
completor.Completor = MockComletor
sys.modules['completor'] = completor
sys.modules['vim'] = Vim()


from completor_neosnippet import Neosnippet  # noqa


def test_parse():
    neo = Neosnippet()
    neo.ft = 'python'
    neo.input_data = 'def'

    assert neo.parse('def') == [
        {'dup': 1, 'menu': b'[neosnip] def world', 'word': b'def'},
        {'dup': 1, 'menu': b'[neosnip] hello def', 'word': b'defm'},
    ]

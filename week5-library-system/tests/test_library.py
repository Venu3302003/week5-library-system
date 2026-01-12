from library_system.library import Library

def test_library_load():
    lib = Library()
    assert isinstance(lib.books, dict)

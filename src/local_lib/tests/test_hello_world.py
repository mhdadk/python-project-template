from local_lib import hello_world


def test1():
    text = hello_world()
    assert text == "Hello World!", "Incorrect text."

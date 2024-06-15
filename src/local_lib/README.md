The `local_lib` directory (the one this README file is in) contains all the functions and classes used in the files contained in the [`scripts`](../scripts/) directory, along with tests for each of these functions and classes.

More specifically, the [`local_lib`](local_lib/) directory contains the functions and
classes, while the [`tests`](tests/) directory contains the corresponding tests for
these functions and classes. For example, the [`local_lib/hello_world.py`](local_lib/hello_world.py) file contains a `hello_world` function, with its corresponding test inside the [`tests/test_hello_world.py`](tests/test_hello_world.py) file.

The [`__init__.py`](__init__.py) and [`local_lib/__init__.py`](local_lib/__init__.py) files are used to expose the functions inside the `local_lib` directory for easier importing.

Finally, if you are curious to know why the `local_lib` directory has this structure, see [this answer](https://stackoverflow.com/a/78593812/13809128).
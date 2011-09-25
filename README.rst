This integrates Chuck Rhode's `PythonTidy` script from
http://pypi.python.org/pypi/PythonTidy/ with the Sublime Text 2 editor.
For as long as there is no download available from PyPI, it uses my
Github fork at https://github.com/witsch/PythonTidy


Installation
------------

At the moment Git is required to install the plugin.  You will need
to clone the repository in your Sublime Text "Packages" directory::

$ git clone git@github.com:witsch/SublimePythonTidy.git

The "Packages" directory is located at:

* OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux: `~/.Sublime Text 2/Packages/`
* Windows: `%APPDATA%/Sublime Text 2/Packages/`


Usage
-----

To reformat your Python source, simply press the keyboard shortcut.  It
is **Ctrl+Alt+Cmd+T** on OSX and **Ctrl+Alt+Shift+T** on
Linux and Windows.

The output of `PythonTidy` can be tweaked to your individual taste or
company policy via a configuration file stored at `~/.pythontidy.xml`.
The complete set of default settings can be dumped using::

$ cd 'Library/Application Support/Sublime Text 2/Packages'
$ python SublimePythonTidy/PythonTidy/runner.py -d

Example settings are available at https://gist.github.com/1240583

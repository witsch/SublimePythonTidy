from sublime_plugin import TextCommand
from sublime import Region
from os.path import abspath, expanduser, exists
from StringIO import StringIO
from sys import path


# tweak path to allow importing PythonTidy from the git submodule
extra = abspath('PythonTidy')
path.insert(0, extra)
import PythonTidy
import PythonTidyWrapper
path.remove(extra)


def setup():
    xml = expanduser('~/.pythontidy.xml')
    if exists(xml):
        config = PythonTidyWrapper.Config(file=xml)
        config.to_pythontidy_namespace()


class python_tidy(TextCommand):

    def run(self, edit):
        setup()
        view = self.view
        region = Region(0L, view.size())
        source = StringIO(view.substr(region))
        output = StringIO()
        PythonTidy.tidy_up(source, output)
        view.replace(edit, region, output.getvalue())

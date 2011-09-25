from sublime_plugin import TextCommand
from sublime import Region
from subprocess import call
from os.path import abspath, expanduser, exists, join
from StringIO import StringIO
from sys import path


# load the git submodule
extra = abspath('PythonTidy')
if not exists(join(extra, '.git')):
    call(['git', 'submodule', 'init'])
    call(['git', 'submodule', 'update'])

# tweak path to allow importing PythonTidy from the git submodule
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

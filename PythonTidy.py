from sublime_plugin import TextCommand
from sublime import Region
from subprocess import Popen, PIPE
from os.path import expanduser, exists


cmd = ['pythontidy']
config = expanduser('~/.pythontidy.xml')
if exists(config):
    cmd.extend(['-c', config])


class python_tidy(TextCommand):
    def run(self, edit):
        view = self.view
        region = Region(0L, view.size())
        tidy = Popen(cmd, bufsize=-1, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = tidy.communicate(view.substr(region))
        view.replace(edit, region, output)

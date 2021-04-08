"""This module exports the Solhint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Solhint(NodeLinter):
    """Solhint class delegate call to solhint tool and return result back."""

    cmd = 'solhint --config ./.solhint.json ${file}'
    regex = r'^\s+(?P<line>\d+):(?P<col>\d+)\s+((?P<error>error)|(?P<warning>warning))\s+(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'sol'
    error_stream = util.STREAM_BOTH
    defaults = {
        'selector': 'source.sol'
    }

    def run(self, cmd, code):
        # Workaround eslint bug https://github.com/eslint/eslint/issues/9515
        # Fixed in eslint 4.10.0
        if code == '':
            code = ' '

        return super().run(cmd, code)

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from sphinx.directives.other import Include as BaseInclude



class MDInclude(BaseInclude):
    """Override of sphinx.directives.other.Include with customizations

    Adds option to specify a line of text to inject into the beginning of the
    included document.  This allows you to use:

    .. code-block:: rst

       .. mdinclude:: ../../README.md
          :parser: myst_parser.sphinx_
          :start-after: # Installation
          :inject: # Installation

    Since the ``start-after`` option will remove the line from the included document,
    but you may want to keep it in the output.
    """

    option_spec = BaseInclude.option_spec.copy() if BaseInclude.option_spec else {}
    option_spec["inject"] = str
    optional_arguments = 1

    def read_file(self, filename: str) -> str:
        """Override of sphinx.directives.other.Include.read_file to handle the ``inject`` option
        """
        content = super().read_file(filename)
        if "inject" in self.options:
            inject_line = self.options.pop("inject")
            content = inject_line + "\n" + content
        return content


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive("mdinclude", MDInclude)
    return {"version": "0.1", "parallel_read_safe": True}

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

try:
    __version__ = version("pypci")
except:
    __version__ = "0.0.0"


from .pypci import lspci
from .pypci import read
from .pypci import write



from ._version import get_versions
__version__ = get_versions()['version']
if not __version__:
    __version__ = '1.2.3'
del get_versions

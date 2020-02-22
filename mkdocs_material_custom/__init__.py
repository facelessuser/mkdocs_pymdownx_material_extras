"""Mkdocs material Custom."""
from .__meta__ import __version__, __version_info__  # noqa: F401
import glob
import os
import mkdocs.plugins
import mkdocs.structure.files

RESOURCE_PATH = os.path.abspath(os.path.dirname(__file__))

# Nothing to import with all
__all__ = tuple()


class MaterialCustom(mkdocs.plugins.BasePlugin):
    """Plugin to add custom assets to Material theme."""

    def on_files(self, files, config):
        """Add additional assets."""

        for item in glob.glob(os.path.join(RESOURCE_PATH, '*.svg').replace('\\', '/'), recursive=True):
            files.append(item)
        return mkdocs.structure.files.Files(files)

    def on_config(self, config, **kwargs):
        """Add additional assets."""

        config['extra_css'].extend(
            glob.glob(os.path.join(RESOURCE_PATH, '*.css').replace('\\', '/'), recursive=True)
        )
        config['extra_javascript'].extend(
            glob.glob(os.path.join(RESOURCE_PATH, '*.js').replace('\\', '/'), recursive=True)
        )
        return config

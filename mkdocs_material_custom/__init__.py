"""Mkdocs material Custom."""
from .__meta__ import __version__, __version_info__  # noqa: F401
import glob
import os
import mkdocs.plugins
import mkdocs.structure.files

RESOURCE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'theme')

# Nothing to import with all
__all__ = tuple()


class MaterialCustom(mkdocs.plugins.BasePlugin):
    """Plugin to add custom assets to Material theme."""

    def on_config(self, config, **kwargs):
        """Add additional assets."""

        config['theme'].dirs.append(RESOURCE_PATH)

        config['extra_css'].extend(
            [
                os.path.basename(f) for f in glob.glob(os.path.join(RESOURCE_PATH, '*.css').replace('\\', '/'))
            ]
        )
        config['extra_javascript'].extend(
            [
                os.path.basename(f) for f in glob.glob(os.path.join(RESOURCE_PATH, '*.js').replace('\\', '/'))
            ]
        )

        return config

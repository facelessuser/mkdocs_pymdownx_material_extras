"""Mkdocs material Custom."""
from .__meta__ import __version__, __version_info__  # noqa: F401
import glob
import os
import mkdocs.plugins

RESOURCE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'theme')


class PymdownxMaterialExtras(mkdocs.plugins.BasePlugin):
    """Plugin to add custom assets to Material theme."""

    def on_config(self, config, **kwargs):
        """Add additional assets."""

        base_path = RESOURCE_PATH + '/'

        # Add our theme resources to the theme path.
        config['theme'].dirs.append(RESOURCE_PATH)

        # Add our extra styles and JavaScript to be included in the template.
        config['extra_css'].extend(glob.glob(RESOURCE_PATH + '*.css').replace(base_path, '').replace('\\', '/'))
        config['extra_javascript'].extend(glob.glob(RESOURCE_PATH + '*.js').replace(base_path, '').replace('\\', '/'))
        return config

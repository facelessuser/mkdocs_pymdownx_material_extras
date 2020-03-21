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


        # Add our theme resources to the theme path.
        config['theme'].dirs.insert(0, RESOURCE_PATH)

        base_path = RESOURCE_PATH.replace('\\', '/') + '/'

        # Add our extra styles and JavaScript to be included in the template.
        config['extra_css'].extend(
            [f.replace('\\', '/').replace(base_path, '') for f in glob.glob(base_path + '**/*.css', recursive=True)]
        )
        config['extra_javascript'].extend(
            [f.replace('\\', '/').replace(base_path, '') for f in glob.glob(base_path + '**/*.js', recursive=True)]
        )
        return config

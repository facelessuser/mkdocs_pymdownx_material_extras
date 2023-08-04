"""Mkdocs material Custom."""
from .__meta__ import __version__, __version_info__, parse_version  # noqa: F401
import glob
import os
import mkdocs.plugins
import mkdocs

MKDOCS_150 = parse_version(mkdocs.__version__) >= (1, 5, 0)
RESOURCE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'theme')


class PymdownxMaterialExtras(mkdocs.plugins.BasePlugin):
    """Plugin to add custom assets to Material theme."""

    def on_config(self, config, **kwargs):
        """Add additional assets."""

        # Add our theme resources to the theme path.
        config['theme'].dirs.insert(0, RESOURCE_PATH)

        base_path = RESOURCE_PATH.replace('\\', '/') + '/'

        # Add our extra styles and JavaScript to be included in the template.
        extras = set(config['extra_css'])
        for f in glob.glob(base_path + '**/*.css', recursive=True):
            name = f.replace('\\', '/').replace(base_path, '')
            if name not in extras:
                config['extra_css'].append(name)

        if MKDOCS_150:
            from mkdocs.config.config_options import ExtraScriptValue

            extras = set(
                script.path if not isinstance(script, str) else script for script in config['extra_javascript']
            )
            for f in glob.glob(base_path + '**/extra*.js', recursive=True):
                name = f.replace('\\', '/').replace(base_path, '')
                if name not in extras:
                    config['extra_javascript'].append(ExtraScriptValue(name))
        else:
            extras = set(config['extra_javascript'])
            for f in glob.glob(base_path + '**/extra*.js', recursive=True):
                name = f.replace('\\', '/').replace(base_path, '')
                if name not in extras:
                    config['extra_javascript'].append(name)

        return config

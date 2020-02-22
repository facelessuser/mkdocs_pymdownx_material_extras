# MkDocs Pymdownx Material Extras

A plugin that for MkDocs and specifically the [MkDocs Material Theme](https://github.com/squidfunk/mkdocs-material).

Adds additional resources that are used in the PyMdown Extensions documentation, and other
[@facelessuser](https://github.com/facelessuser) projects.

While this is not specifically meant for outside consumption, and was originally written for
[@facelessuser](https://github.com/facelessuser) projects,
it can be freely used if desired.

Files are copied from the [pymdown-extensions project](https://github.com/facelessuser/pymdown-extensions/tree/master/docs/theme/assets/pymdownx-extras).

## Instructions

This is bound to specific versions of MkDocs Material and PyMdown Extensions. It may sometimes be tied to betas.

Installation (supported as soon as we make it available in pip)

```
pip install mkdocs_pymdownx_material_extras
```

Add it to your your `mkdocs.yml` plugins. It is assuming you are using MkDocs Material. When doing so, remember to add
back the `search` plugin as it doesn't append to the plugins, but overrides the plugins:

```yml
plugins:
  - search
  - mkdocs_pymdownx_material_extras
```

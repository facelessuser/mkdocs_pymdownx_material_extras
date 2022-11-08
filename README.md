# MkDocs Pymdownx Material Extras

A plugin for MkDocs -- specifically the [MkDocs Material Theme](https://github.com/squidfunk/mkdocs-material).

Adds additional resources that are used in the PyMdown Extensions documentation, and other
[@facelessuser](https://github.com/facelessuser) projects.

While this is not specifically meant for outside consumption, and was originally written for
[@facelessuser](https://github.com/facelessuser) projects, it can be freely used if desired.

Files are copied from the [pymdown-extensions project](https://github.com/facelessuser/pymdown-extensions/tree/master/docs/theme/assets/pymdownx-extras).

## Instructions

This is bound to specific versions of MkDocs Material and PyMdown Extensions. It may sometimes be tied to betas.

Installation:

```
pip install mkdocs_pymdownx_material_extras
```

Add it to your `mkdocs.yml` plugins. It is assuming you are using MkDocs Material. When doing so, remember to add
back the `search` plugin as it doesn't append to the plugins, but overrides the plugins:

```yml
plugins:
  - search
  - mkdocs_pymdownx_material_extras
```

Setup your theme as follows:

```yml
theme:
  name: material # Must use Material theme
  custom_dir: docs/theme # If you have overrides, specify where to find them
  palette:
    scheme: dracula # This is how to enables the Dracula theme for dark. For light, it will use default Material with some tweaks.
    primary: deep purple # Primary colors
    accent: deep purple # accent color
```

The following Material primary/accent colors map to actual Dracula colors:

Material    | Dracula
----------- | -------
red         | red
pink        | pink
purple      | purple
deep-purple | purple
blue        | blue
indigo      | blue
light-blue  | blue
cyan        | cyan
teal        | cyan
green       | green
light-green | green
lime        | green
yellow      | yellow
amber       | yellow
orange      | orange
deep-orange | orange

## Sponsor Footer Link

If you'd like to add the sponsor heart in the footer, add your sponsor link under the MkDocs theme options like so.

```yml
theme:
  pymdownx:
    sponsor: "https://github.com/sponsors/facelessuser"
```

## Mermaid Support

Mermaid support is baked in. Simply add the Mermaid script to your MkDocs config:

```yml
extra_javascript:
  - https://unpkg.com/mermaid@8.8.4/dist/mermaid.min.js
```

If you do not like our default setup, you are free to modify it. Simply provide a script file before before you include
Mermaid with the new config:

```yml
extra_javascript:
  - my_mermaid_config.js
  - https://unpkg.com/mermaid@8.8.4/dist/mermaid.min.js
```
Also, setup your Mermaid diagrams:

```yml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        # Mermaid diagrams
        - name: diagram
          class: diagram
          format: !!python/name:pymdownx.superfences.fence_code_format
```

Then you can specify your Mermaid diagrams in `diagram` code blocks:

````
```diagram
...
```
````

Mermaid setups are provided per scheme. You can see the setup [here](https://github.com/facelessuser/pymdown-extensions/blob/main/docs/src/js/material-extra-3rdparty.js).
if you are trying to override them.

## MathJax/KaTeX

Again, MathJax and KaTeX support is baked in. Simply add the MathJax script(s) to your MkDocs config:

MathJax:

```yml
extra_javascript:
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

KaTeX:

```yml
extra_javascript:
  - https://cdn.jsdelivr.net/npm/katex@0.13.18/dist/katex.min.js
```

Lastly, setup Arithmatex:

```yml
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true # Must use generic mode
      block_tag: 'pre' # We wrap block math in `<pre>` to avoid issues with MkDocs minify HTML plugin: https://github.com/byrnereese/mkdocs-minify-plugin
```

If you do not like the default MathJax setup, add your own config before MathJax script:

```yml
extra_javascript:
  - my_mathjax_config.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Smart eInvoicing GovHack'
copyright = u'2016, Chris Gough'
author = u'Chris Gough'
version = u'0.1'
release = u'0.1'
language = None
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv'
]
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'SmartEinvoicingGovHack'
latex_elements = {
     'papersize': 'a4paper',
     'pointsize': '10pt',
     # 'preamble': '',
     # 'figure_align': 'htbp',
}
handle = 'SmartEinvoicingGovHack'
description = 'dumb untrusted gateways that journal to blockchain'

latex_documents = [
    (master_doc, '{}.tex'.format(handle), project,
     u'Chris Gough', 'manual'),
]
man_pages = [
    (master_doc, handle.lower(), project, [author], 1)
]
texinfo_documents = [
    (master_doc, handle, project,
     author, handle, description,
     'Miscellaneous'),
]
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}

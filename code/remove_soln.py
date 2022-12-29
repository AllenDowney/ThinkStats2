import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
filenames = glob('chap*soln.ipynb')

text = '# Solution'
replacement = ''

# Search through each notebook
for filename in filenames:
    ntbk = nbf.read(filename, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        # remove tags
        if 'tags' in cell['metadata']:
            tags = cell['metadata']['tags']
            cell['metadata']['tags'] = []

            # Remove code from fill-in cells
            if 'fill-in' in tags:
                cell['source'] = ''

        # remove output
        if 'outputs' in cell:
            cell['outputs'] = []

        # remove solutions
        if cell['source'].startswith(text):
            cell['source'] = replacement

    outname = filename.replace('soln', 'ex')
    nbf.write(ntbk, outname)

# coding: utf-8

import glob

def match_files(dirname, extensions, recursive=True):
    '''
    Find files in a dir with specified extensions
    '''
    results = []
    for ext in extensions:
        results.extend(glob.glob(dirname+ '/**/*.' + ext, recursive=recursive))
    return results


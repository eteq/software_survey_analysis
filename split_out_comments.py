from __future__ import print_function
"""
This script splits out the comments from the csv file as downloaded from the
survey document, randomizing their order to anonymize the comments.
"""
import numpy as np
from astropy.io import ascii

readfn = 'questionaire_data.csv'
writefn = 'questionaire_data_nocomments.csv'
commfn = 'randomized_comments.txt'

data = ascii.read(readfn, comment='#', delimiter=',')

commentdata = data['career', 'comment']
commentdata = commentdata[np.random.permutation(len(commentdata))]
del commentdata.meta['comments']

del data['comment']

print('Writing data to', writefn)
data.write(writefn, comment='#', delimiter=',', format='csv')

print('Writing comments to', commfn)
commentdata.write(commfn, comment='#', delimiter=',', format='csv')

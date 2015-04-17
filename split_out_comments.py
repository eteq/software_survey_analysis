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






"""
comms = []

with open(readfn) as fr:
    for l in fr:
        if not l.startswith('#'):
            headers = l.strip().split(', ')
            break

comment_idx = headers.index('comment')
career_idx = headers.index('career')

print('Writing data to', writefn)
with open(readfn) as fr:
    with open(writefn, 'w') as fw:
        for l in fr:
            lsplit = l.split(',')

            comms.append((lsplit[career_idx], lsplit[comment_idx]))

            del lsplit[comment_idx]

            towrite = ','.join(lsplit)

            fw.write(towrite)
            if l.endswith('\n') and not towrite.endswith('\n'):
                fw.write('\n')

random.shuffle(comms)

print('Writing comments to', commfn)
with open(commfn, 'w') as fcomm:
    fcomm.write('career, comment\n')
    for comm in comms:
        fcomm.write(','.join(comm))
        fcomm.write('\n')
"""

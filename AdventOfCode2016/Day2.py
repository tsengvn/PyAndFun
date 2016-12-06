pad = [[1,2,3],[4,5,6],[7,8,9]]

x = [x for x in pad if 3 in x][0]
print 'The index is (%d,%d)' %( pad.index(x), x.index(3) )



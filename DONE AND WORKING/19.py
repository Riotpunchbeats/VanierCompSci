""""99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero."""

for n in range(99, 0, -1):
    print n, 'bottle%s of beer on the the wall.' % ('s', '')[n == 1]
    print n, 'bottle%s of beer.' % ('s', '')[n == 1]
    print 'Take one down, pass it around.'
    print n - 1, 'bottle%s of beer on the wall.\n' % ('s', '')[n - 1 == 1]

# cara 1
print('Hello world 1')

# cara 2
a = 'Hello world 2'
print('%s' % a)

# cara 3
import sys

if len(sys.argv) > 1 :
    print ('%s' % sys.argv[1])
else:
    print ('Hello world 3')

# cara 4
salam = input('masukkan kata: ')
print ('%s' % salam)

filename = input('masukkan path file: ')
try:
    file = open(filename, 'r')
    isi_file = file.readlines()
    file.close()
    
    for tiap_baris in isi_file:
        print (tiap_baris)
    
except IOError:
    print('Terjadi kesalahan: {}'.format(str(diag)))

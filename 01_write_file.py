filename = input('masukkan path file: ')
try:
    file = open(filename, 'w')
    isi_file = raw_input('masukkan kata yg ingin ditulis ke file: ')
    file.write('%s\n' % (isi_file))
    file.write('saya tulis lagi\n')
    file.close()
    
except IOError as diag:
    print ('Terjadi kesalahan: {}'.format(str(diag)))

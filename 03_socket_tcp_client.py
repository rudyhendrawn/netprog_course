import socket
import errno

# deklarasi variabel
IP = '127.0.0.1'
PORT = 77
PESAN = 'test 1 2 3'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    '''
    program client mencoba terhubung ke server
    apabila gagal, akan ditampilkan sesuai error
    pada bagian except
    '''
    sock.connect((IP,PORT))
    
    '''
    karena server mengirim data terlebih dahulu,
    maka lebih baik receive dulu supaya tidak error
    '''
    print('pesan dari server: {}'.format(sock.recv(1024)))
    
    '''
    setelah menerima pesan dari server,
    maka giliran client yg mengirim pesan ke server
    '''
    sock.send(PESAN)

    '''
    apabila terjadi error, maka akan dialihkan
    ke bagian ini supaya program tidak terhenti
    '''
except socket.error as e:
    if e.errno == errno.ECONNREFUSED:
        print('gagal melakukan koneksi ke server')
    elif e.errno ==  errno.ECONNRESET:
        print('koneksi ke server terputus')
    elif e.errno == errno.ETIMEDOUT:
        print('koneksi timeout!')
    else:
        print(e)
except Exception as e:
    print(e)
finally:
    '''   
    close socket
    biasakan membuat program selesai dengan tidak meninggalkan jejak di memori
    seharusnya tanpa perintah close juga sudah otomatis dicek oleh python,
    tapi tidak ada salahnya belajar membuat program yang baik.
    '''
    sock.close()        

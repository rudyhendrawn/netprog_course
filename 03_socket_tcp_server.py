import socket
import errno

# deklarasi variabel
IP = '' # atau bisa digunakan IP = '0.0.0.0.0'
PORT = 77 # cek port yg tersedia menggunakan netstat

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    '''
    bind socket; 
    biasanya disini error apabila port yg diset 
    sudah digunakan oleh program lain.
    cek pakai netstat
    '''
    sock.bind((IP,PORT))
    print('Server binding ke {} : {}'.format(IP,PORT))

    '''
    listen socket
    100 adalah jumlah backlog, atau jumlah antrean koneksi yg diperbolehkan
    minimal 0, maksimal tergantung spek komputer(CPU usage, RAM usage, & Ethernet Card usage).
    harusnya 100 sudah cukup. 
    '''
    sock.listen(100)
    print('Server sedang listening...')

    '''
    saat program server menerima koneksi dari client
    '''
    while True:
        try:
            '''
            ada koneksi yang masuk ke server
            '''
            con, addr = sock.accept()
            '''
            biasakan saat mendapatkan coneksi dari client,
            sapa terlebih dahulu client nya
            '''
            con.send('Selamat datang di Server kami')
            print('Pesan dari client: {}'.format(con.recv(1024)))
        
            '''
            apabila terjadi error, maka akan dialihkan
            ke bagian ini supaya program tidak terhenti
            '''
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                print('gagal melakukan koneksi balik')
            elif e.errno ==  errno.ECONNRESET:
                print('koneksi ke client terputus')
            elif e.errno == errno.ETIMEDOUT:
                print('koneksi timeout!')
            else:
                print(e)
            '''
            except ini cuma berlaku untuk posix system
            entah kenapa cmd windows tidak merespon
            apabila user menekan Ctrl+C
            '''
        except KeyboardInterrupt:
            print('Server dimatikan!\n')
            con.close()
            break

    '''   
    close socket
    biasakan membuat program selesai dengan tidak meninggalkan jejak di memori
    seharusnya tanpa perintah close juga sudah otomatis dicek oleh python,
    tapi tidak ada salahnya belajar membuat program yang baik.
    '''
    sock.close()
    
    '''
    Exception untuk perintah bind
    ''' 
except socket.error as e :
    if e.errno == errno.EADDRINUSE:
        print('gagal bind, port tidak tersedia atau digunakan oleh program lain')

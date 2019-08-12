import multiprocessing as mp
import socket



def client(e,**kwargs):
    AF = kwargs['af']
    addr = kwargs['addr']
    msgs = 0

    print('Receiving messages...')

    sock = socket.socket(AF, socket.SOCK_STREAM)
    sock.connect(addr)

    while e.is_set():
        data = sock.recv(32)
        msgs += 1

    sock.close()

    print('Received {} messages.'.format(msgs))


def server(e,**kwargs):
    AF = kwargs['af']
    addr = kwargs['addr']

    duration = 5
    end = time.time() + duration

    sock = socket.socket(AF, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(0)

    print("Server ready")

    conn, _ = sock.accept()

    while (time.time() < end) and e.is_set():
        conn.send(b'Hello there!')

    conn.close()
    print('*** Server is done ***')
    e.clear()




kw = {
    'af': socket.AF_UNIX,
    'addr': '/tmp/uds_test'
}

# if the file already exists, you will get an address in use error
if os.path.exists(kw['addr']):
    os.remove(kw['addr'])

s = mp.Process(target=server, args=(event,), name="server", kwargs=kw)
s.start()
print('Started {}[{}]'.format(s.name, s.pid))

sleep(10)
s.terminate()

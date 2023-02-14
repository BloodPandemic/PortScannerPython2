import socket
import time
class PortScanner:
    def __init__(self, address, port, first, last):
        self.port = port
        self.first = first
        self.last = last
        self.address = address
    def check_port(self):
        try:
            if self.first is None and self.last is None:
                time.sleep(1)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((self.address, self.port))
                with open("output.txt", "w") as f:
                    if result == 0:
                        f.write(f'{self.address}:{self.port} is open\n')
                f.close()
                sock.close()
            elif self.port is None:
                with open("output.txt", "w") as f:
                    for i in range(self.first, self.last):
                        time.sleep(2)
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(5)
                        result = sock.connect_ex((self.address, i))
                        if result == 0:
                            f.write(f'{self.address}:{i} is open\n')
                        sock.close()
                f.close()
            else:
                print("Enter either one port or a range")
                exit()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='''simple port scanner
                                     usage --> python portScanner.py --address <ip> --port <port> --first <first> --last <last>''')
    parser.add_argument('--address', type=str, required=True, help='specify the address')
    parser.add_argument('--port', type=int, required=False, help='specify only one port')
    parser.add_argument('--first', type=int, required=False, help='enter the first port in the range if you want to select a range')
    parser.add_argument('--last', type=int, required=False, help='Enter the last port in the range')
    args = parser.parse_args()
    pS = PortScanner(args.address, args.port, args.first, args.last)
    pS.check_port()

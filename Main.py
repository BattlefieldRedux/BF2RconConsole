__author__ = 'Scott Davey'

from BFHRCONPython.BFHServer import *
import socket


def menu():
    print("=== BFH/BFP4F/BF2 SERVER CONSOLE ===")
    print("Made by Scott Davey - www.scottdavey.me - Type in qq to exit.")
    print("Use connect [ip] [port] [password] to connect to a server.")
    print()
    quit_ = False
    while not quit_:
        cmd = input(">>> ")
        if cmd == "qq":
            try:
                server.query("logout")
                server.close()
            except NameError: pass
            quit_ = True
        elif cmd[0:7] == "connect":
            args = cmd.split()
            del args[0]
            if len(args) < 3:
                print("USAGE: connect [ip] [port] [password]")
            else:
                server = BFHServer(args[0], args[1], args[2])
                try:
                    s = server.connect()
                    if s: print("Authentication successful, rcon ready.")
                    else: print("Authentication failed.")
                except socket.error:
                    print("ERROR: Could not connect to server.")
        else:
            try: print(server.query(cmd, True, False))
            except NameError: print("You must be connected to a server!")
            except socket.error: print("Socket has been closed. Reconnect.")

if __name__ == "__main__":
    menu()
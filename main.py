import socket

def get_ip_by_hostname():
    """Get IP and hostname"""
    hostname = input("Please enter website hostname (e.g google.com): ")
    try:
        return f"Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}"
    except socket.gaierror as error:
        return f"Invalid hostname - {error}"

def main():
    print(get_ip_by_hostname())

if __name__ == "__main__":
    main()
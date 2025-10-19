# Port Scanner
# Given an IP address or Domain name scan a range of ports inputted by user
# Resources: geeksforgeeks socket-programming-python
#https://realpython.com/ref/stdlib/socket/


import socket  # Library that allows sending and receiving network data
from datetime import datetime  # Module allows me to grab date/timestamp
import argparse  # Module to handle command line arguments
common_ports = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP Proxy"
}
def parse_arguments():
    parser = argparse.ArgumentParser(description = "Port Scanner")
    parser.add_argument("-t", "--target", required = True, 
                        help = "Target IP address or domain name to scan")
    parser.add_argument("-p", "--ports", required = True,
                        help = "Port range to scan in the format 'start-end' (e.g., 20-80)")
    parser.add_argument("-to", "--timeout", type = float, default = 1.0,
                        help = "Timeout in seconds for each port scan (default: 1.0)")
    parser.add_argument("-o", "--output", default = None, 
                        help = "Output file to save results (default: None)")
    parser.add_argument("-e", "--email", default= None,
                        help = "Email address to send results to (default: None)")
    return parser.parse_args()
# Function to scan a port
def scan_port(host, port, timeout):
    sock = socket.socket()
    sock.settimeout(timeout)  # Will stop after one second to be faster
    try:
        sock.connect((host, port))  # When successful return True
        return True
    except socket.error:
        return False
def main():
    args = parse_arguments()
    target_input = args.target
    timeout = args.timeout
    output_file = args.output
    try:
        start_port, end_port = map(int, args.ports.split('-'))
    except ValueError:
        print("Invalid port range format. Use 'start-end' (e.g., 20-80).")
        exit(1)
    try:
        target_ip = socket.gethostbyname(target_input)  # This handles both website names and IP addresses as input
    except socket.gaierror:
        print("Invalid target. Please enter a valid IP address or domain name.")
        exit(1)
    start_time = datetime.now()  # Calls current date and time to be printed for user
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"Scan started at: {start_time}\n")
    print("Scanning started at: ", start_time)
    for port in range(start_port, end_port + 1):  # Loop through the given range by user, and scan each port
        if scan_port(target_ip, port, timeout):
            service = common_ports.get(port, "Unknown Service")
            result = f"Port {port} is open ({service})"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
        else:
            result = f"Port {port} is closed"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
    finish_time = datetime.now()
    final_message = f"Scan finished at: {finish_time}\nTotal duration: {finish_time - start_time}\n"
    print(final_message)
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"Scan finished at: {finish_time}\n")
            f.write(f"Total duration: {finish_time - start_time}\n")
    

if __name__ == "__main__":
    main()
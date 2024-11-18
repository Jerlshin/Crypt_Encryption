# Network Security Tools and Commands in Linux

## 1. Packet Analysis
- `tcpdump`: Captures and analyzes network traffic.
- `wireshark`: GUI tool for deep packet inspection and protocol analysis.

## 2. Network Scanning and Vulnerability Assessment
- `nmap`: Scans for open ports and services, detects operating systems.
- `zenmap`: GUI version of nmap.
- `nessus`: Advanced vulnerability scanner (requires installation).
- `nikto`: Scans web servers for vulnerabilities and misconfigurations.

## 3. Firewall and IP Filtering
- `iptables`: Configures network packet filtering rules.
- `ufw`: Simplified frontend for iptables.
- `firewalld`: Dynamic firewall management tool.

## 4. Network Monitoring
- `netstat`: Displays network connections, routing tables, and statistics.
- `ss`: Faster replacement for netstat.
- `iftop`: Displays bandwidth usage by IPs in real time.
- `nethogs`: Shows bandwidth usage by processes.

## 5. Intrusion Detection and Prevention
- `snort`: Packet-based intrusion detection system.
- `suricata`: Network threat detection, similar to Snort but with multithreading.
- `fail2ban`: Blocks IPs showing malicious signs (e.g., failed login attempts).

## 6. Password Attacks
- `hydra`: Brute-forces login credentials on various services.
- `john`: Password cracker for hashed passwords.

## 7. Secure File Transfers
- `scp`: Securely copies files over SSH.
- `rsync`: Synchronizes files and directories over the network with SSH encryption.
- `sftp`: Secure file transfer protocol using SSH.

## 8. Cryptographic Tools
- `openssl`: Toolkit for SSL/TLS and cryptographic operations.
- `gpg`: Encrypts and signs files with GNU Privacy Guard.

## 9. DNS Analysis
- `dig`: Queries DNS servers for records.
- `nslookup`: Resolves DNS names to IP addresses.

## 10. Network Configuration and Troubleshooting
- `ping`: Tests connectivity to a host.
- `traceroute`: Shows the route packets take to a destination.
- `mtr`: Combines ping and traceroute for real-time network diagnostics.
- `arp`: Displays or modifies the ARP table.
- `ethtool`: Displays or modifies Ethernet device settings.
- `ip`: Replaces `ifconfig` for managing IP addresses and interfaces.
- `netcat (nc)`: Simple tool for reading/writing data over networks.

## 11. Proxy and Tunneling
- `ssh`: Secure shell for remote connections and tunneling.
- `proxychains`: Routes traffic through proxies like TOR.
- `tor`: Anonymizes network traffic.
- `stunnel`: Adds SSL encryption to insecure services.

## 12. Exploitation Frameworks
- `metasploit`: Framework for developing and executing exploits.
- `msfconsole`: Command-line interface for Metasploit.

## 13. Log Analysis
- `logwatch`: Analyzes and summarizes system logs.
- `grep`: Searches specific patterns in log files.

## 14. Wireless Network Security
- `aircrack-ng`: Suite for auditing Wi-Fi networks.
- `kismet`: Wireless network detector and packet sniffer.
- `reaver`: Brute-forces WPS pins on wireless routers.

## 15. Forensics and Packet Replay
- `tcpreplay`: Replays captured packet files to a network.
- `foremost`: Recovers files based on their headers, footers, and structure.

## 16. VPN and Tunneling
- `openvpn`: Secure virtual private network software.
- `wireguard`: Modern, efficient VPN solution.

## 17. Miscellaneous
- `curl`: Transfers data from or to a server, supporting many protocols.
- `wget`: Downloads files from the web.
- `whois`: Fetches domain information.
- `hping`: Assembles and sends custom TCP/IP packets.


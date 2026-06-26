from tools.full_sniff import FullSniff
from tools.https_sniff import HttpsSniff
from tools.tcp_sniff import TcpSniff
from tools.udp_sniff import UdpSniff
from tools.arp_sniff import ArpSniff
from tools.icmp_sniff import IcmpSniff
from tools.flag_sniff import FlagSniff
from tools.ssh_sniff import SshSniff
from rich.console import Console

def OutPut():
    while True:
        try:
            choice = input("[+] ")
        except KeyboardInterrupt:
            break

        if choice == "0":
            FullSniff()
        elif choice == "1":
            SshSniff()
        elif choice == "2":
            TcpSniff()
        elif choice == "3":
            UdpSniff()
        elif choice == "4":
            ArpSniff()
        elif choice == "5":
            IcmpSniff()
        elif choice == "6":
            FlagSniff()
        elif choice == "7":
            HttpsSniff()
        else:
            console = Console()
            console.print("Invalid choice, try again.", style="yellow")
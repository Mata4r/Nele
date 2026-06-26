from scapy.all import sniff, IP, TCP
from rich.console import Console

def SshSniff():
    try:
        interface = input("[Iface] ")
        console = Console()
        console.print("[*]Capture begin...","yellow")

        sniff_pair = sniff(iface=interface,
                           promisc=True,
                           store=False,
                           filter="tcp",
                           prn=lambda pkt: 
        (print(f"[SSH] {pkt[IP].src} > {pkt[IP].dst}") if TCP in pkt and pkt[TCP].sport == 22 else None))
    except:
        console.print(f"An error occurred: No such interface exists: {interface}",style="yellow")

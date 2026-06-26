from scapy.all import*
from rich.console import Console

def ArpSniff():
    try:
        Interface = input("[Iface] ") 
        console = Console()
        console.print("[*]Capture begin...",style="yellow")

        sniff_pair = sniff(iface=Interface,
                           promisc=True,
                           store=False,
                           filter="arp",
                           prn=lambda x: x.summary())
    except:
        console.print(f"An error occurred: No such interface exists: {Interface}",style="yellow")

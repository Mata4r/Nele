from scapy.all import *
from rich.console import Console

def UdpSniff():
    try:
        Interface = input("[Iface] ")
        console = Console()
        console.print("[*]Capture begin...","yellow")

        sniff_pair = sniff(iface=Interface,
                           promisc=True,
                           store=False,
                           filter="udp",
                           prn=lambda x: x.summary())
    except Exception:
        console.print(f"An error occurred: No such interface exists: {Interface}",style="yellow")

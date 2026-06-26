from scapy.all import *
from rich.console import Console

def FullSniff():
    try:
        Interface = input("[Iface] ")
        Filter = input("[Fliter] ")
        console = Console()
        console.print("[*]Capture begin...",style="yellow")

        Filter_lowering = Filter.lower()

        sniff_pair = sniff(iface=Interface,
                           promisc=True,
                           store=False,
                           filter=Filter_lowering,
                           prn=lambda x: x.summary())
    except Exception:
        console.print(f"An error occurred: No such interface exists: {Interface}",style="yellow")

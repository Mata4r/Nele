from scapy.all import*
from rich.console import Console

def TcpSniff():
    try:
        Interface = input("[Iface] ")
        console = Console()
        print("[*]Capture begin...","yellow")

        sniff_pair = sniff(iface=Interface,
                           promisc=True,
                           store=False,
                           filter="tcp",
                           prn=lambda x: x.summary())
    except:
        console.print(f"An error occurred: No such interface exists: {Interface}",style="yellow")

from scapy.all import sniff, IP, TCP
from rich.console import Console

def FlagSniff():
    try:
        interface = input("[Iface] ")
        console = Console()
        console.print("[*]Capture begin...",style="yellow")

        sniff_pair = sniff(iface=interface,
                           promisc=True,
                           store=False,
                           filter="tcp",
                           prn=lambda pkt: 
                           (print(f"[SYN] {pkt[IP].src} > {pkt[IP].dst} port:{pkt[TCP].dport}") if TCP in pkt and pkt[TCP].flags == 0x02 else 
                            print(f"[SYN-ACK] {pkt[IP].src} > {pkt[IP].dst} port:{pkt[TCP].dport}") if TCP in pkt and pkt[TCP].flags == 0x12 else 
                            print(f"[ACK] {pkt[IP].src} > {pkt[IP].dst} port:{pkt[TCP].dport}") if TCP in pkt and pkt[TCP].flags == 0x10 else
                            print(f"[RST] {pkt[IP].src} > {pkt[IP].dst} port:{pkt[TCP].dport}") if TCP in pkt and pkt[TCP].flags == 0x04 else None))
    except:
        console.print(f"An error occurred: No such interface exists: {interface}",style="yellow")

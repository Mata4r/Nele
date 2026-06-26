from scapy.all import IP, TCP, sniff
from rich.console import Console

def HttpsSniff():
    try:
        Interface = input("[Iface] ")
        console = Console()
        print("[*]Capture begin...",style="yellow")

        sniff_pair = sniff(iface=Interface,
                           promisc=True,
                           filter="tcp or udp",
                           store=False,
                           prn=lambda pkt:
                           (print(f"[HTTPS] {pkt[IP].src} > {pkt[IP].dst} ") if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt[TCP].dport == 443 else
                            print(f"[HTTP] {pkt[IP].src} > {pkt[IP].dst} ") if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt[TCP].dport == 80 else None))
    except Exception:
        console.print(f"An error occurred: No such interface exists: {Interface}",style="yellow")

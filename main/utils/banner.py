from scapy.all import*
from rich.console import Console
import pyfiglet

def Banner():
    print()
    banner = pyfiglet.figlet_format("NELE SCAN" , font="ansi_shadow", )
    print(banner)
    console = Console()
    console.print("┃Developed by @Mata4r", style="#363636")

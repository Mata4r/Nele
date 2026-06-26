from scapy.all import*
from rich.console import Console
import pyfiglet

def Banner():
    print()
    banner = pyfiglet.figlet_format("NELE SCAN" , font="ansi_shadow", )
    console = Console()
    console.print(banner, style="#5800AA")
    console.print("┃Developed by @Mata4r", style="#363636")
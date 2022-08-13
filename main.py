from __future__ import annotations

import re
import tkinter as tk
from tkinter import ttk

import wmi as wmi_lib

from element_types import InterfaceType
from gui_elements import PlaceholderEntry, HelpLabel, SelectMenu


IP_PATTERN = re.compile(
    r'\b('
    r'(?:1?[0-9]{1,2}|2(?:[0-4][0-9]|5[0-5]))\.'
    r'(?:1?[0-9]{1,2}|2(?:[0-4][0-9]|5[0-5]))\.'
    r'(?:1?[0-9]{1,2}|2(?:[0-4][0-9]|5[0-5]))\.'
    r'(?:1?[0-9]{1,2}|2(?:[0-4][0-9]|5[0-5]))'
    r')(?:/([1-2]?[0-9]|3[0-2]))?'
    r'\b$'
)


def get_mask(value: int) -> str:
    if not (0 <= value <= 32):
        raise ValueError("Network mask can only range between 1 and 32")
    parts = []
    m, n = divmod(value, 8)
    for i in range(m):
        parts.append('255')
    if n > 0:
        parts.append(str((1 << 8) - (1 << 8-n)))
    while len(parts) < 4:
        parts.append('0')
    return '.'.join(parts)


wmi = wmi_lib.WMI()
root = tk.Tk()
root.title("IP Changer (by DevilXD)")
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")
# Gather and display a list of interfaces
raw_interfaces: list[InterfaceType] = wmi.Win32_NetworkAdapterConfiguration(IPEnabled=True)
interfaces: dict[str, InterfaceType] = {i.Description: i for i in raw_interfaces}
HelpLabel(
    frame, text="Interface: ", tooltip="Select the interface to interract with."
).grid(column=0, row=0)
nic_menu: SelectMenu[InterfaceType] = SelectMenu(frame, options=interfaces)
nic_menu.grid(column=1, row=0, sticky="ew")
ipaddress = PlaceholderEntry(frame, placeholder="IP Address")
ipaddress.grid(column=0, row=1, sticky="ew")


def ipset():
    nic = nic_menu.get()
    if nic is None:
        return
    ipmask = ipaddress.get()
    if (match := IP_PATTERN.match(ipmask)) is None:
        return
    ip = match.group(1)
    raw_mask = match.group(2)
    if raw_mask is None:
        raw_mask = 24
    subnetmask = get_mask(int(raw_mask))
    gateway = "192.168.0.1"
    print(ip, subnetmask, gateway)
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
    # nic.EnableDHCP()


ttk.Button(frame, text="Set", command=ipset).grid(column=1, row=1)
root.mainloop()

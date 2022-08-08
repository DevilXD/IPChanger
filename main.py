from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Any

import wmi as wmi_lib

from gui_elements import PlaceholderEntry, HelpLabel


wmi = wmi_lib.WMI()
root = tk.Tk()
root.title("IP Changer (by DevilXD)")
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")
# Gather and display a list of interfaces
raw_interfaces = wmi.Win32_NetworkAdapterConfiguration(IPEnabled=True)
interfaces: dict[str, Any] = {i.Description: i for i in raw_interfaces}
HelpLabel(
    frame, text="Interface: ", tooltip="Select the interface to interract with."
).grid(column=0, row=0)
nic_var = tk.StringVar(frame)
tk.OptionMenu(frame, nic_var, *interfaces.keys()).grid(column=1, row=0, sticky="ew")
ipaddress = PlaceholderEntry(frame, placeholder="IP Address")
ipaddress.grid(column=0, row=1, sticky="ew")


def ipset():
    nic = interfaces[nic_var.get()]
    ip = ipaddress.get()
    if not ip:
        return
    print(ip)
    # subnetmask = "255.255.255.0"
    # gateway = "192.168.0.1"
    # nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    # nic.SetGateways(DefaultIPGateway=[gateway])
    # nic.EnableDHCP()


ttk.Button(frame, command=ipset).grid(column=1, row=1)
root.mainloop()

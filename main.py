import tkinter as tk
from tkinter import ttk
from typing import Any

import wmi as wmi_lib

from gui_elements import PlaceholderEntry


wmi = wmi_lib.WMI()
root = tk.Tk()
root.title("IP Changer (by DevilXD)")
frame = ttk.Frame(root, padding=20)
# Gather and display a list of interfaces
raw_interfaces = wmi.Win32_NetworkAdapterConfiguration()
interfaces: dict[str, Any] = {i.Description: i for i in raw_interfaces}
ttk.Label(frame, text="Interface: ").grid(column=0, row=0)
nic_var = tk.StringVar(frame)
tk.OptionMenu(frame, nic_var, *interfaces.keys()).grid(column=1, row=0, sticky="ew")
ipaddress = PlaceholderEntry(frame, placeholder="IP Address")
ipaddress.grid(column=0, row=0, sticky="ew")


def ipset(nic):
    wmi.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    ip = "192.168.0.11"
    subnetmask = "255.255.255.0"
    gateway = "192.168.0.1"
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
    nic.EnableDHCP()

    ipaddress.get()


ttk.Button(frame, command=...)

root.mainloop()

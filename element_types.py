from __future__ import annotations

from typing import Any

import wmi
import win32com


class WMIObjectType(wmi._wmi_object):
    id: str
    keys: list[str]
    methods: list[str]
    is_association: bool
    properties: list[str]
    qualifiers: dict[str, Any]
    ole_object: win32com.client.CDispatch
    property_map: dict[str, wmi._wmi_object]
    associated_classes: dict[str, wmi._wmi_class]

    def derivation(self) -> tuple[str]:
        """
        Return a tuple representing the object derivation for this object,
        with the most specific object first:

            pp0 = wmi.WMI().Win32_ParallelPort()[0]
            print(' <- '.join(pp0.derivation()))
        """

    def associators(
        self, wmi_association_class: str = "", wmi_result_class: str = ""
    ) -> list[wmi._wmi_object]:
        """
        Return a list of objects related to this one, optionally limited
        either by association class(ie the name of the class which relates
        them) or by result class(ie the name of the class which would be
        retrieved)::

            c = wmi.WMI()
            pp = c.Win32_ParallelPort()[0]

            for i in pp.associators(wmi_association_class="Win32_PortResource"):
                print(i)

            for i in pp.associators(wmi_result_class="Win32_PnPEntity"):
                print(i)
        """

    def path(self) -> str:
        """
        Return the WMI URI to this object. Can be used to determine the path relative
        to the parent namespace:

            pp0 = wmi.WMI().Win32_ParallelPort()[0]
            print(pp0.path().RelPath)
        """

    def references(self, wmi_class: str = "") -> list[wmi._wmi_object]:
        ...

    def set(self, **kwargs) -> None:
        """
        Set several properties of the underlying object at one go. This is particularly useful
        in combination with the new() method below. However, an instance which has been spawned
        in this way won't have enough information to write pack,
        so only try if the instance has a path.
        """

    def wmi_property(self, property_name: str) -> wmi._wmi_property:
        """
        Return the cached object representing one property of this object.
        """

    def put(self) -> None:
        """
        Push all outstanding property updates back to the WMI database.
        """


class InterfaceType(WMIObjectType):
    ArpAlwaysSourceRoute: None
    ArpUseEtherSNAP: None
    Caption: str
    DHCPEnabled: bool
    DHCPLeaseExpires: str  # '20220816124219.000000+120'
    DHCPLeaseObtained: str  # '20220813124219.000000+120'
    DHCPServer: str  # '192.168.100.1'
    DNSDomain: None
    DNSDomainSuffixSearchOrder: tuple[Any]
    DNSEnabledForWINSResolution: bool
    DNSHostName: str
    DNSServerSearchOrder: tuple[str]  # ('192.168.100.1',)
    DatabasePath: str
    DeadGWDetectEnabled: bool
    DefaultIPGateway: tuple[str]  # ('192.168.100.1', 'fe80::1')
    DefaultTOS: None
    DefaultTTL: int
    Description: str
    DomainDNSRegistrationEnabled: bool
    ForwardBufferMemory: None
    FullDNSRegistrationEnabled: bool
    GatewayCostMetric: tuple[int]  # (0, 256)
    IGMPLevel: None
    IPAddress: tuple[str]  # ('192.168.100.4', 'fe80::8bf:21e3:d644:b313')
    IPConnectionMetric: int
    IPEnabled: bool
    IPFilterSecurityEnabled: bool
    IPPortSecurityEnabled: None
    IPSecPermitIPProtocols: tuple[Any]
    IPSecPermitTCPPorts: tuple[Any]
    IPSecPermitUDPPorts: tuple[Any]
    IPSubnet: tuple[str]  # ('255.255.255.0', '64')
    IPUseZeroBroadcast: None
    IPXAddress: None
    IPXEnabled: None
    IPXFrameType: None
    IPXMediaType: None
    IPXNetworkNumber: None
    IPXVirtualNetNumber: None
    Index: int
    KeepAliveInterval: None
    KeepAliveTime: None
    MACAddress: str  # '60:3B:38:1F:57:AC'
    MTU: None
    NumForwardPackets: None
    PMTUBHDetectEnabled: bool
    PMTUDiscoveryEnabled: bool
    ServiceName: str
    SettingID: str  # '{9B55CFBB-7463-49FD-BAB9-8F73A82D6321}'
    TcpMaxConnectRetransmissions: None
    TcpMaxDataRetransmissions: None
    TcpNumConnections: None
    TcpUseRFC1122UrgentPointer: None
    TcpWindowSize: None
    TcpipNetbiosOptions: int
    WINSEnableLMHostsLookup: bool
    WINSHostLookupFile: None
    WINSPrimaryServer: None
    WINSScopeID: str
    WINSSecondaryServer: None

    """
    General return codes:

    0: Successful completion, no reboot required.
    1: Successful completion, reboot required.
    64: Method not supported on this platform.
    65: Unknown failure.
    66: Invalid subnet mask.
    67: An error occurred while processing an instance that was returned.
    68: Invalid input parameter.
    69: More than five gateways specified.
    70: Invalid IP address.
    71: Invalid gateway IP address.
    72: An error occurred while accessing the registry for the requested information.
    73: Invalid domain name.
    74: Invalid host name.
    75: No primary or secondary WINS server defined.
    76: Invalid file.
    77: Invalid system path.
    78: File copy failed.
    79: Invalid security parameter.
    80: Unable to configure TCP/IP service.
    81: Unable to configure DHCP service.
    82: Unable to renew DHCP lease.
    83: Unable to release DHCP lease.
    84: IP not enabled on adapter.
    85: IPX not enabled on adapter.
    86: Frame or network number bounds error.
    87: Invalid frame type.
    88: Invalid network number.
    89: Duplicate network number.
    90: Parameter out of bounds.
    91: Access denied.
    92: Out of memory.
    93: Already exists.
    94: Path, file, or object not found.
    95: Unable to notify service.
    96: Unable to notify DNS service.
    97: Interface not configurable.
    98: Not all DHCP leases could be released or renewed.
    100: DHCP not enabled on the adapter.
    """

    def EnableDHCP(self) -> int:
        """
        The EnableDHCP WMI class method enables the Dynamic Host Configuration Protocol (DHCP)
        for service with this network adapter.
        DHCP allows IP addresses to be dynamically allocated.
        """

    def RenewDHCPLease(self) -> int:
        """
        The RenewDHCPLease WMI class method renews the IP address
        on specific DHCP-enabled network adapters.
        """

    def RenewDHCPLeaseAll(self) -> int:
        """
        The RenewDHCPLeaseAll WMI class static method renews the IP addresses
        on all DHCP-enabled network adapters.
        """

    def ReleaseDHCPLease(self) -> int:
        """
        The ReleaseDHCPLease WMI class method releases the IP address
        bound to a specific DHCP-enabled network adapter.
        """

    def ReleaseDHCPLeaseAll(self) -> int:
        """
        The ReleaseDHCPLeaseAll WMI class static method releases the IP addresses
        bound to all DHCP-enabled network adapters.
        """

    def EnableStatic(self, *, IPAddress: list[str], SubnetMask: list[str]) -> int:
        """
        The EnableStatic WMI class method enables static TCP/IP addressing
        for the target network adapter. As a result, DHCP for this network adapter is disabled.


        Parameters:
        -----------
        IPAddress: list[str]
            Lists all of the static IP addresses for the current network adapter.
            Example: 155.34.22.0.
        SubnetMask: list[str]
            Subnet masks that complement the values in the IPAddress parameter.
            Example: 255.255.0.0.
        """

    def SetGateways(self, *, DefaultIPGateway: list[str], GatewayCostMetric: int) -> int:
        """
        The SetGateways WMI class method specifies a list of gateways for routing packets
        to a subnet that is different from the subnet that the network adapter is connected to.

        Parameters:
        -----------

        DefaultIPGateway: list[str]
            List of IP addresses to gateways where network packets are routed.
        GatewayCostMetric: int
            Assigns a value that ranges from 1 to 9999, which is used to calculate the fastest
            and most reliable routes. The values of this parameter correspond with the values
            in the DefaultIPGateway parameter. The default value for a gateway is 1.
        """

    def EnableDNS(
        self,
        *,
        DNSHostName: str = '',
        DNSDomain: str = '',
        DNSServerSearchOrder: list[str] = [],
        DNSDomainSuffixSearchOrder: list[str] = [],
    ) -> int:
        """
        The EnableDNS WMI class static method enables the Domain Name System (DNS) for service.

        Parameters:
        -----------
        DNSHostName: str
            Name of the DNS host that this method enables.
            Example: "corpdns"
        DNSDomain: str
            Represents an organization name followed by a period
            and an extension that indicates the type of organization.
            Example: "microsoft.com"
        DNSServerSearchOrder: list[str]
            List of server IP addresses to query for DNS servers.
        DNSDomainSuffixSearchOrder: list[str]
            DNS domain suffix that is appended to a host name during name resolution.
            When resolving a fully qualified domain name (FQDN) from a host-only name,
            the system appends the local domain name. If the name resolution is not successful,
            the system uses the domain suffix list to create additional FQDNs in the order listed,
            and then queries DNS servers for each one.
        """

    def SetDNSDomain(self, *, DNSDomain: str) -> int:
        """
        The SetDNSDomain WMI class method allows for the setting of the DNS domain.

        Parameters:
        -----------
        DNSDomain: str
            Domain with which the DNS is associated, represented by an organization name
            followed by a period and an extension that indicates the type of organization.
            Example: "microsoft.com"
        """

    def SetDNSServerSearchOrder(self, *, DNSServerSearchOrder: list[str]) -> int:
        """
        The SetDNSServerSearchOrder WMI class method uses an array of string elements
        to set the server search order.

        Parameters:
        -----------
        DNSServerSearchOrder: list[str]
            List of server IP addresses to query for DNS servers.
            Example: 130.215.24.1 or 157.54.164.1
        """

    def SetDNSSuffixSearchOrder(self, *, DNSDomainSuffixSearchOrder: list[str]) -> int:
        """
        The SetDNSSuffixSearchOrder WMI class static method uses an array of string elements
        to set the suffix search order.

        Parameters:
        -----------
        DNSDomainSuffixSearchOrder: list[str]
            List of server suffixes to query for DNS servers.
            The registry location of the DNS suffix is:
            ``HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\Tcpip|NameServer``
            Example: "suffix1.company.com", "suffix2.company.com"
        """

    def SetDynamicDNSRegistration(
        self, *, FullDNSRegistrationEnabled: bool, DomainDNSRegistrationEnabled: bool
    ) -> int:
        """
        The SetDynamicDNSRegistration method indicates the dynamic DNS registration
        of IP addresses for this IP-bound adapter.

        Parameters:
        -----------
        FullDNSRegistrationEnabled: bool
            If true, the IP addresses for this connection is registered in DNS
            under the computer's full DNS name. The full DNS name of the computer is displayed
            on the Network Identification tab of the system Control Panel.
        DomainDNSRegistrationEnabled: bool
            If true, the IP addresses for this connection are registered under the domain name
            of this connection, in addition to being registered under the computer's full DNS name.
            The domain name of this connection is either set using the method SetDNSDomain
            or assigned by DHCP. The registered name is the host name of the computer
            with the domain name appended.
            This parameter has meaning only when FullDNSRegistrationEnabled is enabled.
            The default value is false.
        """

    def SetIPConnectionMetric(self, *, IPConnectionMetric: int) -> int:
        """
        The SetIPConnectionMetric method is used to set the routing metric
        associated with this IP-bound adapter.

        Parameters:
        -----------
        IPConnectionMetric: int
            Indicates the cost of using the configured routes for this IP-bound adapter.
            The value is weighted for those routes in the IP routing table.
            If there are multiple routes to a destination in the routing table,
            the route with the lowest metric is used. The range of valid values is 1 through 9999.
            The default value is 1.
        """

    def SetWINSServer(self, *, WINSPrimaryServer: str, WINSSecondaryServer: str) -> int:
        """
        The SetWINSServer WMI class method sets the primary and secondary
        Windows Internet Naming Service (WINS) servers on this TCP/IP-bound network adapter.
        This method is applied independently of the network adapter.

        Parameters:
        -----------
        WINSPrimaryServer: str
            IP address of the primary WINS server.
            .. Note
            Always verify the validity of this IP address when it is from an unknown source,
            or a source that you do not trust.
        WINSSecondaryServer: str
            IP address of the secondary WINS server.
            .. Note
            Always verify the validity of this IP address when it is from an unknown source,
            or a source that you do not trust.
        """

    def EnableWINS(
        self,
        *,
        DNSEnabledForWINSResolution: bool,
        WINSEnableLMHostsLookup: bool,
        WINSHostLookupFile: str = '',
        WINSScopeID: str = '',
    ) -> int:
        """
        The EnableWINS WMI class static method enables Windows Internet Naming Service (WINS)
        settings specific to TCP/IP, but independent of the network adapter.

        Parameters:
        -----------
        DNSEnabledForWINSResolution [in]
            If true, the Domain Name System (DNS) is enabled for name resolution
            over WINS resolution.
        WINSEnableLMHostsLookup [in]
            If true, local lookup files are used. Lookup files will contain mappings
            of IP addresses to host names.
        WINSHostLookupFile [in, optional]
            Lookup files that contain mappings of IP addresses to host names.
            If available, the files will be found in ``%SystemRoot%\\system32\\drivers``.
        WINSScopeID [in, optional]
            Scope identifier value that will be appended to the end of the computer's NetBIOS name.
            Systems that use the same scope identifier can communicate with this computer.
        """

    def SetTcpipNetbios(self, *, TcpipNetbiosOptions: int) -> int:
        """
        The SetTcpipNetbios method is used to set the default operation of NetBIOS over TCP/IP.

        Parameters:
        -----------
        TcpipNetbiosOptions: int
            Value that specifies the possible settings related to NetBIOS over TCP/IP.

            0: Enable Netbios via DHCP
            1: Enable Netbios
            2: Disable Netbios
        """

    def EnableIPSec(
        self,
        *,
        IPSecPermitTCPPorts: list[str],
        IPSecPermitUDPPorts: list[str],
        IPSecPermitIPProtocols: list[str],
    ) -> int:
        """
        The EnableIPSec WMI class method enables Internet Protocol security (IPsec)
        on a TCP/IP-enabled network adapter.

        Parameters:
        -----------
        IPSecPermitTCPPorts: list[str]
            List of ports to be granted access permission for TCP.
            A numeric value of 0 (zero) indicates access permission is granted for all ports.
            An empty array indicates that no ports are to be granted access permission.
        IPSecPermitUDPPorts: list[str]
            List of ports to be granted access permission for UDP.
            A numeric value of 0 (zero) indicates access permission is granted for all ports.
            An empty array indicates that no ports are to be granted access permission.
        IPSecPermitIPProtocols: list[str]
            List of protocols permitted to run over the IP.
            A numeric value of 0 (zero) indicates access permission is granted for all protocols.
            An empty array indicates that no protocols are granted access permission.
        """

    def DisableIPSec(self) -> int:
        """
        The DisableIPSec WMI class method is used to disable Internet Protocol security (IPsec)
        on this TCP/IP-enabled network adapter.
        """

    def SetIPXVirtualNetworkNumber(self, *, IPXVirtualNetNumber: str) -> int:
        """
        Sets the Internetworking Packet Exchange (IPX) virtual network number
        on the target computer system. Windows 2000 and Windows NT 3.51 or greater
        uses an internal network number for internal routing.
        The internal network number is also known as a virtual network number.
        It uniquely identifies the computer system on the network.

        Parameters:
        -----------
        IPXVirtualNetNumber: str
            The virtual network number for this system.
        """

    def SetIPXFrameTypeNetworkPairs(
        self, *, IPXNetworkNumber: list[str], IPXFrameType: list[int]
    ) -> int:
        """
        Sets the Internetworking Packet Exchange (IPX) network number/frame pairs
        for this network adapter.

        Windows 2000 and Windows NT 3.51 and higher use an IPX network number for routing purposes.
        It is assigned to each configured frame type/network adapter combination
        on your computer system. This number is sometimes referred to
        as the "external network number." It must be unique for each network segment.
        If the frame type is set to AUTO, the network number should to zero.

        Parameters:
        -----------
        IPXNetworkNumber: list[str]
            An array of characters that uniquely identify an adapter on the computer system.
            The NetWare Link (NWLink) IPX/SPX-compatible transport in Windows 2000
            and Windows NT 3.51 or higher, uses two different types of network numbers.
            This number is sometimes referred to as the External Network Number.
            It must be unique for each network segment. The values in this string list must have
            a corresponding value in the IPXFrameType parameter identifying the packet frame type
            used for this network.
        IPXFrameType: list[int]
            An integer array of frame type identifiers. The values in this array correspond
            to the elements in the IPXNetworkNumber parameter:

            0: Ethernet II
            1: Ethernet 802.3
            2: Ethernet 802.2
            3: Ethernet SNAP
            255: AUTO
        """

    def SetDatabasePath(self, *, DatabasePath: str) -> int:
        """
        The SetDatabasePath WMI class static method sets the path to the standard
        Internet database files (HOSTS, LMHOSTS, NETWORKS, and PROTOCOLS).

        Parameters:
        -----------
        DatabasePath [in]
            Valid file path to standard Internet database files (HOSTS, LMHOSTS, NETWORKS,
            and PROTOCOLS) used by the Windows Sockets interface.
        """

    def SetIPUseZeroBroadcast(self, *, IPUseZeroBroadcast: bool = False) -> int:
        """
        The SetIPUseZeroBroadcast WMI class static method is used to set IP zero broadcast usage.

        Parameters:
        -----------
        IPUseZeroBroadcast: bool
            If true, IP zero broadcast is used. The default is false.
        """

    def SetArpAlwaysSourceRoute(self, *, ArpAlwaysSourceRoute: bool) -> int:
        """
        The SetArpAlwaysSourceRoute WMI class static method is used
        to set the transmission of ARP queries by TCP/IP.

        Parameters:
        -----------
        ArpAlwaysSourceRoute: bool
            If true, TCP/IP is forced to transmit ARP queries with source routing enabled
            on Token Ring networks. By default, the stack transmits ARP queries
            without source routing first, then retries with source routing enabled
            if no reply is received.
        """

    def SetArpUseEtherSNAP(self, *, ArpUseEtherSNAP: bool) -> int:
        """
        The SetArpUseEtherSNAP WMI class static method is used to enable ethernet packets
        to use 802.3 SNAP encoding.

        Parameters:
        -----------
        ArpUseEtherSNAP: bool
            If true enables TCP/IP to transmit Ethernet packets using 802.3 SNAP encoding.
        """

    def SetDefaultTTL(self, *, DefaultTTL: int) -> int:
        """
        The SetDefaultTTL WMI class static method is used to set the default Time to Live (TTL)
        value in the header of outgoing IP packets.

        Parameters:
        -----------
        DefaultTTL: int
            Time to Live value set in the header of outgoing IP packets.
            The default value is 32; Valid range: 1 - 255
        """

    def SetDeadGWDetect(self, *, DeadGWDetectEnabled: bool) -> int:
        """
        The SetDeadGWDetect WMI class static method is used to enable dead gateway detection.

        Parameters:
        -----------
        DeadGWDetectEnabled: bool
            If true, dead gateway detection should be enabled.
        """

    def SetPMTUBHDetect(self, *, PMTUBHDetectEnabled: bool) -> int:
        """
        The SetPMTUBHDetect WMI class static method is used to enable the detection
        of Black Hole routers while doing Path MTU Discovery.

        Parameters:
        -----------
        PMTUBHDetectEnabled: bool
            If true, TCP attempts to discover Black Hole and route packets
            in different network paths.
        """

    def SetPMTUDiscovery(self, *, PMTUDiscoveryEnabled: bool) -> int:
        """
        The SetPMTUDiscovery WMI class static method is used to enable
        Maximum Transmission Unit (MTU) discovery over the path to a remote host.

        Parameters:
        -----------
        PMTUDiscoveryEnabled: bool
            If true, TCP is enabled to attempt to discover the Maximum Transmission Unit (MTU)
            or largest packet size over the path to a remote host. The default is true.
        """

    def SetForwardBufferMemory(self, *, ForwardBufferMemory: int) -> int:
        """
        The SetForwardBufferMemory WMI class static method is used to specify
        how much memory IP allocates to store packet data in the router packet queue.

        Parameters:
        -----------
        ForwardBufferMemory: int
            Size, in bytes, of the router packet queue used to store packet data.
            The default value is 74240 (fifty 1480-byte packets, rounded to a multiple of 256).
        """

    def SetIGMPLevel(self, *, ForwardBufferMemory: int) -> int:
        """
        The SetIGMPLevel WMI class static method is used to set the extent
        to which the system supports IP multicasting and participates
        in the Internet Group Management Protocol.

        Parameters:
        -----------
        IGMPLevel: int
            Sets the level at which the system supports IP multicast and participates
            in the Internet Group Management Protocol.
            At level 0, the system provides no multicast support.
            At level 1, the system may only send IP multicast packets.
            At level 2, the system may send IP multicast packets
            and fully participate in IGMP to receive multicast packets.

            0: No Multicast
            1: IP Multicast
            2: IP & IGMP multicast
        """

    def SetKeepAliveInterval(self, *, KeepAliveInterval: int) -> int:
        """
        The SetKeepAliveInterval WMI class static method is used to set the interval
        separating Keep Alive Retransmissions until a response is received.

        Parameters:
        -----------
        KeepAliveInterval: int
            Value, in milliseconds, for the interval separating Keep Alive Retransmissions
            until a response is received.
        """

    def SetKeepAliveTime(self, *, KeepAliveTime: int) -> int:
        """
        The SetKeepAliveTime WMI class static method is used to set
        how often TCP attempts to verify that an idle connection is still available
        by sending a Keep Alive packet.

        Parameters:
        -----------
        KeepAliveTime: int
            Interval, in milliseconds, the TCP waits to check that an idle connection
            is still available.
        """

    def SetMTU(self, *, MTU: int) -> int:
        """
        The SetMTU WMI class static method is used to set the default
        Maximum Transmission Unit (MTU) for a network interface.

        Parameters:
        -----------
        MTU: int
            Default Maximum Transmission Unit (MTU) for a network interface.
            The range of this value spans the minimum packet size (68)
            to the MTU supported by the underlying network.
        """

    def SetNumForwardPackets(self, *, NumForwardPackets: int) -> int:
        """
        The SetNumForwardPackets WMI class static method is used to set the number
        of IP packet headers allocated for the router packet queue.
        When all headers are in use, the router will begin to discard packets
        from the queue at random.

        Parameters:
        -----------
        NumForwardPackets: int
            Number of IP packet headers allocated for the router packet queue.
            This should be at least as large as the value of the ForwardBufferMemory property
            divided by the maximum IP data size of the networks connected to the router.
            It should be no larger than the ForwardBufferMemory value divided by 256,
            since at least 256 bytes of forward buffer memory are required by each packet.
            The optimal number of forward packets for a given ForwardBufferMemory size
            depends on the type of traffic carried on the network, and will be somewhere
            between these two values. If the router is disabled, this parameter is ignored
            and no headers are allocated. Valid range: 1 - 0xFFFFFFFE.
        """

    def SetTcpMaxConnectRetransmissions(self, *, TcpMaxConnectRetransmissions: int) -> int:
        """
        The SetTcpMaxConnectRetransmissions WMI class static method is used to set
        the number of attempts TCP will retransmit a connect request before aborting.

        Parameters:
        -----------
        TcpMaxConnectRetransmissions: int
            Number of attempts TCP will retransmit a connect request before aborting.
            The valid range for values is 0 - 0xFFFFFFFF.
        """

    def SetTcpMaxDataRetransmissions(self, *, TcpMaxDataRetransmissions: int) -> int:
        """
        The SetTcpMaxDataRetransmissions WMI class static method is used to set the number
        of times TCP retransmits an individual data segment before aborting the connection.

        Parameters:
        -----------
        TcpMaxDataRetransmissions: int
            Number of times TCP retransmits an individual data segment
            before aborting the connection. Valid range: 0 - 0xFFFFFFFF.
        """

    def SetTcpNumConnections(self, *, TcpNumConnections: int) -> int:
        """
        The SetTcpNumConnections WMI class static method is used to set
        the maximum number of connections that TCP may have open simultaneously.

        Parameters:
        -----------
        TcpNumConnections: int
            Maximum number of connections that TCP may have open simultaneously.
            The valid range of values is 0 - 0xFFFFFE.
        """

    def SetTcpUseRFC1122UrgentPointer(self, *, TcpUseRFC1122UrgentPointer: bool) -> int:
        """
        The SetTcpUseRFC1122UrgentPointer WMI class static method is used to specify
        whether TCP uses the RFC 1122 specification for urgent data,
        or the mode used by Berkeley Software Design (BSD) derived systems.

        Parameters:
        -----------
        TcpUseRFC1122UrgentPointer: bool
            If true, TCP uses the RFC 1122 specification.
            If false, urgent data is sent in the mode used by BSD-derived systems.
        """

    def SetTcpWindowSize(self, *, TcpWindowSize: int) -> int:
        """
        The SetTcpWindowSize WMI class static method is used to set the maximum
        TCP Receive Window size offered by the system.

        Parameters:
        -----------
        TcpWindowSize: int
            Maximum TCP receive window size offered by the system.
            The valid range of values in bytes is 0 - 65535.
        """

    def EnableIPFilterSec(self, IPFilterSecurityEnabled: bool) -> int:
        """
        The EnableIPFilterSec WMI class static method is used to enable
        Internet Protocol security (IPsec) globally across all IP-bound network adapters.

        Parameters:
        -----------
        IPFilterSecurityEnabled: bool
            If true, IPsec is enabled globally across all IP-bound network adapters.
            If false, all port and protocol traffic is allowed to flow unfiltered.
        """

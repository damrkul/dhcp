from enum import Enum


DHCP_DISCOVER   = 1
DHCP_OFFER      = 2
DHCP_REQUEST    = 3
DHCP_DECLINE    = 4
DHCP_ACK        = 5
DHCP_NAK        = 6
DHCP_RELEASE    = 7

op_name = { 
    1: "DHCP_DISCOVER",
    2: "DHCP_OFFER",
    3: "DHCP_REQUEST",
    4: "DHCP_DECLINE",
    5: "DHCP_ACK",
    6: "DHCP_NAK",
    7: "DHCP_RELEASE",
}

def dhcp_method_discover():
    print("This is discover Method")

def dhcp_method_offer():
    print("This is offer Method")

dhcp_methods =  {
    1: dhcp_method_discover,
    2: dhcp_method_offer,
    2: dhcp_method_offer,
    2: dhcp_method_offer,
    2: dhcp_method_offer,
}
dhcp_options =  {
0: {'tag': 0, 'name': 'Pad', 'length': 0, 'meaning': 'None', 'reference': '[RFC2132]'},
1: {'tag': 1, 'name': 'Subnet Mask', 'length': 4, 'meaning': 'Subnet Mask Value', 'reference': '[RFC2132]'},
2: {'tag': 2, 'name': 'Time Offset', 'length': 4, 'meaning': 'Time Offset in Seconds from UTC(note: deprecated by 100 and 101)', 'reference': '[RFC2132]'},
3: {'tag': 3, 'name': 'Router', 'length': 'N', 'meaning': 'N/4 Router addresses', 'reference': '[RFC2132]'},
4: {'tag': 4, 'name': 'Time Server', 'length': 'N', 'meaning': 'N/4 Timeserver addresses', 'reference': '[RFC2132]'},
5: {'tag': 5, 'name': 'Name Server', 'length': 'N', 'meaning': 'N/4 IEN-116 Server addresses', 'reference': '[RFC2132]'},
6: {'tag': 6, 'name': 'Domain Server', 'length': 'N', 'meaning': 'N/4 DNS Server addresses', 'reference': '[RFC2132]'},
7: {'tag': 7, 'name': 'Log Server', 'length': 'N', 'meaning': 'N/4 Logging Server addresses', 'reference': '[RFC2132]'},
8: {'tag': 8, 'name': 'Quotes Server', 'length': 'N', 'meaning': 'N/4 Quotes Server addresses', 'reference': '[RFC2132]'},
9: {'tag': 9, 'name': 'LPR Server', 'length': 'N', 'meaning': 'N/4 Printer Server addresses', 'reference': '[RFC2132]'},
10: {'tag': 10, 'name': 'Impress Server', 'length': 'N', 'meaning': 'N/4 Impress Server addresses', 'reference': '[RFC2132]'},
11: {'tag': 11, 'name': 'RLP Server', 'length': 'N', 'meaning': 'N/4 RLP Server addresses', 'reference': '[RFC2132]'},
12: {'tag': 12, 'name': 'Hostname', 'length': 'N', 'meaning': 'Hostname string', 'reference': '[RFC2132]'},
13: {'tag': 13, 'name': 'Boot File Size', 'length': 2, 'meaning': 'Size of boot file in 512 byte chunks', 'reference': '[RFC2132]'},
14: {'tag': 14, 'name': 'Merit Dump File', 'length': 'N', 'meaning': 'Client to dump and name the file to dump it to', 'reference': '[RFC2132]'},
15: {'tag': 15, 'name': 'Domain Name', 'length': 'N', 'meaning': 'The DNS domain name of the client', 'reference': '[RFC2132]'},
16: {'tag': 16, 'name': 'Swap Server', 'length': 'N', 'meaning': 'Swap Server address', 'reference': '[RFC2132]'},
17: {'tag': 17, 'name': 'Root Path', 'length': 'N', 'meaning': 'Path name for root disk', 'reference': '[RFC2132]'},
18: {'tag': 18, 'name': 'Extension File', 'length': 'N', 'meaning': 'Path name for more BOOTP info', 'reference': '[RFC2132]'},
19: {'tag': 19, 'name': 'Forward On/Off', 'length': 1, 'meaning': 'Enable/Disable IP Forwarding', 'reference': '[RFC2132]'},
20: {'tag': 20, 'name': 'SrcRte On/Off', 'length': 1, 'meaning': 'Enable/Disable Source Routing', 'reference': '[RFC2132]'},
21: {'tag': 21, 'name': 'Policy Filter', 'length': 'N', 'meaning': 'Routing Policy Filters', 'reference': '[RFC2132]'},
22: {'tag': 22, 'name': 'Max DG Assembly', 'length': 2, 'meaning': 'Max Datagram Reassembly Size', 'reference': '[RFC2132]'},
23: {'tag': 23, 'name': 'Default IP TTL', 'length': 1, 'meaning': 'Default IP Time to Live', 'reference': '[RFC2132]'},
24: {'tag': 24, 'name': 'MTU Timeout', 'length': 4, 'meaning': 'Path MTU Aging Timeout', 'reference': '[RFC2132]'},
25: {'tag': 25, 'name': 'MTU Plateau', 'length': 'N', 'meaning': 'Path MTU  Plateau Table', 'reference': '[RFC2132]'},
26: {'tag': 26, 'name': 'MTU Interface', 'length': 2, 'meaning': 'Interface MTU Size', 'reference': '[RFC2132]'},
27: {'tag': 27, 'name': 'MTU Subnet', 'length': 1, 'meaning': 'All Subnets are Local', 'reference': '[RFC2132]'},
28: {'tag': 28, 'name': 'Broadcast Address', 'length': 4, 'meaning': 'Broadcast Address', 'reference': '[RFC2132]'},
29: {'tag': 29, 'name': 'Mask Discovery', 'length': 1, 'meaning': 'Perform Mask Discovery', 'reference': '[RFC2132]'},
30: {'tag': 30, 'name': 'Mask Supplier', 'length': 1, 'meaning': 'Provide Mask to Others', 'reference': '[RFC2132]'},
31: {'tag': 31, 'name': 'Router Discovery', 'length': 1, 'meaning': 'Perform Router Discovery', 'reference': '[RFC2132]'},
32: {'tag': 32, 'name': 'Router Request', 'length': 4, 'meaning': 'Router Solicitation Address', 'reference': '[RFC2132]'},
33: {'tag': 33, 'name': 'Static Route', 'length': 'N', 'meaning': 'Static Routing Table', 'reference': '[RFC2132]'},
34: {'tag': 34, 'name': 'Trailers', 'length': 1, 'meaning': 'Trailer Encapsulation', 'reference': '[RFC2132]'},
35: {'tag': 35, 'name': 'ARP Timeout', 'length': 4, 'meaning': 'ARP Cache Timeout', 'reference': '[RFC2132]'},
36: {'tag': 36, 'name': 'Ethernet', 'length': 1, 'meaning': 'Ethernet Encapsulation', 'reference': '[RFC2132]'},
37: {'tag': 37, 'name': 'Default TCP TTL', 'length': 1, 'meaning': 'Default TCP Time to Live', 'reference': '[RFC2132]'},
38: {'tag': 38, 'name': 'Keepalive Time', 'length': 4, 'meaning': 'TCP Keepalive Interval', 'reference': '[RFC2132]'},
39: {'tag': 39, 'name': 'Keepalive Data', 'length': 1, 'meaning': 'TCP Keepalive Garbage', 'reference': '[RFC2132]'},
40: {'tag': 40, 'name': 'NIS Domain', 'length': 'N', 'meaning': 'NIS Domain Name', 'reference': '[RFC2132]'},
41: {'tag': 41, 'name': 'NIS Servers', 'length': 'N', 'meaning': 'NIS Server Addresses', 'reference': '[RFC2132]'},
42: {'tag': 42, 'name': 'NTP Servers', 'length': 'N', 'meaning': 'NTP Server Addresses', 'reference': '[RFC2132]'},
43: {'tag': 43, 'name': 'Vendor Specific', 'length': 'N', 'meaning': 'Vendor Specific Information', 'reference': '[RFC2132]'},
44: {'tag': 44, 'name': 'NETBIOS Name Srv', 'length': 'N', 'meaning': 'NETBIOS Name Servers', 'reference': '[RFC2132]'},
45: {'tag': 45, 'name': 'NETBIOS Dist Srv', 'length': 'N', 'meaning': 'NETBIOS Datagram Distribution', 'reference': '[RFC2132]'},
46: {'tag': 46, 'name': 'NETBIOS Node Type', 'length': 1, 'meaning': 'NETBIOS Node Type', 'reference': '[RFC2132]'},
47: {'tag': 47, 'name': 'NETBIOS Scope', 'length': 'N', 'meaning': 'NETBIOS Scope', 'reference': '[RFC2132]'},
48: {'tag': 48, 'name': 'X Window Font', 'length': 'N', 'meaning': 'X Window Font Server', 'reference': '[RFC2132]'},
49: {'tag': 49, 'name': 'X Window Manager', 'length': 'N', 'meaning': 'X Window Display Manager', 'reference': '[RFC2132]'},
50: {'tag': 50, 'name': 'Address Request', 'length': 4, 'meaning': 'Requested IP Address', 'reference': '[RFC2132]'},
51: {'tag': 51, 'name': 'Address Time', 'length': 4, 'meaning': 'IP Address Lease Time', 'reference': '[RFC2132]'},
52: {'tag': 52, 'name': 'Overload', 'length': 1, 'meaning': 'Overload "sname" or "file', 'reference': '[RFC2132]'},
53: {'tag': 53, 'name': 'DHCP Msg Type', 'length': 1, 'meaning': 'DHCP Message Type', 'reference': '[RFC2132]'},
54: {'tag': 54, 'name': 'DHCP Server Id', 'length': 4, 'meaning': 'DHCP Server Identification', 'reference': '[RFC2132]'},
55: {'tag': 55, 'name': 'Parameter List', 'length': 'N', 'meaning': 'Parameter Request List', 'reference': '[RFC2132]'},
56: {'tag': 56, 'name': 'DHCP Message', 'length': 'N', 'meaning': 'DHCP Error Message', 'reference': '[RFC2132]'},
57: {'tag': 57, 'name': 'DHCP Max Msg Size', 'length': 2, 'meaning': 'DHCP Maximum Message Size', 'reference': '[RFC2132]'},
58: {'tag': 58, 'name': 'Renewal Time', 'length': 4, 'meaning': 'DHCP Renewal (T1) Time', 'reference': '[RFC2132]'},
59: {'tag': 59, 'name': 'Rebinding Time', 'length': 4, 'meaning': 'DHCP Rebinding (T2) Time', 'reference': '[RFC2132]'},
60: {'tag': 60, 'name': 'Class Id', 'length': 'N', 'meaning': 'Class Identifier', 'reference': '[RFC2132]'},
61: {'tag': 61, 'name': 'Client Id', 'length': 'N', 'meaning': 'Client Identifier', 'reference': '[RFC2132]'},
62: {'tag': 62, 'name': 'NetWare/IP Domain', 'length': 'N', 'meaning': 'NetWare/IP Domain Name', 'reference': '[RFC2242]'},
63: {'tag': 63, 'name': 'NetWare/IP Option', 'length': 'N', 'meaning': 'NetWare/IP sub Options', 'reference': '[RFC2242]'},
64: {'tag': 64, 'name': 'NIS-Domain-Name', 'length': 'N', 'meaning': 'NIS+ v3 Client Domain Name', 'reference': '[RFC2132]'},
65: {'tag': 65, 'name': 'NIS-Server-Addr', 'length': 'N', 'meaning': 'NIS+ v3 Server Addresses', 'reference': '[RFC2132]'},
66: {'tag': 66, 'name': 'Server-Name', 'length': 'N', 'meaning': 'TFTP Server Name', 'reference': '[RFC2132]'},
67: {'tag': 67, 'name': 'Bootfile-Name', 'length': 'N', 'meaning': 'Boot File Name', 'reference': '[RFC2132]'},
68: {'tag': 68, 'name': 'Home-Agent-Addrs', 'length': 'N', 'meaning': 'Home Agent Addresses', 'reference': '[RFC2132]'},
69: {'tag': 69, 'name': 'SMTP-Server', 'length': 'N', 'meaning': 'Simple Mail Server Addresses', 'reference': '[RFC2132]'},
70: {'tag': 70, 'name': 'POP3-Server', 'length': 'N', 'meaning': 'Post Office Server Addresses', 'reference': '[RFC2132]'},
71: {'tag': 71, 'name': 'NNTP-Server', 'length': 'N', 'meaning': 'Network News Server Addresses', 'reference': '[RFC2132]'},
72: {'tag': 72, 'name': 'WWW-Server', 'length': 'N', 'meaning': 'WWW Server Addresses', 'reference': '[RFC2132]'},
73: {'tag': 73, 'name': 'Finger-Server', 'length': 'N', 'meaning': 'Finger Server Addresses', 'reference': '[RFC2132]'},
74: {'tag': 74, 'name': 'IRC-Server', 'length': 'N', 'meaning': 'Chat Server Addresses', 'reference': '[RFC2132]'},
75: {'tag': 75, 'name': 'StreetTalk-Server', 'length': 'N', 'meaning': 'StreetTalk Server Addresses', 'reference': '[RFC2132]'},
76: {'tag': 76, 'name': 'STDA-Server', 'length': 'N', 'meaning': 'ST Directory Assist. Addresses', 'reference': '[RFC2132]'},
77: {'tag': 77, 'name': 'User-Class', 'length': 'N', 'meaning': 'User Class Information', 'reference': '[RFC3004]'},
78: {'tag': 78, 'name': 'Directory Agent', 'length': 'N', 'meaning': 'directory agent information', 'reference': '[RFC2610]'},
79: {'tag': 79, 'name': 'Service Scope', 'length': 'N', 'meaning': 'service location agent scope', 'reference': '[RFC2610]'},
80: {'tag': 80, 'name': 'Rapid Commit', 'length': 0, 'meaning': 'Rapid Commit', 'reference': '[RFC4039]'},
81: {'tag': 81, 'name': 'Client FQDN', 'length': 'N', 'meaning': 'Fully Qualified Domain Name', 'reference': '[RFC4702]'},
82: {'tag': 82, 'name': 'Relay Agent Information', 'length': 'N', 'meaning': 'Relay Agent Information', 'reference': '[RFC3046]'},
83: {'tag': 83, 'name': 'iSNS', 'length': 'N', 'meaning': 'Internet Storage Name Service', 'reference': '[RFC4174]'},
84: {'tag': 84, 'name': 'REMOVED/Unassigned', 'length': '', 'meaning': '', 'reference': '[RFC3679]'},
85: {'tag': 85, 'name': 'NDS Servers', 'length': 'N', 'meaning': 'Novell Directory Services', 'reference': '[RFC2241]'},
86: {'tag': 86, 'name': 'NDS Tree Name', 'length': 'N', 'meaning': 'Novell Directory Services', 'reference': '[RFC2241]'},
87: {'tag': 87, 'name': 'NDS Context', 'length': 'N', 'meaning': 'Novell Directory Services', 'reference': '[RFC2241]'},
88: {'tag': 88, 'name': 'BCMCS Controller Domain Name list', 'length': '', 'meaning': '', 'reference': '[RFC4280]'},
89: {'tag': 89, 'name': 'BCMCS Controller IPv4 address option', 'length': '', 'meaning': '', 'reference': '[RFC4280]'},
90: {'tag': 90, 'name': 'Authentication', 'length': 'N', 'meaning': 'Authentication', 'reference': '[RFC3118]'},
91: {'tag': 91, 'name': 'client-last-transaction-time option', 'length': '', 'meaning': '', 'reference': '[RFC4388]'},
92: {'tag': 92, 'name': 'associated-ip option', 'length': '', 'meaning': '', 'reference': '[RFC4388]'},
93: {'tag': 93, 'name': 'Client System', 'length': 'N', 'meaning': 'Client System Architecture', 'reference': '[RFC4578]'},
94: {'tag': 94, 'name': 'Client NDI', 'length': 'N', 'meaning': 'Client Network Device Interface', 'reference': '[RFC4578]'},
95: {'tag': 95, 'name': 'LDAP', 'length': 'N', 'meaning': 'Lightweight Directory Access Protocol', 'reference': '[RFC3679]'},
96: {'tag': 96, 'name': 'REMOVED/Unassigned', 'length': '', 'meaning': '', 'reference': '[RFC3679]'},
97: {'tag': 97, 'name': 'UUID/GUID', 'length': 'N', 'meaning': 'UUID/GUID-based Client Identifier', 'reference': '[RFC4578]'},
98: {'tag': 98, 'name': 'User-Auth', 'length': 'N', 'meaning': "Open Group's User Authentication", 'reference': '[RFC2485]'},
99: {'tag': 99, 'name': 'GEOCONF_CIVIC', 'length': '', 'meaning': '', 'reference': '[RFC4776]'},
100: {'tag': 100, 'name': 'PCode', 'length': 'N', 'meaning': 'IEEE 1003.1 TZ String', 'reference': '[RFC4833]'},
101: {'tag': 101, 'name': 'TCode', 'length': 'N', 'meaning': 'Reference to the TZ Database', 'reference': '[RFC4833]'},
108: {'tag': 108, 'name': 'IPv6-Only Preferred (TEMPORARY - registered 2020-06-24, expires 2021-06-24)', 'length': 4, 'meaning': 'Number of seconds before retrying DHCPv4', 'reference': '[draft-ietf-dhc-v6only-03]'},
109: {'tag': 109, 'name': 'OPTION_DHCP4O6_S46_SADDR', 'length': 16, 'meaning': 'DHCPv4 over DHCPv6 Softwire Source Address Option', 'reference': '[RFC8539]'},
110: {'tag': 110, 'name': 'REMOVED/Unassigned', 'length': '', 'meaning': '', 'reference': '[RFC3679]'},
111: {'tag': 111, 'name': 'Unassigned', 'length': '', 'meaning': '', 'reference': '[RFC3679]'},
112: {'tag': 112, 'name': 'Netinfo Address', 'length': 'N', 'meaning': 'NetInfo Parent Server Address', 'reference': '[RFC3679]'},
113: {'tag': 113, 'name': 'Netinfo Tag', 'length': 'N', 'meaning': 'NetInfo Parent Server Tag', 'reference': '[RFC3679]'},
114: {'tag': 114, 'name': 'DHCP Captive-Portal', 'length': 'N', 'meaning': 'DHCP Captive-Portal', 'reference': '[RFC-ietf-capport-rfc7710bis-10]'},
115: {'tag': 115, 'name': 'REMOVED/Unassigned', 'length': '', 'meaning': '', 'reference': '[RFC3679]'},
116: {'tag': 116, 'name': 'Auto-Config', 'length': 'N', 'meaning': 'DHCP Auto-Configuration', 'reference': '[RFC2563]'},
117: {'tag': 117, 'name': 'Name Service Search', 'length': 'N', 'meaning': 'Name Service Search', 'reference': '[RFC2937]'},
118: {'tag': 118, 'name': 'Subnet Selection Option', 'length': 4, 'meaning': 'Subnet Selection Option', 'reference': '[RFC3011]'},
119: {'tag': 119, 'name': 'Domain Search', 'length': 'N', 'meaning': 'DNS domain search list', 'reference': '[RFC3397]'},
120: {'tag': 120, 'name': 'SIP Servers DHCP Option', 'length': 'N', 'meaning': 'SIP Servers DHCP Option', 'reference': '[RFC3361]'},
121: {'tag': 121, 'name': 'Classless Static Route Option', 'length': 'N', 'meaning': 'Classless Static Route Option', 'reference': '[RFC3442]'},
122: {'tag': 122, 'name': 'CCC', 'length': 'N', 'meaning': 'CableLabs Client Configuration', 'reference': '[RFC3495]'},
123: {'tag': 123, 'name': 'GeoConf Option', 'length': 16, 'meaning': 'GeoConf Option', 'reference': '[RFC6225]'},
124: {'tag': 124, 'name': 'V-I Vendor Class', 'length': '', 'meaning': 'Vendor-Identifying Vendor Class', 'reference': '[RFC3925]'},
125: {'tag': 125, 'name': 'V-I Vendor-Specific Information', 'length': '', 'meaning': 'Vendor-Identifying Vendor-Specific Information', 'reference': '[RFC3925]'},
128: {'tag': 128, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
128: {'tag': 128, 'name': 'Etherboot signature. 6 bytes: E4:45:74:68:00:00', 'length': '', 'meaning': '', 'reference': ''},
128: {'tag': 128, 'name': 'DOCSIS "full security" server IP address', 'length': '', 'meaning': '', 'reference': ''},
128: {'tag': 128, 'name': 'TFTP Server IP address (for IP Phone software load)', 'length': '', 'meaning': '', 'reference': ''},
129: {'tag': 129, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
129: {'tag': 129, 'name': 'Kernel options. Variable length string', 'length': '', 'meaning': '', 'reference': ''},
129: {'tag': 129, 'name': 'Call Server IP address', 'length': '', 'meaning': '', 'reference': ''},
130: {'tag': 130, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
130: {'tag': 130, 'name': 'Ethernet interface. Variable length string.', 'length': '', 'meaning': '', 'reference': ''},
130: {'tag': 130, 'name': 'Discrimination string (to identify vendor)', 'length': '', 'meaning': '', 'reference': ''},
131: {'tag': 131, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
131: {'tag': 131, 'name': 'Remote statistics server IP address', 'length': '', 'meaning': '', 'reference': ''},
132: {'tag': 132, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
132: {'tag': 132, 'name': 'IEEE 802.1Q VLAN ID', 'length': '', 'meaning': '', 'reference': ''},
133: {'tag': 133, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
133: {'tag': 133, 'name': 'IEEE 802.1D/p Layer 2 Priority', 'length': '', 'meaning': '', 'reference': ''},
134: {'tag': 134, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
134: {'tag': 134, 'name': 'Diffserv Code Point (DSCP) for VoIP signalling and media streams', 'length': '', 'meaning': '', 'reference': ''},
135: {'tag': 135, 'name': 'PXE - undefined (vendor specific)', 'length': '', 'meaning': '', 'reference': '[RFC4578]'},
135: {'tag': 135, 'name': 'HTTP Proxy for phone-specific applications', 'length': '', 'meaning': '', 'reference': ''},
136: {'tag': 136, 'name': 'OPTION_PANA_AGENT', 'length': '', 'meaning': '', 'reference': '[RFC5192]'},
137: {'tag': 137, 'name': 'OPTION_V4_LOST', 'length': '', 'meaning': '', 'reference': '[RFC5223]'},
138: {'tag': 138, 'name': 'OPTION_CAPWAP_AC_V4', 'length': 'N', 'meaning': 'CAPWAP Access Controller addresses', 'reference': '[RFC5417]'},
139: {'tag': 139, 'name': 'OPTION-IPv4_Address-MoS', 'length': 'N', 'meaning': 'a series of suboptions', 'reference': '[RFC5678]'},
140: {'tag': 140, 'name': 'OPTION-IPv4_FQDN-MoS', 'length': 'N', 'meaning': 'a series of suboptions', 'reference': '[RFC5678]'},
141: {'tag': 141, 'name': 'SIP UA Configuration Service Domains', 'length': 'N', 'meaning': 'List of domain names to search for SIP User Agent Configuration', 'reference': '[RFC6011]'},
142: {'tag': 142, 'name': 'OPTION-IPv4_Address-ANDSF', 'length': 'N', 'meaning': 'ANDSF IPv4 Address Option for DHCPv4', 'reference': '[RFC6153]'},
143: {'tag': 143, 'name': 'OPTION_V4_SZTP_REDIRECT', 'length': 'N', 'meaning': 'This option provides a list of URIs for SZTP bootstrap servers', 'reference': '[RFC8572]'},
144: {'tag': 144, 'name': 'GeoLoc', 'length': 16, 'meaning': 'Geospatial Location with Uncertainty', 'reference': '[RFC6225]'},
145: {'tag': 145, 'name': 'FORCERENEW_NONCE_CAPABLE', 'length': 1, 'meaning': 'Forcerenew Nonce Capable', 'reference': '[RFC6704]'},
146: {'tag': 146, 'name': 'RDNSS Selection', 'length': 'N', 'meaning': 'Information for selecting RDNSS', 'reference': '[RFC6731]'},
150: {'tag': 150, 'name': 'TFTP server address | Etherboot | GRUB configuration path name', 'length': '', 'meaning': '', 'reference': '[RFC5859]'},
151: {'tag': 151, 'name': 'status-code', 'length': 'N+1', 'meaning': 'Status code and optional N byte text message describing status.', 'reference': '[RFC6926]'},
152: {'tag': 152, 'name': 'base-time', 'length': 4, 'meaning': 'Absolute time (seconds since Jan 1, 1970) message was sent.', 'reference': '[RFC6926]'},
153: {'tag': 153, 'name': 'start-time-of-state', 'length': 4, 'meaning': 'Number of seconds in the past when client entered current state.', 'reference': '[RFC6926]'},
154: {'tag': 154, 'name': 'query-start-time', 'length': 4, 'meaning': 'Absolute time (seconds since Jan 1, 1970) for beginning of query.', 'reference': '[RFC6926]'},
155: {'tag': 155, 'name': 'query-end-time', 'length': 4, 'meaning': 'Absolute time (seconds since Jan 1, 1970) for end of query.', 'reference': '[RFC6926]'},
156: {'tag': 156, 'name': 'dhcp-state', 'length': 1, 'meaning': 'State of IP address.', 'reference': '[RFC6926]'},
157: {'tag': 157, 'name': 'data-source', 'length': 1, 'meaning': 'Indicates information came from local or remote server.', 'reference': '[RFC6926]'},
158: {'tag': 158, 'name': 'OPTION_V4_PCP_SERVER', 'length': 'Variable; the minimum length is 5.', 'meaning': 'Includes one or multiple lists of PCP server IP addresses;  each list is treated as a separate PCP server.', 'reference': '[RFC7291]'},
159: {'tag': 159, 'name': 'OPTION_V4_PORTPARAMS', 'length': 4, 'meaning': 'This option is used to configure a set of ports bound to a shared IPv4 address.', 'reference': '[RFC7618]'},
161: {'tag': 161, 'name': 'OPTION_MUD_URL_V4', 'length': 'N (variable)', 'meaning': 'Manufacturer Usage Descriptions', 'reference': '[RFC8520]'},
175: {'tag': 175, 'name': 'Etherboot (Tentatively Assigned -2005-06-23)', 'length': '', 'meaning': '', 'reference': ''},
176: {'tag': 176, 'name': 'IP Telephone (Tentatively Assigned -2005-06-23)', 'length': '', 'meaning': '', 'reference': ''},
177: {'tag': 177, 'name': 'Etherboot (Tentatively Assigned -2005-06-23)', 'length': '', 'meaning': '', 'reference': ''},
177: {'tag': 177, 'name': 'PacketCable and CableHome (replaced by 122)', 'length': '', 'meaning': '', 'reference': ''},
208: {'tag': 208, 'name': 'PXELINUX Magic', 'length': 4, 'meaning': 'magic string = F1:00:74:7E', 'reference': '[RFC5071][Deprecated]'},
209: {'tag': 209, 'name': 'Configuration File', 'length': 'N', 'meaning': 'Configuration file', 'reference': '[RFC5071]'},
210: {'tag': 210, 'name': 'Path Prefix', 'length': 'N', 'meaning': 'Path Prefix Option', 'reference': '[RFC5071]'},
211: {'tag': 211, 'name': 'Reboot Time', 'length': 4, 'meaning': 'Reboot Time', 'reference': '[RFC5071]'},
212: {'tag': 212, 'name': 'OPTION_6RD', 'length': '18 + N', 'meaning': 'OPTION_6RD with N/4 6rd BR addresses', 'reference': '[RFC5969]'},
213: {'tag': 213, 'name': 'OPTION_V4_ACCESS_DOMAIN', 'length': 'N', 'meaning': 'Access Network Domain Name', 'reference': '[RFC5986]'},
220: {'tag': 220, 'name': 'Subnet Allocation Option', 'length': 'N', 'meaning': 'Subnet Allocation Option', 'reference': '[RFC6656]'},
221: {'tag': 221, 'name': 'Virtual Subnet Selection (VSS) Option', 'length': '', 'meaning': '', 'reference': '[RFC6607]'},
249: {'tag': 249, 'name': 'Private/Classless Static Route', 'length': 4, 'meaning': 'None', 'reference': '[RFC2132]'},
252: {'tag': 252, 'name': 'Proxy Autodiscovery', 'length': 4, 'meaning': 'None', 'reference': '[RFC2132]'},
255: {'tag': 255, 'name': 'End', 'length': 0, 'meaning': 'None', 'reference': '[RFC2132]'},
}

# CyberSentinel

CyberSentinel is a web-based network reconnaissance and analysis platform built using Python, Flask, Socket Programming, HTML, CSS, and JavaScript. It provides cybersecurity-focused tools through a unified dashboard, allowing users to perform network discovery, port scanning, service enumeration, HTTP header analysis, reverse DNS lookup, and TCP-based reachability testing.

The project was created to strengthen practical knowledge of networking, cybersecurity fundamentals, backend development, and deployment of Python applications.

---

# Overview

CyberSentinel combines multiple reconnaissance techniques into a single web application.

The platform currently includes:

* Port Scanner
* TCP Ping Tool
* Reverse DNS Resolution
* Service Detection
* HTTP Header Analysis
* Technology Fingerprinting
* JSON Report Export

The application is deployed using Railway and designed with a cybersecurity-themed user interface.

---

# Features

## Port Scanner

The Port Scanner performs TCP-based scanning against a target host.

Capabilities include:

* Hostname resolution
* IP address identification
* Open port discovery
* Service identification
* HTTP and HTTPS detection
* Reverse DNS lookup
* Response header collection
* Technology fingerprinting
* Content-Type analysis
* Content-Length extraction

### Information Collected

* Hostname
* IP Address
* Host Status
* Reverse DNS Record
* Open Ports
* Service Type
* Server Banner
* HTTP Headers
* Technology Information

---

## TCP Ping Tool

The Ping Tool performs TCP-based reachability testing and latency measurement.

Unlike traditional ICMP ping, this implementation uses TCP socket connections to ensure compatibility with cloud hosting environments such as Railway.

Capabilities include:

* Host reachability testing
* DNS resolution
* RTT measurement
* Average latency calculation
* Minimum latency calculation
* Maximum latency calculation
* Jitter calculation
* Packet loss estimation
* JSON report export

### Information Collected

* Hostname
* IP Address
* Connection Status
* Protocol Used
* Port Used
* Packets Sent
* Packets Received
* Packet Loss
* RTT Minimum
* RTT Average
* RTT Maximum
* Jitter
* Total Test Time

---

# Technologies Used

## Programming Language

Python

---

## Backend Technologies

* Flask
* Socket Programming
* HTTP Requests
* JSON Processing
* DNS Resolution

---

## Frontend Technologies

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

---

## Networking Concepts

* TCP Connections
* Port Scanning
* DNS Resolution
* Reverse DNS Lookup
* Banner Grabbing
* HTTP Header Parsing
* Service Enumeration
* Network Reconnaissance

---
## IP Geolocation Tool

The IP Geolocation Tool allows users to gather geographical and network-related information about any public IP address directly from the CyberSentinel dashboard.

### Features

* Public IP address lookup
* Country detection
* Region and city identification
* ZIP / Postal code information
* Latitude and longitude coordinates
* Timezone detection
* ISP / Organization identification
* ASN (Autonomous System Number) information
* Interactive and clean web interface
* Error handling for invalid IP addresses

### How It Works

1. The user enters an IP address.
2. The application sends a request to an IP geolocation API.
3. The API returns location and network metadata.
4. Flask processes the response.
5. Results are displayed in a structured dashboard.

### Information Retrieved

| Field        | Description                        |
| ------------ | ---------------------------------- |
| IP Address   | Target IP address                  |
| Country      | Country where the IP is registered |
| Region       | State / Province / Region          |
| City         | City associated with the IP        |
| Postal Code  | ZIP or Postal Code                 |
| Latitude     | Geographic latitude                |
| Longitude    | Geographic longitude               |
| Timezone     | Local timezone of the IP           |
| ISP          | Internet Service Provider          |
| Organization | Owning organization                |
| ASN          | Autonomous System Number           |

### Technologies Used

* Python
* Flask
* Requests
* JSON
* HTML
* CSS
* Jinja2 Templates


### Example Use Cases

* Network reconnaissance
* Security investigations
* Threat intelligence research
* Infrastructure mapping
* Educational purposes
* IP ownership verification

### Limitations

* Works only with public IP addresses.
* Private IP addresses (192.168.x.x, 10.x.x.x, 172.16.x.x) cannot be geolocated.
* Location data may not always represent the exact physical location of the user.
* Accuracy depends on the geolocation provider database.

### Educational Purpose

This tool is designed for learning networking, web development, and cybersecurity concepts. It helps users understand how IP addresses are mapped to geographical regions and how network ownership information is publicly available.

## Subdomain Finder

### Overview

The Subdomain Finder module helps identify subdomains associated with a target domain. It combines Certificate Transparency logs from crt.sh with DNS validation to discover live and accessible subdomains.

This tool is useful for reconnaissance, attack surface mapping, asset discovery, and understanding an organization's publicly exposed infrastructure.

### Features

* Certificate Transparency log enumeration using crt.sh
* Extraction and cleanup of discovered subdomains
* Removal of duplicate entries
* DNS validation of discovered subdomains
* Live subdomain detection
* Multi-threaded validation for improved performance
* Clean web-based results dashboard

### Technologies Used

* Python
* Flask
* Requests
* Socket Programming
* ThreadPoolExecutor
* HTML
* CSS

### Workflow

1. User enters a target domain.
2. CyberSentinel queries crt.sh Certificate Transparency logs.
3. Extracted subdomains are cleaned and normalized.
4. Each subdomain is validated through DNS resolution.
5. Live subdomains are displayed in the results dashboard.

### Example Output

Target Domain:
microsoft.com

Results:

* login.microsoft.com
* portal.microsoft.com
* support.microsoft.com
* teams.microsoft.com
* outlook.microsoft.com

### Educational Concepts

* Certificate Transparency Logs
* DNS Resolution
* Asset Discovery
* Multi-threading
* Web Reconnaissance
* Network Enumeration

## DNS Enumeration

### Overview

The DNS Enumeration module retrieves publicly available DNS records associated with a domain. These records provide valuable information about hosting infrastructure, mail services, name servers, and domain configuration.

This information is commonly used during reconnaissance and network investigations.

### Features

* A Record Lookup
* AAAA Record Lookup
* MX Record Lookup
* NS Record Lookup
* TXT Record Lookup
* Clean tabular presentation
* Web-based interface

### Technologies Used

* Python
* Flask
* dnspython
* HTML
* CSS

### Workflow

1. User enters a target domain.
2. CyberSentinel queries DNS servers.
3. Multiple record types are collected.
4. Results are displayed in an organized format.

### Supported DNS Records

#### A Records

Maps a domain name to an IPv4 address.

Example:

google.com → 142.250.183.238

#### AAAA Records

Maps a domain name to an IPv6 address.

#### MX Records

Identifies mail servers responsible for handling email.

#### NS Records

Shows authoritative name servers for the domain.

#### TXT Records

Contains metadata such as SPF, DKIM, and verification records.

### Example Output

Domain:
google.com

A Records:
142.250.183.238

MX Records:
smtp.google.com

NS Records:
ns1.google.com
ns2.google.com
ns3.google.com
ns4.google.com

TXT Records:
v=spf1 include:_spf.google.com ~all

### Educational Concepts

* DNS Architecture
* Resource Records
* Email Infrastructure
* SPF Records
* Domain Resolution Process
* Network Enumeration

## WHOIS Lookup

### Overview

The WHOIS Lookup module retrieves publicly available registration information about a domain. It provides ownership, registrar, registration dates, expiration details, and domain infrastructure information.

WHOIS data is widely used for domain investigations, asset attribution, threat intelligence, and cybersecurity reconnaissance.

### Features

* Domain Registration Information
* Registrar Details
* Creation Date
* Expiration Date
* Last Updated Date
* Name Server Enumeration
* Structured Results Dashboard

### Technologies Used

* Python
* Flask
* python-whois
* HTML
* CSS

### Workflow

1. User enters a target domain.
2. CyberSentinel queries WHOIS databases.
3. Registration details are collected.
4. Results are formatted and displayed.

### Information Retrieved

#### Domain Name

Registered domain identifier.

#### Registrar

Organization responsible for domain registration.

#### Creation Date

Date when the domain was first registered.

#### Expiration Date

Date when the domain registration expires.

#### Updated Date

Last modification date of the domain registration.

#### Name Servers

Authoritative DNS servers associated with the domain.

### Example Output

Domain:
google.com

Registrar:
MarkMonitor, Inc.

Created:
15-09-1997

Expires:
14-09-2028

Updated:
09-09-2019

Name Servers:
ns1.google.com
ns2.google.com
ns3.google.com
ns4.google.com

### Educational Concepts

* Domain Registration Process
* Internet Governance
* Domain Ownership
* Registrar Infrastructure
* Name Server Architecture
* Cyber Threat Intelligence

### Use Cases

* Asset Investigation
* Threat Intelligence
* Security Research
* Domain Verification
* Infrastructure Analysis
* Reconnaissance Operations



# Project Structure

```text
CyberSentinel/
│
├── main.py
│
├── scanner/
│   └── scanner.py
│
├── ping_tool/
│   └── ping.py
│
├── ip_geolocation/
│   └── geo.py
│
├── subdomain_finder/
│   └── subfinder.py
│
├── whois_lookup/
│   └── whois_lookup.py
│
├── dns_tool/
│   └── dns_lookup.py
│
├── templates/
│   ├── dashboard.html
│   │
│   ├── portscan.html
│   ├── result.html
│   │
│   ├── ping.html
│   ├── ping_result.html
│   │
│   ├── geo_index.html
│   ├── geo_result.html
│   │
│   ├── subdomain_index.html
│   ├── subdomain_result.html
│   │
│   ├── whois_index.html
│   ├── whois_result.html
│   │
│   ├── dns_index.html
│   └── dns_result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

```

# Installation

Clone the repository:

```bash
git clone https://github.com/MAYANK2454-19/Cybersentinel.git
```

Move into the project directory:

```bash
cd CyberSentinel
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

# Deployment

CyberSentinel is designed to run both locally and on Railway.

For Railway deployment:

1. Push the project to GitHub.
2. Create a Railway project.
3. Connect the GitHub repository.
4. Deploy automatically.

Production startup command:

```bash
gunicorn main:app
```

---

# Why TCP Ping Instead of ICMP Ping?

Most cloud hosting providers do not provide access to the operating system's ICMP ping utility.

To ensure compatibility across deployment environments, CyberSentinel implements a TCP-based reachability test using Python sockets.

Benefits include:

* Works on Railway
* Works without system ping utilities
* Provides latency measurements
* Allows packet loss estimation
* Requires no special permissions

---

# Learning Outcomes

This project provided practical experience with:

* Python Programming
* Flask Development
* Socket Programming
* Network Reconnaissance
* DNS Resolution
* Reverse DNS Lookup
* Port Scanning
* Banner Grabbing
* HTTP Requests
* HTTPS Requests
* Header Parsing
* JSON Processing
* Web Development
* Application Deployment
* Cybersecurity Fundamentals

---

# Future Improvements

Planned enhancements include:

* WHOIS Lookup Tool
* IP Geolocation Tool
* Advanced Banner Grabbing
* Multi-threaded Scanning
* Service Version Detection
* PDF Report Generation
* Vulnerability Checks
* Dark/Light Theme Support
* Scan History Storage

---

# Disclaimer

CyberSentinel is intended for educational purposes, cybersecurity learning, and authorized network testing only.

Users are responsible for ensuring they have permission before scanning or testing any network, system, or host.

Unauthorized scanning of third-party systems may violate laws, regulations, or organizational policies.

Designed for educational and reconnaissance purposes.

Some features such as port scanning and network reachability

may be affected by restrictions imposed by the hosting provider.

---

# Author

Mayank

Cybersecurity Student and Developer

CyberSentinel v1.0

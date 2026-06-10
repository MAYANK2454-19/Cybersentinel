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
├──ip_geolocation/
│      └── geo.py
├── templates/
│   ├── dashboard.html
│   ├── portscan.html
│   ├── result.html
│   ├── ping.html
│   └── ping_result.html
|   ├── geo_index.html
│   └── geo_result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
│
└── README.md
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

---

# Author

Mayank

Cybersecurity Student and Developer

CyberSentinel v1.0

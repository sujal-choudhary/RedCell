import socket
import requests
import ssl
from urllib.parse import urlparse


def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return None


def get_http_headers(domain):
    try:
        url = domain if domain.startswith("http") else f"http://{domain}"
        response = requests.get(url, timeout=10)
        return dict(response.headers)
    except Exception:
        return {}


def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return {
                    "issuer": cert.get("issuer"),
                    "subject": cert.get("subject"),
                    "version": cert.get("version")
                }
    except Exception:
        return {}


def fingerprint_technology(headers):
    tech = []

    server = headers.get("Server")
    powered_by = headers.get("X-Powered-By")

    if server:
        tech.append(f"Server: {server}")
    if powered_by:
        tech.append(f"X-Powered-By: {powered_by}")

    return tech


def gather_information(domain):
    result = {}

    result["domain"] = domain
    result["ip_address"] = resolve_ip(domain)

    headers = get_http_headers(domain)
    result["http_headers"] = headers

    result["ssl_info"] = get_ssl_info(domain)
    result["technologies"] = fingerprint_technology(headers)

    return result

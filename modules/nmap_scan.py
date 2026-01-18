import subprocess
import xml.etree.ElementTree as ET
import tempfile
import os


SAFE_NSE = (
    "vuln,"
    "http-headers,"
    "http-security-headers,"
    "http-methods,"
    "ssl-enum-ciphers"
)


def run_nmap(target):
    """
    Runs SAFE Nmap scan only.
    Returns parsed results as dict.
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as tmp:
        xml_file = tmp.name

    cmd = [
        "nmap",
        "-sV",                # service/version detection
        "-Pn",                # no host discovery (safe)
        "--script", SAFE_NSE, # safe NSE scripts only
        "-oX", xml_file,
        target
    ]

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        results = parse_nmap_xml(xml_file)
        return results

    finally:
        if os.path.exists(xml_file):
            os.remove(xml_file)


def parse_nmap_xml(xml_path):
    """
    Parses Nmap XML output into structured data.
    """

    tree = ET.parse(xml_path)
    root = tree.getroot()

    findings = []

    for host in root.findall("host"):
        for port in host.findall(".//port"):
            port_id = port.get("portid")
            service = port.find("service")

            service_name = service.get("name") if service is not None else "unknown"
            service_version = service.get("version") if service is not None else ""

            for script in port.findall("script"):
                findings.append({
                    "port": port_id,
                    "service": service_name,
                    "version": service_version,
                    "script": script.get("id"),
                    "output": script.get("output")
                })

    return findings

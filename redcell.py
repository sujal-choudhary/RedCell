# =========================
# RedCell Main Entry Point
# =========================

import sys
import os

# Ensure project root is in Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from rich import print

from core.nlp_engine import process_command
from core.intent_mapper import detect_intent
from core.groq_client import ask_ai

from modules.info_gathering import gather_information
from modules.vulnerability_analysis import fetch_cves, risk_score
from modules.nmap_scan import run_nmap

from config.settings import ENABLE_GROK, APP_NAME, VERSION


def show_banner():
    print(f"[bold red]🔴 {APP_NAME} AI[/bold red]  [white]v{VERSION}[/white]")
    print("[dim]AI-powered security assistant (Passive & Authorized Mode)[/dim]\n")


def main():
    show_banner()
    print("Type your command (or 'exit')\n")

    while True:
        try:
            user_input = input("🧠 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("[green]RedCell shutting down safely...[/green]")
                break

            # =========================
            # NLP + INTENT
            # =========================
            nlp_data = process_command(user_input)
            intent_data = detect_intent(nlp_data["tokens"])

            intent = intent_data["intent"]
            confidence = intent_data["confidence"]
            target = nlp_data["target"]

            print("\n[cyan]🔍 RedCell Understanding[/cyan]")
            print(f"Intent     : {intent}")
            print(f"Confidence : {confidence}")
            print(f"Target     : {target}")

            # =========================
            # INFORMATION GATHERING
            # =========================
            if intent == "information_gathering":
                if not target:
                    print("[yellow]⚠ No target detected.[/yellow]")
                    continue

                print("\n[bold green]🔍 Information Gathering (Passive)...[/bold green]")

                info = gather_information(target)

                print("\n[bold cyan]📊 Raw Findings[/bold cyan]")
                for k, v in info.items():
                    print(f"{k}: {v}")

                if ENABLE_GROK:
                    summary = ask_ai(
                        f"Domain: {info['domain']}, "
                        f"IP: {info['ip_address']}, "
                        f"Technologies: {info['technologies']}. "
                        "Summarize findings briefly."
                    )
                    print("\n[bold yellow]🧠 AI Summary[/bold yellow]")
                    print(summary)

            # =========================
            # VULNERABILITY ANALYSIS (PASSIVE)
            # =========================
            elif intent == "vulnerability_analysis":
                if not target:
                    print("[yellow]⚠ No target detected.[/yellow]")
                    continue

                print("\n[bold green]🛡 Running Vulnerability Analysis...[/bold green]")

                # ---- Step 1: Info gathering ----
                info = gather_information(target)
                technologies = info.get("technologies", [])

                # ---- Step 2: CVE correlation ----
                all_cves = []
                for tech in technologies:
                    keyword = tech.split(":")[-1].strip()
                    all_cves.extend(fetch_cves(keyword))

                cve_risk = risk_score(all_cves)

                # ---- Step 3: Nmap safe scan ----
                print("\n[bold green]🧪 Running Nmap Safe Scan...[/bold green]")
                nmap_results = run_nmap(target)

                print("\n[bold cyan]📡 Nmap Findings[/bold cyan]")
                if not nmap_results:
                    print("No issues detected by Nmap.")
                else:
                    for item in nmap_results:
                        print(
                            f"- Port {item['port']} | "
                            f"{item['service']} {item['version']} | "
                            f"Script: {item['script']}"
                        )

                # ---- Step 4: Risk scoring ----
                final_risk = risk_score(all_cves + nmap_results)

                print("\n[cyan]📊 Risk Assessment[/cyan]")
                print(f"Risk Level: {final_risk}")

                # ---- Step 5: AI confirmation ----
                if ENABLE_GROK:
                    summary = ask_ai(
                        f"""
Target: {target}
Technologies: {technologies}
CVEs Found: {all_cves}
Nmap Findings: {nmap_results}
Risk Level: {final_risk}

Confirm whether vulnerabilities are real or informational.
Keep answer short.
"""
                    )
                    print("\n[bold yellow]🧠 AI Vulnerability Confirmation[/bold yellow]")
                    print(summary)

            # =========================
            # EXPLOIT (BLOCKED)
            # =========================
            elif intent == "exploit":
                print("\n[bold red]⛔ Exploitation Disabled[/bold red]")
                print("Only analysis and validation are allowed.")

            # =========================
            # REPORT (PLACEHOLDER)
            # =========================
            elif intent == "report":
                print("\n[yellow]📄 Report module coming next.[/yellow]")

            # =========================
            # HELP
            # =========================
            elif intent == "help":
                print("""
[bold cyan]Available Commands[/bold cyan]
- Find information about <domain>
- Analyze security of <domain>
- Generate report
- Exit
                """)

            else:
                print("\n[yellow]🤔 Command not understood.[/yellow]")

        except KeyboardInterrupt:
            print("\n[green]Interrupted. Exiting safely.[/green]")
            break

        except Exception as e:
            print(f"\n[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    main()

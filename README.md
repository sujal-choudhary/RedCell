
---

# 🔴 RedCell

**RedCell** is an AI-assisted **cybersecurity analysis framework** designed for **information gathering, passive vulnerability analysis, and risk assessment** — with a strong focus on **ethical, authorized, and non-destructive security testing**.

It combines **NLP, automation, Nmap, CVE correlation, and AI reasoning** to help security learners and professionals understand *what is vulnerable, why it is vulnerable, and how risky it is* — without performing real-world exploitation.

---

## 🚀 Key Features

### 🧠 Natural Language Interface

Interact with RedCell using simple commands:

```
Hey RedCell, find information about example.com
Analyze security of testphp.vulnweb.com
```

RedCell understands intent using NLP and maps it to the correct security workflow.

---

### 🔍 Information Gathering (Passive)

* DNS & IP resolution
* HTTP response headers
* SSL/TLS certificate inspection
* Basic technology fingerprinting

✔ No intrusive scanning
✔ Read-only analysis

---

### 🛡 Vulnerability Analysis (Passive)

* CVE correlation using public databases (NVD)
* Risk classification (Low / Medium / High)
* Misconfiguration detection (headers, TLS, services)

---

### 🧪 Nmap Integration (Safe Mode)

RedCell integrates **Nmap** using:

* Service & version detection
* Safe NSE vulnerability scripts only
* XML parsing for structured analysis

❌ No exploit scripts
❌ No brute-force
❌ No aggressive scanning

---

### 🤖 AI-Powered Security Reasoning

RedCell uses an LLM (via Groq API) **only for explanation and validation**, not exploitation.

The AI:

* Explains findings briefly
* Confirms whether vulnerabilities are real or informational
* Suggests safe next steps
* Keeps responses short and technical

---

### 🔐 Ethical & Secure by Design

* Exploitation is **disabled by default**
* Designed for:

  * Labs
  * Test environments
  * Learning platforms
* Clear separation between **analysis** and **attack**

RedCell is built to be **portfolio-safe, recruiter-safe, and legally safe**.

---

## 🧱 Architecture Overview

```
User Command
   ↓
NLP Engine
   ↓
Intent Mapper
   ↓
Information Gathering
   ↓
Vulnerability Analysis
   ↓
Nmap (Safe Scripts)
   ↓
Risk Scoring
   ↓
AI Validation
```

---

## 📂 Project Structure

```
RedCell/
├── redcell.py
├── core/
│   ├── nlp_engine.py
│   ├── intent_mapper.py
│   └── groq_client.py
├── modules/
│   ├── info_gathering.py
│   ├── vulnerability_analysis.py
│   └── nmap_scan.py
├── config/
│   ├── intents.json
│   └── settings.py
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/sujal-choudhary/RedCell.git
cd RedCell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set API key (for AI explanations):

```bash
export GROQ_API_KEY="your_api_key"
```

---

## ▶️ Usage

Run RedCell:

```bash
python redcell.py
```

Example commands:

```
Find information about example.com
Analyze security of testphp.vulnweb.com
Help
Exit
```

---

## 🎯 Intended Use

RedCell is designed for:

* Cybersecurity students
* Ethical hacking learners
* SOC / blue-team practice
* Portfolio projects
* Security automation experiments

It is **not** intended for:

* Illegal hacking
* Unauthorized scanning
* Real-world exploitation

---

## 🧠 Why RedCell?

Most tools either:

* Only scan, or
* Only exploit, or
* Don’t explain results

**RedCell bridges the gap** by combining:

* Automation
* Evidence-based analysis
* Human-readable explanations
* Ethical controls

---

## 📌 Roadmap

* 📄 Report Generator (JSON / TXT / PDF)
* 🔐 Scope & authorization system
* 🧪 Exploit simulation (lab-only)
* 🌐 Web dashboard
* 📊 CVSS-based scoring

---

## ⚠️ Disclaimer

RedCell must be used **only on systems you own or have explicit permission to test**.
The authors are not responsible for misuse.

---

## 🧑‍💻 Author

**Sujal Choudhary**
Cybersecurity & AI Automation Enthusiast

---

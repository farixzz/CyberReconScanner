import subprocess
import os
import pexpect

def run_scan(domain, scan_type, force=False, custom_sqlmap_url=None, custom_port=None):
    gobuster_url = f"http://{domain}"
    if custom_port:
        gobuster_url += f":{custom_port}"

    tools = {
        "nmap": ["nmap", "-sV"] + (["-Pn"] if force else []) + [domain],
        "nikto": ["nikto", "-h", domain],
        "sqlmap": ["sqlmap", "-u", custom_sqlmap_url if custom_sqlmap_url else f"http://{domain}/index.php?id=1", "--batch"],
        "gobuster": ["gobuster", "dir", "-u", gobuster_url, "-w", "/usr/share/wordlists/dirb/common.txt"],
        "shodan": ["shodan", "host", domain],
        "metasploit": [
            "msfconsole", "-q", "-x",
            (
                f"use auxiliary/scanner/portscan/tcp; set RHOSTS {domain}; run; "
                f"use auxiliary/scanner/smb/smb_version; set RHOSTS {domain}; run; "
                f"use auxiliary/scanner/http/http_version; set RHOSTS {domain}; run; exit"
            )
        ]
    }

    selected_tools = tools.keys() if scan_type == "all" else [scan_type]
    os.makedirs("results", exist_ok=True)

    for tool in selected_tools:
        yield f"Running {tool} scan..."
        try:
            if tool == "gobuster":
                test_url = gobuster_url
                try:
                    test = subprocess.run(["curl", "-Is", test_url], capture_output=True, timeout=5)
                    if b"200" not in test.stdout and b"301" not in test.stdout:
                        gobuster_url = gobuster_url.replace("http://", "https://")
                        yield f"[i] HTTP unreachable, switching Gobuster to HTTPS: {gobuster_url}"
                except:
                    gobuster_url = gobuster_url.replace("http://", "https://")
                    yield f"[i] HTTP check failed, defaulting Gobuster to HTTPS: {gobuster_url}"
                tools["gobuster"] = ["gobuster", "dir", "-u", gobuster_url, "-w", "/usr/share/wordlists/dirb/common.txt"]

            command = tools[tool]
            yield f"Command executed: {' '.join(command)}"

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=300
            )
            output = result.stdout + result.stderr
            log_entry = f"--- {tool.upper()} SCAN OUTPUT ---\n{output}\n"

            with open(f"results/{tool}_scan.txt", "w") as f:
                f.write(log_entry)

            for line in log_entry.strip().splitlines():
                yield line

            yield f"{tool} scan completed."

        except subprocess.TimeoutExpired:
            yield f"{tool} scan timed out."
        except FileNotFoundError:
            yield f"{tool} tool not found."
        except Exception as e:
            yield f"Error running {tool}: {str(e)}"


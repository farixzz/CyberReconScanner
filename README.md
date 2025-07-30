# 🛡️ Cyber Recon Scanner

A Python-based GUI tool for offensive reconnaissance, integrating powerful scanning utilities like Nmap, Nikto, SQLMap, Gobuster, Metasploit, and Hydra — all under one sleek interface powered by `CustomTkinter`.

![Cyber Recon Scanner Banner](A_professional_digital_graphic_banner_showcases_%22C.png)

---

## 🚀 Features

- 🔍 One-click scan execution via GUI
- 🧠 Intelligent domain/IP recognition
- 📦 Results saved automatically (`/results` folder)
- ⚙️ Customizable scan options (ports, SQLMap URLs, force mode)
- 🧾 Exportable PDF scan reports (coming soon!)
- 🪪 Dark Mode GUI powered by `CustomTkinter`
- 🛠 Hydra Brute Force login support
- ✅ Supports both `HTTP` & `HTTPS` fallback

---

## 🔧 Tools Integrated

| Tool       | Purpose                         |
|------------|----------------------------------|
| **Nmap**   | Port scanning & service detection |
| **Nikto**  | Web server vulnerability scan     |
| **SQLMap** | SQL injection testing             |
| **Gobuster** | Directory brute forcing          |
| **Metasploit** | Multi-module exploit scanner  |
| **Hydra**  | Brute-force login on protocols (FTP, SSH, HTTP, etc.) |

---

## 🖥️ GUI Screenshot

> 

![GUI Screenshot](/screenshot-cyber-recon-scanner.png)

---

## 💾 Installation

### 🔗 Requirements

- Python 3.10+
- Git
- Dependencies (see below)

### 🐍 Install dependencies

```bash
pip install -r requirements.txt
```

### 🛠 Setup Instructions

```bash
git clone https://github.com/farixzz/CyberReconScanner.git
cd CyberReconScanner
python main.py
```

---

## 🧠 How to Use

1. Run `main.py`
2. Enter the target IP or domain.
3. Select tools to include (e.g., Nmap, Hydra).
4. Hit **"Run Scan"** and view results in terminal or `/results` folder.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

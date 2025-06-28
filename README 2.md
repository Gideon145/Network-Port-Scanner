# Network Port Scanner 🔍

A simple Python script that scans a target host for open ports using basic socket programming.

## 💡 What It Does

- Takes a hostname or IP address as input
- Scans a list of common ports (e.g., 22, 80, 443)
- Prints out which ports are open

## 🛠 Technologies Used

- Python 3
- `socket` module

## 🧪 How to Use

1. Clone the repo:
```bash
git clone https://github.com/yourusername/network-port-scanner
cd network-port-scanner
```

2. Run the script:
```bash
python network_port_scanner.py
```

3. Enter a host (like `google.com` or `127.0.0.1`), and get your results.

## 🚀 Future Improvements

- Add threading for faster scanning
- Allow custom port range input
- Save results to a file
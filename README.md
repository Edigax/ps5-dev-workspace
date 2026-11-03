# PlayStation 5 Homebrew & Development Workspace

A clean, self-contained development suite for setting up, compiling, and testing open-source homebrew software on macOS and Linux.

---

## 📌 Scope & Compliance Notice

This repository contains **only** open-source build configurations, development scripts, and reference projects.
- **No Proprietary Code**: Does not host Sony proprietary SDK files, system binaries, or copyrighted headers.
- **No Exploits**: Does not contain or distribute kernel exploits, vulnerability chains, or DRM circumvention tools.
- **Compliant**: Designed for community homebrew development in compliance with GitHub Acceptable Use Policies and open-source licenses.

---

## 📁 Repository Structure

```text
ps5-dev-workspace/
├── .gitignore               # Excludes binaries, build artifacts, and vendor caches
├── LICENSE                  # MIT License
├── README.md                # Workspace documentation and guide
├── env.sh                   # Environment activator (sets PATH and PS5_SDK)
├── setup.sh                 # Dependency check and automated SDK setup
├── tools/
│   ├── send_payload.py      # Network socket streamer to send userland ELFs to console
│   └── sync_repos.py        # Clones curated open-source homebrew repositories
└── samples/
    └── hello_world/         # Clean starter homebrew application template
        ├── Makefile         # Build configuration
        └── main.c           # Sample userland application
```

---

## 🛠️ Prerequisites

Ensure the following tools are installed on your host system:

### macOS
```bash
# Install Xcode Command Line Tools (includes Clang & Git)
xcode-select --install

# Install build tools via Homebrew
brew install cmake ninja python3
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y build-essential clang llvm lld cmake ninja-build git python3
```

---

## 🚀 Quick Start Guide

### 1. Initialize the Workspace
Run the automated setup script to verify dependencies and fetch the open-source SDK:
```bash
chmod +x setup.sh env.sh
./setup.sh
```

### 2. Activate the Environment
Source `env.sh` in your active terminal:
```bash
source env.sh
```

### 3. Build the Starter Sample
```bash
cd samples/hello_world
make
```
This produces `hello_world.elf` compiled for the target platform.

### 4. Transmit to Your Console
If you have an ELF listener running on your console:
```bash
python3 tools/send_payload.py samples/hello_world/hello_world.elf --ip <PS5_IP_ADDRESS> --port 9021
```

---

## 📚 Curated Open-Source Repositories

The following repositories are maintained by the community under the [`ps5-payload-dev`](https://github.com/ps5-payload-dev) organization for userland development:

| Project | Description | Source |
| :--- | :--- | :--- |
| **sdk** | Core open-source userland C SDK, libc stubs, and linker scripts | [GitHub](https://github.com/ps5-payload-dev/sdk) |
| **elfldr** | Resident userland background ELF loader daemon (port 9021) | [GitHub](https://github.com/ps5-payload-dev/elfldr) |
| **ftpsrv** | Multi-threaded FTP server utility (port 2121) | [GitHub](https://github.com/ps5-payload-dev/ftpsrv) |
| **websrv** | Lightweight HTTP web server utility (port 8080) | [GitHub](https://github.com/ps5-payload-dev/websrv) |
| **shsrv** | Telnet debug shell interface (port 2323) | [GitHub](https://github.com/ps5-payload-dev/shsrv) |
| **klogsrv** | Console log socket redirector (port 3232) | [GitHub](https://github.com/ps5-payload-dev/klogsrv) |
| **gdbsrv** | Remote GDB debugging server | [GitHub](https://github.com/ps5-payload-dev/gdbsrv) |
| **SDL** | Simple DirectMedia Layer 2.0 port for PS5 | [GitHub](https://github.com/ps5-payload-dev/SDL) |
| **libcross2d**| Cross-platform 2D graphics engine library | [GitHub](https://github.com/ps5-payload-dev/libcross2d) |
| **LakeSnes** | Open-source SNES emulator | [GitHub](https://github.com/ps5-payload-dev/LakeSnes) |
| **FBNeo** | FinalBurn Neo arcade emulator port | [GitHub](https://github.com/ps5-payload-dev/FBNeo) |
| **yquake2** | Yamagi Quake II game engine port | [GitHub](https://github.com/ps5-payload-dev/yquake2) |
| **jtplay** | Audio and media playback utility | [GitHub](https://github.com/ps5-payload-dev/jtplay) |

To automatically clone all curated repositories into `repos/`:
```bash
python3 tools/sync_repos.py
```

---

## 📄 License

This workspace is licensed under the [MIT License](LICENSE). Third-party submodules and SDK libraries belong to their respective open-source copyright holders.

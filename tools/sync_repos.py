#!/usr/bin/env python3
"""
Sync Open-Source PS5 Developer Repositories
Clones or updates curated open-source development tools and userland samples from github.com/ps5-payload-dev.
"""

import json
import os
import subprocess
import sys
import urllib.request

CURATED_REPOS = [
    {"name": "sdk", "desc": "Open-source userland SDK and headers"},
    {"name": "elfldr", "desc": "ELF loader daemon"},
    {"name": "ftpsrv", "desc": "FTP server payload"},
    {"name": "websrv", "desc": "Lightweight HTTP server payload"},
    {"name": "shsrv", "desc": "Telnet shell service"},
    {"name": "klogsrv", "desc": "Kernel log socket daemon"},
    {"name": "gdbsrv", "desc": "Remote GDB debugging server"},
    {"name": "SDL", "desc": "PS5 Simple DirectMedia Layer port"},
    {"name": "libcross2d", "desc": "2D graphics rendering library"},
    {"name": "LakeSnes", "desc": "SNES emulator for PS5"},
    {"name": "FBNeo", "desc": "FinalBurn Neo emulator port"},
    {"name": "yquake2", "desc": "Yamagi Quake II client port"},
    {"name": "jtplay", "desc": "Media player utility"},
    {"name": "launchpad", "desc": "Application launchpad"},
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "repos")

def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    print("=================================================================")
    print(" Syncing Curated Open-Source PS5 Development Repositories")
    print("=================================================================")

    for idx, item in enumerate(CURATED_REPOS, 1):
        name = item["name"]
        desc = item["desc"]
        dest = os.path.join(TARGET_DIR, name)
        url = f"https://github.com/ps5-payload-dev/{name}.git"

        print(f"[{idx:02d}/{len(CURATED_REPOS)}] {name} - {desc}")
        if os.path.isdir(os.path.join(dest, ".git")):
            print(f"       -> Updating existing repository...")
            subprocess.run(["git", "pull", "--ff-only"], cwd=dest, capture_output=True)
        else:
            print(f"       -> Cloning from {url}...")
            subprocess.run(["git", "clone", "--depth", "1", url, dest], capture_output=True)

    print("=================================================================")
    print(f"[+] All repositories synced in: {TARGET_DIR}")
    print("=================================================================")

if __name__ == "__main__":
    main()

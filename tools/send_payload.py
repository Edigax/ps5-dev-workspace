#!/usr/bin/env python3
"""
PS5 Homebrew Payload Sender Utility
Transmits compiled userland ELF files over standard TCP socket to an active listener (port 9021 / 9020).
"""

import argparse
import os
import socket
import sys
import time

DEFAULT_PORT = 9021

def send_payload(host: str, port: int, file_path: str, timeout: int = 15):
    if not os.path.isfile(file_path):
        print(f"[ERROR] File not found: {file_path}", file=sys.stderr)
        return False

    file_size = os.path.getsize(file_path)
    print(f"[*] File: {os.path.basename(file_path)} ({file_size:,} bytes)")
    print(f"[*] Target: {host}:{port}")

    try:
        start_time = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            print(f"[*] Connecting to {host}:{port}...")
            s.connect((host, port))
            print(f"[+] Connected. Sending file...")

            sent_bytes = 0
            with open(file_path, "rb") as f:
                while chunk := f.read(65536):
                    s.sendall(chunk)
                    sent_bytes += len(chunk)
                    pct = (sent_bytes / file_size) * 100
                    sys.stdout.write(f"\r[*] Progress: {pct:5.1f}% ({sent_bytes:,}/{file_size:,} bytes)")
                    sys.stdout.flush()

            elapsed = time.time() - start_time
            print(f"\n[+] Completed successfully in {elapsed:.2f}s.")
            return True

    except socket.timeout:
        print(f"\n[ERROR] Connection timed out to {host}:{port}.", file=sys.stderr)
        return False
    except ConnectionRefusedError:
        print(f"\n[ERROR] Connection refused on {host}:{port}. Is the listener service running?", file=sys.stderr)
        return False
    except Exception as e:
        print(f"\n[ERROR] Network error: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Send ELF binary to PS5")
    parser.add_argument("file", help="Path to ELF binary file to send")
    parser.add_argument("--ip", required=True, help="IP address of the target PS5 console")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Destination port (default: {DEFAULT_PORT})")
    parser.add_argument("--timeout", type=int, default=15, help="Socket timeout in seconds")

    args = parser.parse_args()
    success = send_payload(args.ip, args.port, args.file, args.timeout)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

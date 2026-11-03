#!/usr/bin/env bash
# ==============================================================================
# PS5 Homebrew Workspace Automated Setup Script
# ==============================================================================
set -e

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${WORKSPACE_ROOT}"

echo "================================================================="
echo " Setting up PS5 Homebrew & Development Workspace"
echo "================================================================="

# 1. Check required host tools
MISSING_TOOLS=()
for tool in git cmake python3; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        MISSING_TOOLS+=("$tool")
    fi
done

if [ ${#MISSING_TOOLS[@]} -ne 0 ]; then
    echo "[ERROR] Missing required host dependencies: ${MISSING_TOOLS[*]}"
    echo "Please install them via your package manager (e.g., brew install ${MISSING_TOOLS[*]} on macOS)."
    exit 1
fi
echo "[+] Host prerequisites detected: git, cmake, python3."

# 2. Check compiler (LLVM / Clang)
if ! command -v clang >/dev/null 2>&1 && [ ! -f "${WORKSPACE_ROOT}/toolchain/llvm/bin/clang" ]; then
    echo "[!] Warning: Clang compiler not found on PATH."
    echo "    On macOS, install Xcode command line tools: xcode-select --install"
    echo "    On Linux, install LLVM: sudo apt install llvm clang lld"
else
    echo "[+] Clang toolchain detected."
fi

# 3. Clone open-source PS5 Payload SDK
if [ ! -d "${WORKSPACE_ROOT}/sdk" ]; then
    echo "[*] Cloning official open-source PS5 SDK (github.com/ps5-payload-dev/sdk)..."
    git clone --depth 1 https://github.com/ps5-payload-dev/sdk.git "${WORKSPACE_ROOT}/sdk"
    echo "[+] SDK cloned successfully."
else
    echo "[+] PS5 SDK already exists at ${WORKSPACE_ROOT}/sdk."
fi

# 4. Make scripts executable
chmod +x "${WORKSPACE_ROOT}/env.sh"
chmod +x "${WORKSPACE_ROOT}/setup.sh"
chmod +x "${WORKSPACE_ROOT}/tools/"*.py 2>/dev/null || true

echo "================================================================="
echo "[+] Workspace setup complete!"
echo "To begin, activate the environment:"
echo "    source env.sh"
echo "================================================================="

#!/usr/bin/env bash
# ==============================================================================
# PS5 Homebrew & Payload Development Workspace Environment Activator
# Source this file in your shell:
#   source env.sh
# ==============================================================================

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PS5_WORKSPACE="${WORKSPACE_ROOT}"
export PS5_SDK="${WORKSPACE_ROOT}/sdk"

# Add toolchain utilities to PATH if custom toolchain is installed
if [ -d "${WORKSPACE_ROOT}/toolchain/llvm/bin" ]; then
    export PATH="${WORKSPACE_ROOT}/toolchain/llvm/bin:${PATH}"
fi

# Add SDK binaries to PATH
if [ -d "${PS5_SDK}/bin" ]; then
    export PATH="${PS5_SDK}/bin:${PATH}"
fi

# Add local tools directory
export PATH="${WORKSPACE_ROOT}/tools:${PATH}"

echo "================================================================="
echo "  PlayStation 5 Homebrew Development Workspace"
echo "================================================================="
echo "  WORKSPACE: ${PS5_WORKSPACE}"
echo "  PS5_SDK:   ${PS5_SDK}"
if command -v prospero-clang >/dev/null 2>&1; then
    echo "  COMPILER:  $(which prospero-clang)"
elif command -v clang >/dev/null 2>&1; then
    echo "  COMPILER:  $(which clang)"
else
    echo "  COMPILER:  [Notice] Run ./setup.sh to configure SDK and toolchain."
fi
echo "================================================================="

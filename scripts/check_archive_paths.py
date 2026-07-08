#!/usr/bin/env python3
"""Static ZIP path safety checks.

WARNING: This script lists ZIP metadata only. It does not extract or execute files.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import PurePosixPath, PureWindowsPath


EXECUTABLE_SUFFIXES = {
    ".exe",
    ".dll",
    ".scr",
    ".ps1",
    ".bat",
    ".cmd",
    ".js",
    ".vbs",
    ".jar",
    ".sh",
    ".msi",
    ".so",
    ".dylib",
}

ARCHIVE_SUFFIXES = {".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".xz", ".bz2"}


def has_traversal(name: str) -> bool:
    parts = PurePosixPath(name.replace("\\", "/")).parts
    return ".." in parts


def is_absolute_or_drive(name: str) -> bool:
    posix_name = name.replace("\\", "/")
    win = PureWindowsPath(name)
    return posix_name.startswith("/") or posix_name.startswith("//") or win.is_absolute() or bool(win.drive)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <zipfile>", file=sys.stderr)
        return 2

    archive = sys.argv[1]
    findings: list[str] = []

    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            name = info.filename
            suffix = PurePosixPath(name.lower()).suffix
            mode = (info.external_attr >> 16) & 0o170000
            is_symlink = mode == 0o120000

            print(f"{name}\tcompressed={info.compress_size}\tuncompressed={info.file_size}")

            if has_traversal(name):
                findings.append(f"path traversal: {name}")
            if is_absolute_or_drive(name):
                findings.append(f"absolute or drive path: {name}")
            if is_symlink:
                findings.append(f"symlink entry: {name}")
            if suffix in EXECUTABLE_SUFFIXES:
                findings.append(f"executable-like suffix: {name}")
            if suffix in ARCHIVE_SUFFIXES:
                findings.append(f"nested archive-like suffix: {name}")
            if PurePosixPath(name).name.startswith("."):
                findings.append(f"hidden file: {name}")

    if findings:
        print("\nfindings:", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print("\nno path-safety findings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

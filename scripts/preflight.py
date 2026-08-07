#!/usr/bin/env python3
"""Check whether a workstation can host the ERA SOFT v16 development bench."""

from __future__ import annotations

import shutil
import subprocess
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
	name: str
	command: tuple[str, ...]
	required: bool = True


CHECKS = (
	Check("Git", ("git", "--version")),
	Check("Python 3.14", ("python3.14", "--version")),
	Check("Node.js 24", ("node", "--version")),
	Check("Yarn", ("yarn", "--version")),
	Check("Bench CLI", ("bench", "--version")),
	Check("Docker", ("docker", "--version"), required=False),
	Check("Docker Compose", ("docker", "compose", "version"), required=False),
)


def run(check: Check) -> tuple[bool, str]:
	executable = check.command[0]
	if shutil.which(executable) is None:
		return False, "not found"

	result = subprocess.run(check.command, capture_output=True, check=False, text=True)
	message = (result.stdout or result.stderr).strip().splitlines()
	return result.returncode == 0, message[0] if message else f"exit {result.returncode}"


def main() -> int:
	failed_required = False
	print("ERA SOFT development preflight\n")
	for check in CHECKS:
		ok, detail = run(check)
		label = "OK" if ok else ("MISSING" if check.required else "OPTIONAL")
		print(f"[{label:8}] {check.name}: {detail}")
		failed_required |= check.required and not ok

	if failed_required:
		print("\nRequired tools are missing. Follow docs/LOCAL_DEVELOPMENT.md.")
		return 1

	print("\nRequired commands are available. Verify exact major versions above.")
	return 0


if __name__ == "__main__":
	sys.exit(main())

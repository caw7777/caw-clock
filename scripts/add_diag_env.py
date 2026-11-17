#!/usr/bin/env python3
"""Add the diagnostic-only sdpro_caw_diag PlatformIO environment.

Usage: add_diag_env.py <source-root>   (the directory that holds firmware/)

Run it on the extracted source archive. It
  * appends [env:sdpro_caw_diag] to firmware/platformio.ini, inheriting every
    option of [env:sdpro_caw] (flags, ldscript, extra_scripts, libraries), and
  * copies scripts/diag_build.py into firmware/scripts/.

The production environments are not modified. The environment is only built
when named explicitly (-e sdpro_caw_diag); default_envs stays `sdpro`.
"""
from pathlib import Path
import shutil
import sys

ENV_BLOCK = """
; DIAGNOSTIC ONLY - never flash the image this environment produces.
; Identical to sdpro_caw except that the OTA size gate is raised so that the
; ELF, map and binary can be inspected. The production limit used by
; sdpro_caw (1,044,464 bytes) is not changed.
[env:sdpro_caw_diag]
extends = env:sdpro_caw
board_upload.maximum_size = 2000000
extra_scripts =
  ${env:sdpro_caw.extra_scripts}
  post:scripts/diag_build.py
"""

root = Path(sys.argv[1])
ini = root / "firmware/platformio.ini"
text = ini.read_text()
if "[env:sdpro_caw]" not in text:
    raise SystemExit("sdpro_caw profile not found in platformio.ini")
if "[env:sdpro_caw_diag]" in text:
    raise SystemExit("sdpro_caw_diag already present; refusing to add it twice")
if not text.endswith("\n"):
    text += "\n"
ini.write_text(text + ENV_BLOCK)

helper = Path(__file__).resolve().parent / "diag_build.py"
shutil.copyfile(helper, root / "firmware/scripts/diag_build.py")
print("Added [env:sdpro_caw_diag] and firmware/scripts/diag_build.py")

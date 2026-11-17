"""Diagnostic-only SCons helper for env:sdpro_caw_diag.

PURPOSE
    Let PlatformIO finish linking an image that is larger than the OTA slot so
    the ELF, map file and binary can be inspected.

WHAT IT CHANGES (diagnostic environment only)
    1. Raises PlatformIO's in-memory board `upload.maximum_size` so the size
       gate does not fail the build. This is a belt-and-braces copy of the
       `board_upload.maximum_size` option in platformio.ini, applied after the
       platform and framework scripts have run.
    2. Asks the linker for a map file next to firmware.elf.

WHAT IT NEVER TOUCHES
    The production limit (1,044,464 bytes) and the `sdpro_caw` / `sdpro`
    environments. The script refuses to run in any other environment.

The resulting firmware.bin must never be flashed.
"""

import os

Import("env")  # noqa: F821 - PlatformIO/SCons build environment

RELEASE_OTA_LIMIT = 1044464
DIAG_ENV = "sdpro_caw_diag"
diag_limit = int(os.environ.get("CAW_DIAG_MAX_SIZE", "2000000"))

if env["PIOENV"] != DIAG_ENV:  # noqa: F821
    raise RuntimeError(
        f"diag_build.py is diagnostic-only and must not be used by "
        f"{env['PIOENV']!r}"  # noqa: F821
    )
if diag_limit <= RELEASE_OTA_LIMIT:
    raise RuntimeError(
        f"CAW_DIAG_MAX_SIZE={diag_limit} must exceed the release limit "
        f"{RELEASE_OTA_LIMIT}; this env exists to build oversized images"
    )

board = env.BoardConfig()  # noqa: F821
before = board.get("upload.maximum_size", "unset")
try:
    board.update("upload.maximum_size", diag_limit)
except Exception as exc:  # never let the helper break the diagnostic build
    print(f"[diag] WARNING: could not update upload.maximum_size: {exc!r}")
after = board.get("upload.maximum_size", "unset")
print(
    f"[diag] {DIAG_ENV}: upload.maximum_size {before} -> {after}. "
    f"Release limit {RELEASE_OTA_LIMIT} is unchanged; DO NOT FLASH this image."
)

map_path = env.subst("$BUILD_DIR/firmware.map")  # noqa: F821
env.Append(LINKFLAGS=["-Wl,-Map," + map_path])  # noqa: F821

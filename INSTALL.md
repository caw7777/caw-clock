# Installing CAW Clock

A step-by-step guide for every supported clock. Pick your model, follow the
route for the firmware it runs today, then do the [first-time setup](#first-time-setup).

> **Golden rule:** never unplug the clock while it shows **Updating** or while
> it restarts after an install. Everything else in this guide is safe to retry.

## 1. Which clock do you have?

| Clock | Chip | CAW Clock support |
|---|---|---|
| **JUZIPi SD PRO** ("Smart Weather Clock"), ESP8266 board ("SDP") | ESP8266 | ✅ Supported and tested |
| **JUZIPi SD PRO**, ESP32-C2 board ("SDC2") | ESP32-C2 | ✅ Supported from v0.7.0 |
| GeekMagic SmallTV / SmallTV Ultra | ESP8266 | 🔜 Planned, needs a test unit |
| GeekMagic SmallTV Pro | ESP32 | 🔜 Planned (port), needs a test unit |
| GeekMagic SmallTV ESP32-C2 | ESP32-C2 | 🔜 Planned (port), needs a test unit |

**Don't rename the files.** The name is how a clock's factory updater knows
a file is for it (`SDP...` for the ESP8266 board, `SDC2...` for the ESP32-C2
board). CAW Clock itself checks inside every file and refuses the other
board's firmware.

Only install CAW Clock on a model marked ✅. Firmware for the wrong board can
leave the screen blank, and then you can't read the setup key it shows.

**Which SD PRO board?** Both look the same. The factory firmware's update page
tells them apart: it only takes files whose names start with **SDP** on the
ESP8266 board and **SDC2** on the ESP32-C2 board (its version reads
"SDC2 ..."). Once CAW Clock runs, the **System** tab's **Check for updates**
picks the right file by itself.

## 2. Download the firmware

From the [latest release](https://github.com/caw7777/caw-clock/releases/latest)
download the file for your board:

| Board | File |
|---|---|
| ESP8266 (SDP) | `caw-clock-<version>.bin` (for example `caw-clock-0.7.0.bin`) |
| ESP32-C2 (SDC2), already running CAW Clock | `caw-clock-sdc2-<version>.bin` |
| ESP32-C2 (SDC2), factory firmware | `SDC2-CAW-Clock-Installer-<version>.bin` (route D) |

Optional check: `SHA256SUMS.txt` lists the file's fingerprint. On a computer:

- Windows (PowerShell): `Get-FileHash caw-clock-0.3.0.bin`
- macOS / Linux: `shasum -a 256 caw-clock-0.3.0.bin`

The result must match the line in `SHA256SUMS.txt`.

## 3. Install on the SD PRO with an ESP8266 board (SDP)

Find the firmware your clock runs now:

| The clock's web page or screen shows | Your route |
|---|---|
| **CAW CLOCK** in purple, crow picture | [A: update CAW Clock](#a-already-running-caw-clock) |
| **Home Assistant Mini-Display** / Mini Display panel | [B: from Mini Display](#b-from-home-assistant-mini-display-firmware) |
| The original **Smart Weather Clock** (weather, factory screens) | [C: from the factory firmware](#c-from-the-factory-firmware) |

### A. Already running CAW Clock

1. Open the clock's settings page (`http://<clock address>/`) and sign in as
   **admin** with your clock password.
2. On v0.4.0 or later: **System** tab → **Check for updates** → **Install**.
   Otherwise: **System** tab → **Install a file**, choose the `.bin` file,
   press **Install firmware**.
3. The screen shows **Updating**; the clock restarts by itself (about a
   minute). Your Wi-Fi, password and settings are kept.

No home Wi-Fi? Join the clock's setup network instead (see
[First-time setup](#first-time-setup)) and use the same Firmware section at
`http://192.168.4.1`.

### B. From Home Assistant Mini Display firmware

1. Open the Mini Display web page and sign in.
2. Go to **Firmware**, upload the CAW `.bin`, and wait for the restart.
3. CAW Clock keeps the Wi-Fi details and the interface password (now your
   clock password; user **admin**). Set your time zone on the settings page.
   **If you never set an interface password, the settings page is open to
   anyone on your network:** set a clock password there straight away.
4. In Home Assistant, remove the Mini Display device for this clock: CAW Clock
   doesn't use Home Assistant.

### C. From the factory firmware

You need the clock on your home Wi-Fi with its own web page working, and
internet access.

1. From the [latest release](https://github.com/caw7777/caw-clock/releases/latest)
   download `SDP-CAW-Clock-Installer-<version>.bin`. Don't rename it: the
   factory updater only accepts files whose name starts with `SDP`.
2. Open the clock's own web page (its address is in the clock's network
   settings or your router's device list) and upload the file in its firmware
   update section.
3. The clock restarts into the installer and shows a setup network
   (`CAW-Installer-XXXXXX`) and its key. Join it with your phone and open
   `http://192.168.4.1`.
4. Choose your Wi-Fi, enter its password, choose a clock password (8–32
   characters) and check the time zone, then press **Install**.
5. The installer downloads CAW Clock from the release, checks its SHA-256 and
   installs it. The clock restarts into CAW Clock, joins your Wi-Fi and shows
   its settings-page address. Sign in as **admin** with your clock password.

If the factory page shows **Not found**, the update handler still works: on a
computer joined to the same network, run this in the folder with the file
(PowerShell on Windows; `curl` on macOS or Linux):

```bash
curl.exe -F "update=@.\SDP-CAW-Clock-Installer-<version>.bin" http://<clock address>/update_ota
```

Prefer the longer way? Install the [Home Assistant Mini Display](https://github.com/piotrkochan/homeassistant-minidisplay#readme)
firmware with its bootstrap first, then follow
[route B](#b-from-home-assistant-mini-display-firmware).

## 4. Install on the SD PRO with an ESP32-C2 board (SDC2)

| The clock's web page or screen shows | Your route |
|---|---|
| **CAW CLOCK** in purple, crow picture | [A: update CAW Clock](#a-already-running-caw-clock) (the same as on the ESP8266 board) |
| The factory screens, firmware version **SDC2 ...** | [D: from the factory firmware](#d-from-the-factory-firmware-sdc2) |

### D. From the factory firmware (SDC2)

The clock must be on your home Wi-Fi with its factory firmware (as it comes
out of the box, set up with the factory instructions), with internet access.

1. From the [latest release](https://github.com/caw7777/caw-clock/releases/latest)
   download `SDC2-CAW-Clock-Installer-<version>.bin`. Don't rename it: the
   factory updater only accepts files whose name starts with `SDC2`.
2. Open the clock's factory web page (its address is in the clock's network
   settings or your router's device list), go to **Firmware Update (OTA)**,
   choose the file and upload it.
3. The clock restarts into the installer: the crow, **CAW CLOCK** and the
   version, then its progress: **JOINING WI-FI**, **DOWNLOADING**, **CHECKING**,
   **INSTALLING**, **DONE**. It takes a few minutes. Don't unplug it while it
   shows **INSTALLING**.
4. CAW Clock starts, joins the same Wi-Fi and shows **Connected** with its
   settings-page address for 10 seconds. Open it and sign in as **admin**
   (there is no password yet), then straight away set a **clock password**
   (**System** tab) and your **time zone** (**Display** tab: until then the
   clock shows UTC). Until a password
   is set, anyone on your network can change the settings.

Good to know:

- **One-way:** the installer replaces the factory firmware and arranges the
  flash for CAW Clock (two 1.5 MB program slots and 960 KB of storage).
  Going back to the factory firmware would need a USB-serial adapter.
- **Wi-Fi:** the installer uses the Wi-Fi the factory firmware saved. If
  there is none, or it can't join, the screen shows **WI-FI NEEDED** with a
  network (`CAW-Clock-XXXXXX`) and a key: join it, open `http://192.168.4.1`
  and enter your Wi-Fi name and password (2.4 GHz).
- **If the download fails** (no internet, GitHub unreachable) the installer
  tries again, and after the third failed try the clock goes back to its
  factory firmware, unchanged. Fix the connection and upload the installer
  again.
- The installer installs exactly the release it came with: it checks the
  download's SHA-256 against the one built into it before anything is
  changed.
- **Updates** afterwards: [route A](#a-already-running-caw-clock).
- **Automatic rollback** works differently on this board: if a new version
  keeps crashing when it starts, the clock goes back to the previous one by
  itself.

## First-time setup

After a first install on the ESP8266 board, or after **Factory reset** (on
either board):

1. The clock shows **Set up CAW Clock** with a network name
   (`CAW-Clock-XXXXXX`) and a **Key**.
2. On your phone or laptop, join that network using the key. If your phone
   says "no internet", choose to stay connected. Open `http://192.168.4.1`
   (it doesn't pop up by itself).
3. Pick your home network from the list. The clock needs **2.4 GHz** Wi-Fi;
   if yours isn't listed, tap **Scan again** or choose **Other network**.
4. Enter the Wi-Fi password, a **clock password** (8–32 characters, you'll
   need it to change settings) and check the time zone (taken from your
   phone).
5. Press **Save and connect**. The clock restarts, joins your Wi-Fi and shows
   **Connected** with its settings-page address for 10 seconds. Write the
   address down.

Prices and the chart appear within a minute or two.

## Everyday use

Settings page: `http://<clock address>/`, user **admin**, your clock password.

- **Status:** prices, burns, and the clock's address, signal and memory.
- **Display:** brightness, night mode, which chains to show and for how long,
  price alert, burn alert, supply screen, 12- or 24-hour clock, time zone.
- **Memes:** rotation, and adding or hiding memes.
- **System:** Wi-Fi and clock password (change either at any time), check
  for updates and install them (route A), restart, factory reset. A factory
  reset erases Wi-Fi, password and settings: do this before you give the
  clock away or sell it.

## Troubleshooting

| What you see | What to do |
|---|---|
| **Can't join Wi-Fi** / **Wi-Fi lost** with a reason | The clock reopens its setup network 2 minutes after losing Wi-Fi. Join it and fix the details. "network not found" usually means a typo or a 5 GHz-only network; "check the Wi-Fi password" means the password was refused. |
| Forgot the clock password | **Recovery mode:** unplug the clock and plug it back in **3 times in a row**, each time within 10 seconds. The screen shows **Recovery** with its setup network and key: join it, open `http://192.168.4.1` and enter a new clock password (leave the Wi-Fi password empty to keep it). Settings and memes are kept. The setup network closes by itself after 15 minutes. (Or: switch off your router for 2 minutes; the clock then opens its setup network too.) |
| Can't find the clock's address | Look for **caw-clock** in your router's list of devices, or restart the clock and read the **Connected** screen. |
| Prices show `--` | Normal for the first minute. If it stays, check the clock has internet; `http://<clock address>/api/status` shows each chain's last result. |
| **Safe mode** on the screen | The clock restarted several times in a row, so it paused price updates. The settings page still works: press **Restart normally**, or install other firmware. Please report it with a screenshot of `/api/status`. |
| Stuck on **Updating** | Wait 30 seconds: an interrupted upload is discarded and the normal screen returns. Then try the install again. |
| Screen dark at night | Night mode (Display settings) may be dimming or switching it off on purpose. |

## Advanced: USB-serial recovery

If a clock can't start at all (no screen, no setup network), the only fix is
writing the firmware over a USB-serial adapter. On the SD PRO this means
opening the case and connecting to the ESP8266's serial pins; there's no USB
data connection on the outside. With the module in flash mode:

```bash
esptool.py --port <your serial port> --baud 460800 write_flash 0x0 caw-clock-<version>.bin
```

Only attempt this if you're comfortable with electronics. CAW Clock's
**safe mode** is designed so you shouldn't need it.

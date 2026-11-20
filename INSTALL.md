# Installing CAW Clock

A step-by-step guide for every supported clock. Pick your model, follow the
route for the firmware it runs today, then do the [first-time setup](#first-time-setup).

> **Golden rule:** never unplug the clock while it shows **Updating** or while
> it restarts after an install. Everything else in this guide is safe to retry.

## 1. Which clock do you have?

| Clock | Chip | CAW Clock support |
|---|---|---|
| **JUZIPi SD PRO** ("Smart Weather Clock") | ESP8266 | ✅ Supported and tested |
| GeekMagic SmallTV / SmallTV Ultra | ESP8266 | 🔜 Planned, needs a test unit |
| GeekMagic SmallTV Pro | ESP32 | 🔜 Planned (port), needs a test unit |
| GeekMagic SmallTV ESP32-C2 | ESP32-C2 | 🔜 Planned (port), needs a test unit |

Only install CAW Clock on a model marked ✅. Firmware for the wrong board can
leave the screen blank, and then you can't read the setup key it shows.

## 2. Download the firmware

From the [latest release](https://github.com/caw7777/caw-clock/releases/latest)
download `caw-clock-<version>.bin` (for example `caw-clock-0.3.0.bin`).

Optional check: `SHA256SUMS.txt` lists the file's fingerprint. On a computer:

- Windows (PowerShell): `Get-FileHash caw-clock-0.3.0.bin`
- macOS / Linux: `shasum -a 256 caw-clock-0.3.0.bin`

The result must match the line in `SHA256SUMS.txt`.

## 3. Install on the JUZIPi SD PRO

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

The factory updater can't take the full firmware, so this is a two-step
install for now. You need internet access during step 1.

**Step 1: install Mini Display with its bootstrap**

1. Download `SDP-HomeAssistant-MiniDisplay-Bootstrap-<version>.bin` from the
   [Mini Display releases](https://github.com/piotrkochan/homeassistant-minidisplay/releases).
   Don't rename it: the factory updater only accepts files whose name starts
   with `SDP`.
2. Open the clock's own web page (its address is in the clock's network
   settings or your router's device list) and upload the file in its firmware
   update section.
3. The clock shows an installer network name and password. Join it with your
   phone and open `http://192.168.4.1`.
4. Choose your Wi-Fi, enter its password, set an interface password (keep it:
   it becomes your CAW clock password), then press **Install**. Wait until
   the Mini Display firmware has started.

**Step 2:** follow [route B](#b-from-home-assistant-mini-display-firmware).

> 🔜 **Coming: the CAW bootstrap.** One file uploaded through the factory
> updater that downloads and checks CAW Clock itself, so steps 1 and 2 become
> one. It needs public release hosting, which isn't set up yet.

## First-time setup

After a first install, or after **Factory reset**:

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

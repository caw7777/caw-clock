# CAW Clock Firmware

Custom firmware that turns a **JUZIPi SD PRO** desk clock (ESP8266 ESP-12F,
4 MB flash, 240 × 240 ST7789 display) into a live **CAW (crow with knife)**
price display. It runs on its own: no Home Assistant, server or account.

![CAW screen](docs/caw-screen.png)

## What it shows

- CAW price with a subscript zero count (`$0.0₈4785`), 1H and 24H change
- a 24-hour price chart, filled in from history right after the first start
- liquidity, 24H volume and market cap
- green or red by the 24-hour move; the ticker ring turns grey when the data
  is stale
- the time (your time zone) and Wi-Fi state

It rotates through the main CAW pool on **Cronos, Solana, Base and
Robinhood**, each with its chain logo. You choose the chains and the time on
each in the settings page. Market cap is always the overall CAW figure.

Prices come from DexScreener, with GeckoTerminal as a backup and for chart
history, over HTTPS with certificate checks.

## Install

**Step-by-step guide for every route, setup and troubleshooting:
[INSTALL.md](INSTALL.md).** In short:

Download `caw-clock-<version>.bin` from the
[latest release](https://github.com/caw7777/caw-clock/releases/latest)
and check it against `SHA256SUMS.txt`.

| Clock is running | How to install |
|---|---|
| CAW Clock firmware | Settings page → **Firmware** → choose the `.bin` → **Install firmware** |
| [Home Assistant Mini Display](https://github.com/piotrkochan/homeassistant-minidisplay) firmware | Its **Firmware** page → upload the `.bin` |
| The original (stock) firmware | The stock updater can't take a full firmware. First install the Mini Display firmware with its bootstrap ([instructions](https://github.com/piotrkochan/homeassistant-minidisplay#readme)), then upload the CAW `.bin` from its Firmware page. A CAW bootstrap is planned. |

Don't unplug the clock while it restarts after an install.

## First-time setup

1. The clock shows **Set up CAW Clock** with a network name
   (`CAW-Clock-XXXXXX`) and a key.
2. Join that network with the key. Your phone may say "no internet": stay
   connected. Open `http://192.168.4.1`.
3. Pick your Wi-Fi from the list (2.4 GHz only), enter its password, choose a
   clock password (8–32 characters) and check the time zone (preselected from
   your phone).
4. The clock joins your Wi-Fi and shows its settings-page address for a few
   seconds. Sign in there as **admin** with the clock password.

If it can't join, it says why ("network not found", "check the Wi-Fi
password") and reopens the setup network after 2 minutes.

## Settings page

`http://<clock address>/` (sign in as **admin**):

Four tabs:

- **Status**: price and last update for each chain; the clock's address, signal and memory
- **Display**: brightness, night mode, chains, time on each chain, time zone (63 zones)
- **Memes**: rotation, and the meme library (add, hide, delete)
- **System**: Wi-Fi, clock password, firmware install, restart, factory reset
- `http://<clock address>/api/status`: everything as JSON, including memory
  and the last restart reason

## Giving the clock away

Use **Factory reset** on the settings page. It erases the Wi-Fi details,
password and all settings; the clock starts in setup mode. Nothing personal
is built into the firmware (the default time zone is UTC).

## Safety and security

- Price data: HTTPS with certificate validation (GTS and ISRG roots).
- Settings page: HTTP on your network with Digest sign-in, so the password is
  never sent in clear; page content isn't encrypted.
- Firmware uploads need the clock password (or the setup network, whose key is
  only shown on the clock's screen). Images are not signed.
- **Safe mode:** after three quick restarts in a row the clock stops fetching
  prices and keeps the settings page and firmware upload working.
- No automatic rollback: if a bad image ever stops the clock from starting,
  recovery needs a USB-serial flash.

## Building

The firmware source is in `caw-working-source.zip` (PlatformIO,
espressif8266@4.2.1). CI builds it on every push:

| Workflow | Builds |
|---|---|
| Build CAW standalone | the CAW-only firmware (`sdpro_caw_standalone`) + native tests |
| Release CAW Clock firmware | the release assets, when a release is published |
| Build CAW + Home Assistant | CAW + HA firmware (`sdpro_caw_ha`), on hold, manual runs |

Asset scripts (run by hand, outputs committed): `caw_chain_icons.py`
(chain logos), `caw_memes.py` (bundled pictures), `caw_timezones.py` (time
zones from the IANA database).

Changes: [CHANGELOG.md](CHANGELOG.md).

Based on [Home Assistant Mini Display](https://github.com/piotrkochan/homeassistant-minidisplay);
third-party notices are in `THIRD_PARTY.md` inside the source archive. Chain
logos are trademarks of their owners and only identify which chain is shown.

# Changelog

## v0.8.0

- **Update notices:** the clock checks for a new version once a day. When one
  is out, a small green dot appears next to the Wi-Fi icon and the settings
  page says which version is available. Install it from the **System** tab
  as before; nothing is installed without you.
- **ESP32-C2 board (SDC2):** faster price updates. The clock reuses its secure
  connection to each price and burn source instead of starting a new one each
  time (about 35 ms instead of 1.3 s per connection).
- **ESP32-C2 board (SDC2):** a new built-in animated meme, CAW-verse.

## v0.7.1

- **Check for updates → Install works again on the ESP8266 board (SDP).**
  Installing from GitHub stopped with "Not enough memory to connect to
  release-assets.githubusercontent.com" on 0.7.0. Update mode now leaves more
  memory free for the download. Clocks on 0.7.0 with the ESP8266 board need
  this version installed once by hand (System → Install a file with
  `caw-clock-0.7.1.bin`); later updates work from the settings page.
- Clocks on a test version (such as `0.7.0-rc2`) now see the release of the
  same number as newer.

## v0.7.0

- **New model: the SD PRO with an ESP32-C2 board ("SDC2").** Newer SD PRO
  clocks have an ESP32-C2 instead of the ESP8266. CAW Clock now runs on them
  with the same screens, settings page, memes, alerts and updates. Install it
  from the clock's factory update page with
  `SDC2-CAW-Clock-Installer-<version>.bin`: the installer joins the Wi-Fi the
  clock already uses, downloads CAW Clock from this release, checks it and
  starts it ([INSTALL.md](INSTALL.md#4-install-on-the-sd-pro-with-an-esp32-c2-board-sdc2)).
- **Direct burns on Cronos:** CAW sent straight to the dead wallet now gets a
  burn alert too: the amount, who burned it and the total burned. The Great
  Furnace's burns have their own picture. Bridge burns show as before.
  The Status tab's last burns link each burn's transaction on the chain's
  explorer.
- **Install a file** (System tab) checks that a firmware file is for this
  clock's board before installing anything, and refuses the other board's
  file ("This file is not firmware for this clock"). Check for updates checks
  the same.
- **One-file install from the stock firmware** on the ESP8266 board too:
  `SDP-CAW-Clock-Installer-<version>.bin` through the clock's own update page
  sets up Wi-Fi, the clock password and the time zone, then downloads, checks
  and installs CAW Clock (no Mini Display step).
- Prices always show four digits after the zero count (`$0.0₈4370`, was
  `$0.0₈437` when a source sent fewer), so every chain's price has the same
  width.

## v0.6.0

- **Supply screen** (Display tab): where CAW is, like the
  CAW site's supply panel: a ring of each chain's share, the circulating
  supply, total burned, holders, and a row per chain with its share and
  holders. Shown once each round of chains.
- **BSC** as a fifth price chain (PancakeSwap CAW/WBNB): choose it under
  Chains on the Display tab.
- New clocks show a new meme with each chain (it was every minute). Clocks
  already set up keep their choice (Memes tab).
- A chain with no trades in the last hour shows its 1H change as +0.0%
  instead of "N/A".
- Burn alert: the route shows each chain's logo ("[logo] bsc to [logo]
  solana"), now for BSC, Polygon and Arbitrum too.
- **Recovery mode** for a forgotten clock password: plug the clock in 3 times
  in a row, each time for under 10 seconds. It opens its setup network for
  15 minutes with the key on screen, where a new password can be set.
  Settings and memes are kept.
- Check for updates → Install: more memory for the download, and when
  memory is too broken up the clock says so and tries again instead of
  restarting. An update tried before a new release's files are attached says
  to try again in a few minutes.
- About 4 KB more free memory during every price, burn and holder check:
  the clock loads only the certificates its servers use (the two larger
  ones only if a server ever needs them). After long running times this
  keeps clear of the memory limit at which a check is skipped.
- Security: a clock without a password answers only at its own address or
  network name, so a malicious website can't reach its settings through a
  domain pointed at the clock (DNS rebinding). Clocks with a password were
  not affected.

## v0.5.0

- **Burn alert:** when someone bridges CAW, the 0.5% the bridge burns takes
  over the screen for 20 seconds: the amount burned, the route (e.g. "bsc to
  solana"), the amount bridged and the total burned, counted the same way as
  the CAW Discord's burn bot. The clock reads the bridge's contracts on
  Cronos, BSC, Base, Polygon, Arbitrum and Robinhood every few minutes;
  bridges from Solana count too (their burn happens when they arrive). At
  most one alert every 10 minutes; burns in between are added up ("3
  bridges").
  - Display tab: **Burn alert** on/off (on by default) and **Preview the burn
    alert**.
  - Status tab: **Burns**: total burned, the last burns, each chain's last
    check.
  - `/api/status`: `burns`.
- Memes tab: **Show all** and **Hide all** for the built-in and uploaded memes
  (to keep just one: Hide all, then Show that one).
- Setup screen: the Wi-Fi problem ("check the Wi-Fi password") fits on the
  screen.
- Pages shown just before a restart (Wi-Fi saved during setup, factory reset,
  update installed) now arrive complete.
- Installer for clocks on the factory firmware: status messages use a second
  line when needed instead of being cut off.

## v0.4.0

- Update from the settings page: **System → Check for updates**, then
  **Install**. Downloads are checked against the release's SHA-256 before they
  are installed. The clock checks only when you press the button.
- Built-in backup during updates: the clock keeps a copy of the current
  version while an update installs and returns to it automatically if the new
  version doesn't start correctly.
- Price alert: when a chain moves more than a set amount in an hour (default
  10%; Display tab), the clock shows that chain and the price flashes green
  or red for 5 minutes.
- 12- or 24-hour clock (Display tab).
- Smoother, more efficient performance: more free memory, a firmware about
  40 KB smaller (quicker updates) and lighter settings pages; cleaner progress
  display while updating.
- Dependable over long running times; a chain on the backup price source
  returns to DexScreener by itself; room for longer custom time zones.
- Setup network key made with the Wi-Fi radio on, for full randomness.
- `/api/status`: `freeContStackBoot`, `stackLowWork`, `rollbackCopy`, per-chain
  `alert`, `not_listed` when DexScreener doesn't list a pool; `tlsStackMax`
  now reports the TLS stack's real peak.

## v0.3.0

- Settings page in tabs (Status, Display, Memes, System); the meme library is
  inside the Memes tab. "Picture" is now "meme" in the page; royal purple
  replaces yellow.
- Fixed random restarts (and a restart loop into safe mode): the price fetch
  used too much of the main stack, which Wi-Fi interrupts share.
- Steadier price fetches: TLS sessions are reused, so most fetches skip the
  full handshake; crash reports now also cover watchdog resets and name the
  firmware build; `connectMs`, `resumed` per chain and `freeContStack` in `/api/status`.
- Night mode: dim or switch off the screen between two times of day.
- Settings requests from other websites are refused (cross-site protection);
  stronger setup-network key; warning when no clock password is set.
- Offline: failed price fetches back off and no longer freeze the settings
  page; chains refresh spread out instead of all at once.
- Failed firmware uploads restore time sync; partial settings requests can't
  blank the screen; fewer flash writes.
- Larger 56 px top-left picture with a meme library: built-in memes in the
  firmware plus memes uploaded from the settings page (Memes tab:
  add, hide/show, delete; resized in your browser; kept across firmware
  updates; up to 200), rotating on a timer or with each chain.
- Animated memes: upload a GIF on the Memes tab (up to 30 frames, resized in
  your browser) and it plays in the picture slot.
- 16 CAW memes built in, two of them animated (hide any you don't want from the same page).
- `lightSensorRaw`, `nightMode`, `passwordSet`, `primaryResult`, `memes` in
  `/api/status`.

## v0.2.0

CAW-only firmware: the clock fetches prices itself. The Home Assistant
dashboard engine from v0.1.0 is gone; that is what freed the memory the
HTTPS price fetch needs (v0.1.0 showed "--" for this reason).

- Fixed CAW screen drawn directly: subscript price, 1H / 24H, 24-hour chart,
  liquidity / volume / market cap, ticker; red on down days, grey when stale.
- Price data from DexScreener (4 KB TLS buffers), GeckoTerminal as backup,
  certificate-validated HTTPS.
- Chains: Cronos, Solana, Base and Robinhood with their logos, rotating; chains
  and time per chain set in the settings page.
- 24-hour chart filled in from GeckoTerminal hourly history at start-up,
  gaps (hours without trades) carried forward; kept across restarts.
- First-time setup: WPA2 setup network with the key on screen, Wi-Fi network
  list, clear join errors, settings address shown after connecting.
- Settings page with Digest sign-in: markets, brightness, chains, picture
  rotation (ready for bundled memes), 63 time zones, Wi-Fi, password,
  firmware install, restart, factory reset; `/api/status` JSON.
- Default time zone UTC; the setup page preselects the phone's zone.
- Safety: price fetches skipped when memory is short (no crash), safe mode
  after three quick restarts, last restart reason in the status.
- Interrupted firmware uploads are discarded and the screen recovers.

Upgrading from v0.1.0: Wi-Fi and the clock password are kept; set the time
zone again on the settings page.

## v0.1.0 (pre-release)

CAW screen inside the Home Assistant Mini Display firmware with a CAW / Home
Assistant mode selector. Fit the 1,044,464-byte OTA limit; on the device the
price fetch ran out of memory.

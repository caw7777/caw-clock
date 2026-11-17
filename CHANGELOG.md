# Changelog

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

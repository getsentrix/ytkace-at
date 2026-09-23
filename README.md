# AltStore Source for YTKACE

Custom AltStore / SideStore repository for [YTKACE](https://github.com/itzzace/ytkace), an open-source YouTube enhancer and downloader for iOS with SponsorBlock, background playback, player controls, and interface customization.

<p align="center">
  <img src="logo.png" alt="YTKACE Logo" width="120" style="border-radius: 24px;" />
</p>

---

## 🔗 Repository URL

Copy and paste this URL into your sideloading app:

```text
https://getsentrix.github.io/ytkace-at/apps.json
```

*(Raw fallback URL: `https://raw.githubusercontent.com/getsentrix/ytkace-at/main/apps.json`)*

---

## 📲 How to Add

### SideStore / AltStore
1. Open **SideStore** or **AltStore**.
2. Navigate to the **Sources** tab.
3. Tap the **+** (Add) button in the top corner.
4. Paste the URL: `https://getsentrix.github.io/ytkace-at/apps.json`
5. Tap **Add**. YTKACE will now appear in your browse/source list with automatic update notifications!

### LiveContainer
1. Open **LiveContainer**.
2. Go to the **Sources** tab.
3. Tap **+** and paste: `https://getsentrix.github.io/ytkace-at/apps.json`
*(Or tap "Add to LiveContainer" directly from the [web page](https://getsentrix.github.io/ytkace-at/))*

### Feather / ESign / Scarlet
1. Open the app and go to **Sources / Repositories**.
2. Tap **Add Source**.
3. Paste `https://getsentrix.github.io/ytkace-at/apps.json` and confirm.

---

## ⚙️ How It Works

This repository is designed to never stop working and automatically stay up to date:
- A GitHub Actions workflow runs every 12 hours (and can be triggered manually).
- It queries the official upstream repository ([itzzace/ytkace](https://github.com/itzzace/ytkace)) via GitHub API for new releases.
- When a new version with iOS `.ipa` builds is published, it updates `apps.json` with the new version number, download links (including iOS 17+ and iOS 16 fallback), release notes, and file sizes.

---

## 📜 Credits

- [itzzace/ytkace](https://github.com/itzzace/ytkace) - Developer of YTKACE
- [AltStore](https://altstore.io/) - Sideloading platform & source specifications

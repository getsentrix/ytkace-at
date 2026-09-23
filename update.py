import json
import os
import urllib.request
from datetime import datetime, timezone

REPO = "itzzace/ytkace"
SOURCE_NAME = "YTKACE Community Source"
SOURCE_ID = "com.community.ytkace-source"
APP_NAME = "YTKACE"
BUNDLE_ID = "com.google.ios.youtube"
DEVELOPER_NAME = "itzzace"
SUBTITLE = "Open-source YouTube enhancer and downloader"
LOCALIZED_DESCRIPTION = (
    "YTKACE is a free, open-source YouTube enhancer and downloader for iOS "
    "with SponsorBlock, background playback, player controls, and interface customization."
)
ICON_URL = "https://raw.githubusercontent.com/getsentrix/ytkace-at/main/logo.png"
TINT_COLOR = "BF0013"

url = f"https://api.github.com/repos/{REPO}/releases/latest"
headers = {"User-Agent": "AltStore-Updater"}
github_token = os.environ.get("GITHUB_TOKEN")
if github_token:
    headers["Authorization"] = f"token {github_token}"

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

version = data.get("tag_name", "").lstrip("v")
release_date = data.get("published_at", datetime.now(timezone.utc).isoformat())
body = data.get("body", "Latest release of YTKACE.")

# Filter IPA assets
ipa_assets = [
    a for a in data.get("assets", [])
    if a.get("name", "").lower().endswith(".ipa")
]

if not ipa_assets:
    raise SystemExit("No IPA assets found in latest release.")

# Identify primary (iOS 17+) and legacy (iOS 16) assets
primary_ipa = next(
    (a for a in ipa_assets if "ios16" not in a["name"].lower()),
    ipa_assets[0],
)
legacy_ipa = next(
    (a for a in ipa_assets if "ios16" in a["name"].lower()),
    None,
)

apps = [
    {
        "name": APP_NAME,
        "bundleIdentifier": BUNDLE_ID,
        "developerName": DEVELOPER_NAME,
        "subtitle": SUBTITLE,
        "localizedDescription": LOCALIZED_DESCRIPTION,
        "iconURL": ICON_URL,
        "tintColor": TINT_COLOR,
        "version": version,
        "versionDate": release_date,
        "versionDescription": body,
        "downloadURL": primary_ipa["browser_download_url"],
        "size": primary_ipa["size"],
    }
]

if legacy_ipa:
    apps.append(
        {
            "name": f"{APP_NAME} (iOS 16 Legacy)",
            "bundleIdentifier": f"{BUNDLE_ID}.legacy",
            "developerName": DEVELOPER_NAME,
            "subtitle": "YTKACE YouTube client compatible with iOS 16",
            "localizedDescription": (
                "Legacy build of YTKACE with SponsorBlock, background playback, "
                "and downloader compatible with iOS 16."
            ),
            "iconURL": ICON_URL,
            "tintColor": TINT_COLOR,
            "version": version,
            "versionDate": release_date,
            "versionDescription": body,
            "downloadURL": legacy_ipa["browser_download_url"],
            "size": legacy_ipa["size"],
        }
    )

source_data = {
    "name": SOURCE_NAME,
    "identifier": SOURCE_ID,
    "apps": apps,
}

with open("apps.json", "w", encoding="utf-8") as f:
    json.dump(source_data, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Successfully generated apps.json for {APP_NAME} v{version} with {len(apps)} app build(s).")

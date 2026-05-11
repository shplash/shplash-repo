import json
import sys
from datetime import date

tag = sys.argv[1]
release_name = sys.argv[2]
release_notes = sys.argv[3]

version = tag.lstrip("v")

download_url = f"https://github.com/shplash/IPAID/releases/download/{tag}/IPAID.ipa"

with open("apps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for app in data["apps"]:
    if app.get("bundleIdentifier") == "com.shplash.ipaid":
        app["version"] = version
        app["versionDate"] = str(date.today())
        app["downloadURL"] = download_url
        app["localizedDescription"] = app.get(
            "localizedDescription",
            "Lightweight IPA editor for iOS 15+"
        )

        app["versions"] = [
            {
                "version": version,
                "date": str(date.today()),
                "localizedDescription": release_notes,
                "downloadURL": download_url,
                "size": 0
            }
        ]

with open("apps.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")

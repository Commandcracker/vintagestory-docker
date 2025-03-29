import requests
import json

def main():
    URL = "https://mods.vintagestory.at/api/gameversions"
    response = requests.get(URL)

    if response.status_code != 200:
        exit(f"Failed to fetch data from: \"{URL}\"")
    
    data = response.json()

    game_versions = data.get("gameversions", [])

    stable_versions = []
    unstable_versions = []

    for version in game_versions:
        version_name = version["name"]
        if "rc" not in version_name and "pre" not in version_name:
            stable_versions.append(version_name)
        else:
            unstable_versions.append(version_name)

    latest_stable = stable_versions[0] if stable_versions else exit("No stable version found")
    latest_unstable = unstable_versions[0] if unstable_versions else exit("No unstable version found")

    versions = [
        {"VS_VERSION": latest_stable[1:], "VS_TYPE": "stable"},
        {"VS_VERSION": latest_unstable[1:], "VS_TYPE": "unstable"}
    ]

    print(json.dumps({"include": versions}))

if __name__ == "__main__":
    main()

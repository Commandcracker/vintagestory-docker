import requests

# Make a GET request to the API endpoint
url = "https://mods.vintagestory.at/api/gameversions"
response = requests.get(url)

# Ensure the response is successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    game_versions = data.get('gameversions', [])

    # Define lists to store stable and unstable versions
    stable_versions = []
    unstable_versions = []

    # Loop through all the versions and classify them
    for version in game_versions:
        version_name = version['name']
        if "rc" not in version_name and "pre" not in version_name:  # Stable versions
            stable_versions.append(version_name)
        else:  # Unstable versions (Release Candidate or Pre-release)
            unstable_versions.append(version_name)

    # Display the latest stable and unstable versions
    latest_stable = stable_versions[0] if stable_versions else None
    latest_unstable = unstable_versions[0] if unstable_versions else None

    print(f"Latest Stable Version: {latest_stable}")
    print(f"Latest Unstable Version: {latest_unstable}")

else:
    print("Failed to fetch data from the API")

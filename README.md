# vintagestory-docker

Docker image for [Vintage Story](https://www.vintagestory.at/)

🚧 **Work in process!**

## Features

### Security

- Update [System.Drawing.Common] to 8.0.5 see [CVE-2021-24112] \
    [Shipped with Vintage Story]

- Update [System.Formats.Asn1] to 4.7.2 see [CVE-2024-38095] \
    [Shipped with .NET 7]

- Update [System.Text.Json] to 8.0.5 see [CVE-2024-30105] \
    [Shipped with Vintage Story and .NET 7] \
    (Vintage Story already ships with System.Text.Json 8.0.5 so only the global .NET 7 dependency is updated!)

- Use latest OS version \
    (Most Vintage Story docker images are using outdated OS version becasue they are based on mcr.microsoft.com/dotnet/runtime:7.0)

- Run ther server as none root user \
    (Most Vintage Story docker images are alredy doing this becasue they base on mcr.microsoft.com/dotnet/runtime:7.0)

- TODO: Use Distroles base image

### Image Size

- Remove unnecessary files
- Minify json files
- Use small base image
- TODO: Use Distroles base image

[System.Drawing.Common]: https://www.nuget.org/packages/system.drawing.common#readme-body-tab
[CVE-2021-24112]: https://security.snyk.io/vuln/SNYK-DOTNET-SYSTEMDRAWINGCOMMON-3063427
[System.Formats.Asn1]: https://www.nuget.org/packages/System.Formats.Asn1#readme-body-tab
[CVE-2024-38095]: https://security.snyk.io/vuln/SNYK-DOTNET-SYSTEMFORMATSASN1-7443633
[System.Text.Json]: https://www.nuget.org/packages/System.Text.Json#readme-body-tab
[CVE-2024-30105]: https://security.snyk.io/vuln/SNYK-DOTNET-SYSTEMTEXTJSON-7433719

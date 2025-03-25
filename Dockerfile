FROM alpine:latest AS build

ARG vs_type=stable \
    vs_os=linux-x64 \
    vs_version=1.20.6

WORKDIR /opt/vintagestory

ADD "https://cdn.vintagestory.at/gamefiles/${vs_type}/vs_server_${vs_os}_${vs_version}.tar.gz" vs_server.tar.gz

# TODO: Fix tar extraction
# TODO: Minimize files
RUN set -euxo pipefail; \
    tar --strip-components 1 -xzf vs_server.tar.gz; \
    rm credits.txt server.sh VintagestoryServer.deps.json; \
    rm vs_server.tar.gz

# TODO: Create own update image
FROM mcr.microsoft.com/dotnet/runtime:7.0-jammy-chiseled AS runtime

WORKDIR /opt/vintagestory

COPY --from=build /opt/vintagestory /opt/vintagestory

EXPOSE 42420/tcp 42420/udp

ENTRYPOINT ["dotnet", "VintagestoryServer.dll", "--dataPath", "/srv/vintagestory"]

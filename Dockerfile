FROM mcr.microsoft.com/dotnet/runtime:7.0 AS runtime

ARG vs_type=stable \
    vs_os=linux-x64 \
    vs_version=1.20.6

WORKDIR /opt/vintagestory

ADD "https://cdn.vintagestory.at/gamefiles/${vs_type}/vs_server_${vs_os}_${vs_version}.tar.gz" vs_server.tar.gz

RUN set -eux; \
    tar -xvzf vs_server.tar.gz; \
    rm vs_server.tar.gz

EXPOSE 42420/tcp

CMD ["dotnet", "VintagestoryServer.dll", "--dataPath", "/srv/vintagestory"]

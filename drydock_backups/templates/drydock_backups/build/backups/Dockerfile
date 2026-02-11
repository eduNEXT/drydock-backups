FROM debian:bookworm-slim AS base
ENV DEBIAN_FRONTEND=noninteractive

RUN <<EOF
    set -eux
    apt-get update
    apt-get install -y \
        curl \
        gnupg2 \
    ;
    curl -o /usr/share/keyrings/mysql.asc \
        -fsSL 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xbca43417c3b485dd128ec6d4b7b3b788a8d3785c'
    curl -o /usr/share/keyrings/mongodb.asc \
        -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc
EOF

COPY <<mysql.sources <<mongodb.sources /etc/apt/sources.list.d/
Types: deb
URIs: http://repo.mysql.com/apt/debian/
Suites: bookworm
Components: mysql-8.4-lts
Signed-By: /usr/share/keyrings/mysql.asc
mysql.sources
Types: deb
URIs: http://repo.mongodb.org/apt/debian/
Suites: bookworm/mongodb-org/7.0
Components: main
Signed-By: /usr/share/keyrings/mongodb.asc
mongodb.sources

RUN <<EOF
  apt update
  apt upgrade
  apt install -y mysql-client mongodb-org-tools awscli
EOF

RUN <<EOF
    set -eux
    AZCOPY_TMP="$(mktemp -d)"
    curl -sL https://aka.ms/downloadazcopy-v10-linux |  \
        tar -xz -C "${AZCOPY_TMP}"
    mv ${AZCOPY_TMP}/azcopy_linux_amd64*/azcopy "/usr/local/bin"
    rm -rf $AZCOPY_TMP
EOF

RUN useradd -m backupuser
RUN echo "backupuser ALL=(ALL) NOPASSWD: /usr/bin/mysql, /usr/bin/mongodump" >> /etc/sudoers

USER backupuser

WORKDIR /data

COPY --chown=backupuser:backupuser --chmod=744 docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]

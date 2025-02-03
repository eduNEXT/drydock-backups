FROM debian:bookworm-slim AS base

RUN <<EOF
    set -eux
    apt-get update
    apt-get install -y \
        curl \
        gnupg2
    rm -rf /var/lib/apt/lists/*
EOF

RUN <<EOF
    set -eux
    # pub   rsa4096 2023-10-23 [SC] [expires: 2025-10-22]
    #       BCA4 3417 C3B4 85DD 128E  C6D4 B7B3 B788 A8D3 785C
    # uid           [ unknown] MySQL Release Engineering <mysql-build@oss.oracle.com>
    # sub   rsa4096 2023-10-23 [E] [expires: 2025-10-22]
    key='BCA4 3417 C3B4 85DD 128E C6D4 B7B3 B788 A8D3 785C'
    export GNUPGHOME="$(mktemp -d)"
    gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"
    mkdir -p /etc/apt/keyrings; \
    gpg --batch --export "$key" > /etc/apt/keyrings/mysql.gpg
    gpgconf --kill all
    rm -rf "$GNUPGHOME"
    echo 'deb [ signed-by=/etc/apt/keyrings/mysql.gpg ] http://repo.mysql.com/apt/debian/ bookworm mysql-8.4-lts' > /etc/apt/sources.list.d/mysql.list
EOF

RUN <<EOF
    set -eux
    curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
    echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list
EOF

RUN <<EOF
    set -eux
    apt-get update
    apt-get install -y \
        awscli \
        mongodb-org \
        mysql-community-client
    rm -rf /var/lib/apt/lists/*
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

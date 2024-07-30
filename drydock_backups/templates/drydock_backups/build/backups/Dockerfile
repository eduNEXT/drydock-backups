FROM debian:bookworm-slim AS base

RUN apt-get update && apt-get install -y wget gnupg2 curl && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
# pub   rsa4096 2023-10-23 [SC] [expires: 2025-10-22]
#       BCA4 3417 C3B4 85DD 128E  C6D4 B7B3 B788 A8D3 785C
# uid           [ unknown] MySQL Release Engineering <mysql-build@oss.oracle.com>
# sub   rsa4096 2023-10-23 [E] [expires: 2025-10-22]
	key='BCA4 3417 C3B4 85DD 128E C6D4 B7B3 B788 A8D3 785C'; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
	mkdir -p /etc/apt/keyrings; \
	gpg --batch --export "$key" > /etc/apt/keyrings/mysql.gpg; \
	gpgconf --kill all; \
	rm -rf "$GNUPGHOME"

RUN echo 'deb [ signed-by=/etc/apt/keyrings/mysql.gpg ] http://repo.mysql.com/apt/debian/ bookworm mysql-8.4-lts' > /etc/apt/sources.list.d/mysql.list

# The following command is required to prevent the following error:
# GPG error: http://repo.mysql.com/apt/debian buster InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B7B3B788A8D3785C
# The solution was found here: https://askubuntu.com/questions/1497140/how-to-fix-apt-update-after-to-upgrade-the-mysql-list-file#comment2623210_1497141
# RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B7B3B788A8D3785C && rm /etc/apt/keyrings/mysql.gpg && gpg  --output /etc/apt/keyrings/mysql.gpg --export B7B3B788A8D3785C

RUN curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

RUN echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list

RUN apt-get update && apt-get install -y \
    mysql-community-client \
    mongodb-org \
    awscli \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/azcopy.tar.gz https://aka.ms/downloadazcopy-v10-linux \
    && tar -xvf /tmp/azcopy.tar.gz -C /tmp \
    && cp /tmp/azcopy_linux_amd64*/azcopy /usr/bin/ \
    && chmod +x /usr/bin/azcopy \
    && rm -rf /tmp/azcopy*

RUN useradd -m backupuser
RUN echo "backupuser ALL=(ALL) NOPASSWD: /usr/bin/mysql, /usr/bin/mongodump" >> /etc/sudoers

USER backupuser

WORKDIR /data

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]

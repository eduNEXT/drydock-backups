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

RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | gpg -o /usr/share/keyrings/mongodb-server-4.4.gpg --dearmor

RUN echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

RUN apt-get update && apt-get install -y \
    mysql-community-client=8.4.2-1debian12 \
    mongodb-database-tools \
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

# CHANGELOG


## v19.0.0 (2025-02-03)

### Continuous Integration

- Add docker build and push workflow ([#8](https://github.com/eduNEXT/drydock-backups/pull/8),
  [`09d9527`](https://github.com/eduNEXT/drydock-backups/commit/09d95274f52d0f27b1cd7903df6af8774438fab7))

### Features

- Sumac release ([#11](https://github.com/eduNEXT/drydock-backups/pull/11),
  [`34994a3`](https://github.com/eduNEXT/drydock-backups/commit/34994a36657bf45a19dcf45fcc613839fc9f0027))


## v18.1.1 (2024-08-06)

### Bug Fixes

- Add if not exists to backup user creation
  ([`2dbb437`](https://github.com/eduNEXT/drydock-backups/commit/2dbb437105e64e077e02338ac93c6a3b4950ac85))


## v18.1.0 (2024-08-05)

### Features

- Add minio expiration policy, custom storage class
  ([#10](https://github.com/eduNEXT/drydock-backups/pull/10),
  [`7bff3fc`](https://github.com/eduNEXT/drydock-backups/commit/7bff3fcea4b1661f6c0de315608fa5eca05bd30b))


## v18.0.0 (2024-07-30)

### Features

- Add pyproject, python-semantic-release and rename folder
  ([#7](https://github.com/eduNEXT/drydock-backups/pull/7),
  [`fdb2896`](https://github.com/eduNEXT/drydock-backups/commit/fdb28966631f8d63fbdb7b974680c497a93a78c4))

- Upgrade to redwood ([#6](https://github.com/eduNEXT/drydock-backups/pull/6),
  [`9452b0f`](https://github.com/eduNEXT/drydock-backups/commit/9452b0f4326aaa460f32bf7ea4f8c2d6e9d919db))


## v1.2.0 (2024-01-17)

### Features

- Allow to install drydock backups as non-editable and add mysql backups init job
  ([#5](https://github.com/eduNEXT/drydock-backups/pull/5),
  [`730ac77`](https://github.com/eduNEXT/drydock-backups/commit/730ac7723526caf4c7ec7581c7071658ba768bcf))

* fix: allow to install drydock backups as non-editable

* tmp: try with tabs

* feat: add backups user creation at init

* fix: user correct version

* fix: remove indent

* fix: address suggestions

---------

Co-authored-by: henrrypg <henrry.pulgarin@edunext.co>


## v1.1.0 (2024-01-16)

### Features

- Add the mongo backup user to the initialization job
  ([#4](https://github.com/eduNEXT/drydock-backups/pull/4),
  [`28400a1`](https://github.com/eduNEXT/drydock-backups/commit/28400a11ef7c127d8dea4e466216553666249f8d))


## v1.0.0 (2024-01-04)

### Features

- Split plugin in separated repository
  ([`d12a55e`](https://github.com/eduNEXT/drydock-backups/commit/d12a55edfda68d09f1743b2f56ba3a73572183e7))

BREAKING CHANGE: version v1.0.0

### BREAKING CHANGES

- Version v1.0.0


## v0.4.1 (2023-12-22)

### Bug Fixes

- Remove pat from release workflow ([#55](https://github.com/eduNEXT/drydock-backups/pull/55),
  [`0494096`](https://github.com/eduNEXT/drydock-backups/commit/04940966d28820ed8b43122f274689e8d5e2cb57))


## v0.4.0 (2023-12-22)

### Features

- Support docker operations for image in drydock backups
  ([#53](https://github.com/eduNEXT/drydock-backups/pull/53),
  [`0e3ee1b`](https://github.com/eduNEXT/drydock-backups/commit/0e3ee1baf61b42d2188712dfae38ab4d2a58bfde))

* feat: support docker operations for image in drydock backups

* fix: update image variable in defaults and jobs template

* fix: update .gitignore

* fix: using BACKUP_VARIABLE

* fix: update readme

* fix: update gitignore for /build/ folder


## v0.3.0 (2023-12-22)

### Features

- Mongo DB backups proper implementation ([#52](https://github.com/eduNEXT/drydock-backups/pull/52),
  [`913fd51`](https://github.com/eduNEXT/drydock-backups/commit/913fd51af38d8e69d3b72d4d1138d68650df08d2))

* fix: update variables names and jumplines

* fix: duplicate key

* fix: include custom_storage_endpoint in aws block

* fix: newlines control

* fix: args for command

* fix: environment azure variables

* fix: include bucket path in all options

* fix: delete databases variable

* fix: update .sh

* fix: update default shipyard-utils image


## v0.2.0 (2023-12-22)

### Bug Fixes

- Removing inexistent folder from github actions release flow
  ([`15a2b83`](https://github.com/eduNEXT/drydock-backups/commit/15a2b832edb8054d9b233c35d86a86a509d23279))

- Using Github PAT to bypass main branch protection
  ([`bb66752`](https://github.com/eduNEXT/drydock-backups/commit/bb66752191a47fa852a42ff84be3461a7a8ccc7d))

### Features

- Drydock 1.0 ([#47](https://github.com/eduNEXT/drydock-backups/pull/47),
  [`55b63eb`](https://github.com/eduNEXT/drydock-backups/commit/55b63eb64a233926177c933a8f686648443d0398))

- Use azcopy for databases backups ([#51](https://github.com/eduNEXT/drydock-backups/pull/51),
  [`bead0d6`](https://github.com/eduNEXT/drydock-backups/commit/bead0d6d303eeb73d47af376ea292736c77c7787))

* feat: install azcopy

* feat: add new variables and conditionals for storage services

* fix: include custom storage endpoint inside s3 conditional

* feat: add variables and azcopy command

* fix: update variable names

* fix: storage system names

* fix: default s3 value

* fix: error in readme

* update backup system variable name

* fix: azure-blob conditional


## v0.1.2 (2023-12-22)

### Bug Fixes

- Drydock fails in older versions to tutor palm
  ([#43](https://github.com/eduNEXT/drydock-backups/pull/43),
  [`86b4765`](https://github.com/eduNEXT/drydock-backups/commit/86b47650af6e1136ebd172384ce829de2efcb6a1))

- Set the correct path to use pvc volume ([#45](https://github.com/eduNEXT/drydock-backups/pull/45),
  [`abc6ad1`](https://github.com/eduNEXT/drydock-backups/commit/abc6ad18f82eb953c144adfdce34dd4bca4844ba))


## v0.1.1 (2023-12-22)

### Bug Fixes

- Mysqldump faild due mysql version ([#41](https://github.com/eduNEXT/drydock-backups/pull/41),
  [`804b216`](https://github.com/eduNEXT/drydock-backups/commit/804b2162dbd438ed590e02035cdff2707890dc53))


## v0.1.0 (2023-12-22)

### Features

- Add backups plugin ([#39](https://github.com/eduNEXT/drydock-backups/pull/39),
  [`46ec572`](https://github.com/eduNEXT/drydock-backups/commit/46ec572ab001bafb0cbf5619d5faac3992182207))

Co-authored-by: Cristhian Garcia <cristhian.garcia@edunext.co>

Co-authored-by: Jhony Avella <jhony.avella@edunext.co>

- Connecting with tutor
  ([`630aeef`](https://github.com/eduNEXT/drydock-backups/commit/630aeef72b8c386879d76d0e07c20ffac71aa2cb))

- Stating the purpose and context for this project
  ([`353a946`](https://github.com/eduNEXT/drydock-backups/commit/353a946973ac42940fce4e720207473c17701fde))

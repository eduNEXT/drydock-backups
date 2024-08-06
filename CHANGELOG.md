# CHANGELOG

## v18.1.1 (2024-08-06)

### Fix

* fix: add if not exists to backup user creation ([`2dbb437`](https://github.com/eduNEXT/drydock-backups/commit/2dbb437105e64e077e02338ac93c6a3b4950ac85))

## v18.1.0 (2024-08-05)

### Chore

* chore(release): preparing 18.1.0 ([`7bb8816`](https://github.com/eduNEXT/drydock-backups/commit/7bb8816fde751681459739e9410ac874f3a9370f))

### Feature

* feat: add minio expiration policy, custom storage class (#10) ([`7bff3fc`](https://github.com/eduNEXT/drydock-backups/commit/7bff3fcea4b1661f6c0de315608fa5eca05bd30b))

## v18.0.0 (2024-07-30)

### Chore

* chore(release): preparing 18.0.0 ([`38a63ce`](https://github.com/eduNEXT/drydock-backups/commit/38a63ce61621249f524027e6c631a8e208780394))

### Feature

* feat: upgrade to redwood (#6) ([`9452b0f`](https://github.com/eduNEXT/drydock-backups/commit/9452b0f4326aaa460f32bf7ea4f8c2d6e9d919db))

* feat: add pyproject, python-semantic-release and rename folder (#7) ([`fdb2896`](https://github.com/eduNEXT/drydock-backups/commit/fdb28966631f8d63fbdb7b974680c497a93a78c4))

## v1.2.0 (2024-01-17)

### Chore

* chore(release): preparing 1.2.0 ([`e2d23e7`](https://github.com/eduNEXT/drydock-backups/commit/e2d23e73de5cfb025668c84c2e3ddd19934d72e9))

### Feature

* feat: allow to install drydock backups as non-editable and add mysql backups init job (#5)

* fix: allow to install drydock backups as non-editable

* tmp: try with tabs

* feat: add backups user creation at init

* fix: user correct version

* fix: remove indent

* fix: address suggestions

---------

Co-authored-by: henrrypg &lt;henrry.pulgarin@edunext.co&gt; ([`730ac77`](https://github.com/eduNEXT/drydock-backups/commit/730ac7723526caf4c7ec7581c7071658ba768bcf))

## v1.1.0 (2024-01-16)

### Chore

* chore(release): preparing 1.1.0 ([`33ddb4b`](https://github.com/eduNEXT/drydock-backups/commit/33ddb4bc9c9f2c0818b9099e15df39666ece09a8))

### Feature

* feat: add the mongo backup user to the initialization job (#4) ([`28400a1`](https://github.com/eduNEXT/drydock-backups/commit/28400a11ef7c127d8dea4e466216553666249f8d))

## v1.0.0 (2024-01-04)

### Breaking

* feat: split plugin in separated repository

BREAKING CHANGE: version v1.0.0 ([`d12a55e`](https://github.com/eduNEXT/drydock-backups/commit/d12a55edfda68d09f1743b2f56ba3a73572183e7))

### Chore

* chore(release): preparing 1.0.0 ([`4ef8a1a`](https://github.com/eduNEXT/drydock-backups/commit/4ef8a1a99e8f96452fb288bd318588b00a2287b5))

## v0.4.1 (2023-12-22)

### Fix

* fix: remove pat from release workflow (#55) ([`0494096`](https://github.com/eduNEXT/drydock-backups/commit/04940966d28820ed8b43122f274689e8d5e2cb57))

### Unknown

* doc: update instructions for build docker image (#54) ([`1864cc7`](https://github.com/eduNEXT/drydock-backups/commit/1864cc7cfcabb7e4a1dc872cb1d56b17307ef2ba))

## v0.4.0 (2023-12-22)

### Feature

* feat: support docker operations for image in drydock backups (#53)

* feat: support docker operations for image in drydock backups

* fix: update image variable in defaults and jobs template

* fix: update .gitignore

* fix: using BACKUP_VARIABLE

* fix: update readme

* fix: update gitignore for /build/ folder ([`0e3ee1b`](https://github.com/eduNEXT/drydock-backups/commit/0e3ee1baf61b42d2188712dfae38ab4d2a58bfde))

## v0.3.0 (2023-12-22)

### Feature

* feat: Mongo DB backups proper implementation (#52)

* fix: update variables names and jumplines

* fix: duplicate key

* fix: include custom_storage_endpoint in aws block

* fix: newlines control

* fix: args for command

* fix: environment azure variables

* fix: include bucket path in all options

* fix: delete databases variable

* fix: update .sh

* fix: update default shipyard-utils image ([`913fd51`](https://github.com/eduNEXT/drydock-backups/commit/913fd51af38d8e69d3b72d4d1138d68650df08d2))

## v0.2.0 (2023-12-22)

### Feature

* feat: use azcopy for databases backups (#51)

* feat: install azcopy

* feat: add new variables and conditionals for storage services

* fix: include custom storage endpoint inside s3 conditional

* feat: add variables and azcopy command

* fix: update variable names

* fix: storage system names

* fix: default s3 value

* fix: default s3 value

* fix: error in readme

* update backup system variable name

* fix: azure-blob conditional ([`bead0d6`](https://github.com/eduNEXT/drydock-backups/commit/bead0d6d303eeb73d47af376ea292736c77c7787))

* feat: drydock 1.0 (#47) ([`55b63eb`](https://github.com/eduNEXT/drydock-backups/commit/55b63eb64a233926177c933a8f686648443d0398))

### Fix

* fix: using Github PAT to bypass main branch protection ([`bb66752`](https://github.com/eduNEXT/drydock-backups/commit/bb66752191a47fa852a42ff84be3461a7a8ccc7d))

* fix: removing inexistent folder from github actions release flow ([`15a2b83`](https://github.com/eduNEXT/drydock-backups/commit/15a2b832edb8054d9b233c35d86a86a509d23279))

## v0.1.2 (2023-12-22)

### Fix

* fix: set the correct path to use pvc volume (#45) ([`abc6ad1`](https://github.com/eduNEXT/drydock-backups/commit/abc6ad18f82eb953c144adfdce34dd4bca4844ba))

* fix: drydock fails in older versions to tutor palm (#43) ([`86b4765`](https://github.com/eduNEXT/drydock-backups/commit/86b47650af6e1136ebd172384ce829de2efcb6a1))

## v0.1.1 (2023-12-22)

### Fix

* fix: mysqldump faild due mysql version (#41) ([`804b216`](https://github.com/eduNEXT/drydock-backups/commit/804b2162dbd438ed590e02035cdff2707890dc53))

## v0.1.0 (2023-12-22)

### Feature

* feat: add backups plugin (#39)

Co-authored-by: Cristhian Garcia &lt;cristhian.garcia@edunext.co&gt;
Co-authored-by: Jhony Avella &lt;jhony.avella@edunext.co&gt; ([`46ec572`](https://github.com/eduNEXT/drydock-backups/commit/46ec572ab001bafb0cbf5619d5faac3992182207))

* feat: connecting with tutor ([`630aeef`](https://github.com/eduNEXT/drydock-backups/commit/630aeef72b8c386879d76d0e07c20ffac71aa2cb))

* feat: stating the purpose and context for this project ([`353a946`](https://github.com/eduNEXT/drydock-backups/commit/353a946973ac42940fce4e720207473c17701fde))

### Unknown

* Merge pull request #33 from eduNEXT/catalog-info

chore: adding backstage catalog and owners ([`f927a8e`](https://github.com/eduNEXT/drydock-backups/commit/f927a8e3f34a7d284e717e956b0ea58c5bc18af6))

* Initial commit ([`a4f7c99`](https://github.com/eduNEXT/drydock-backups/commit/a4f7c9906a165383a16b7bd252ede2abccbabdf9))

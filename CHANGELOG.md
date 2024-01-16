# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/eduNEXT/drydock-backups/compare/v1.1.0...HEAD)

Please do not update the unreleased notes.

## [v0.4.0](https://github.com/eduNEXT/drydock-backups/compare/v0.3.0...v0.4.0)

### [0.4.0](https://github.com/eduNEXT/drydock-backups/compare/v0.3.0...v0.4.0)

#### Features

- support docker operations for image in drydock backups (#53)

## [v0.3.0](https://github.com/eduNEXT/drydock-backups/compare/v0.2.0...v0.3.0)

### [0.3.0](https://github.com/eduNEXT/drydock-backups/compare/v0.2.0...v0.3.0)

#### Features

- Mongo DB backups proper implementation (#52)

## [v0.2.0](https://github.com/eduNEXT/drydock-backups/compare/v0.1.2...v0.2.0)

### [0.2.0](https://github.com/eduNEXT/drydock-backups/compare/v0.1.2...v0.2.0)

#### Features

- use azcopy for databases backups (#51)

#### Bug Fixes

- using Github PAT to bypass main branch protection
- removing inexistent folder from github actions release flow

## [v0.1.2](https://github.com/eduNEXT/drydock-backups/compare/v0.1.1...v0.1.2)

### [0.1.2](https://github.com/eduNEXT/drydock-backups/compare/v0.1.1...v0.1.2)

#### Bug fixes

- set the correct path to use pvc volume (#45)

## [v0.1.1](https://github.com/eduNEXT/drydock-backups/compare/v0.1.0...v0.1.1)

### [0.1.1](https://github.com/eduNEXT/drydock-backups/compare/v0.1.0...v0.1.1)

#### Bug fixes

- mysqldump faild due mysql version

#### Code Refactoring

- Move forum pod to wave 4, HPA to wave 5.
- Remove MySQL jobs when MySQL running outside the cluster.

## [v0.1.0](https://github.com/eduNEXT/drydock-backups/commits/v0.1.0)

### [0.1.0](https://github.com/eduNEXT/drydock-backups/commits/v0.1.0)

#### Features

- Add backups plugin

## [v1.1.0](https://github.com/eduNEXT/drydock-backups/compare/v1.0.0...v1.1.0) - 2024-01-16

### [1.1.0](https://github.com/eduNEXT/drydock-backups/compare/v1.0.0...v1.1.0) (2024-01-16)

#### Features

- add the mongo backup user to the initialization job ([#4](https://github.com/eduNEXT/drydock-backups/issues/4)) ([28400a1](https://github.com/eduNEXT/drydock-backups/commit/28400a11ef7c127d8dea4e466216553666249f8d))

#### Build Systems

- use correct readme file in setup.py ([#3](https://github.com/eduNEXT/drydock-backups/issues/3)) ([dcd284e](https://github.com/eduNEXT/drydock-backups/commit/dcd284e196823cb72b9ea09999da493e36b8df73))

## [v1.0.0](https://github.com/eduNEXT/drydock-backups/compare/v0.4.1...v1.0.0) - 2024-01-04

### [1.0.0](https://github.com/eduNEXT/drydock-backups/compare/v0.4.1...v1.0.0) (2024-01-04)

#### ⚠ BREAKING CHANGES

- version v1.0.0

#### Features

- split plugin in separated repository ([d12a55e](https://github.com/eduNEXT/drydock-backups/commit/d12a55edfda68d09f1743b2f56ba3a73572183e7))

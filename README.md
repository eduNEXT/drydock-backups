# Drydock-backups

> **NOTE:**: This plugin was extracted from [drydock](https://github.com/eduNEXT/drydock), versions older than v1.0.0 are created to store historical information but shouldn't be used.

This is a tutor plugin used to easily store backups of mysql and mongodb databases through k8s cronjobs. It backups the databases and stores them in a bucket.

This plugin assumes that the destination bucket is already created and that the credentials to access it are already configured (Works with S3 and Minio buckets indicating his endpoint url through `BACKUP_CUSTOM_STORAGE_ENDPOINT`).

> **Warning:**: This plugin is only usable when [drydock](https://github.com/eduNEXT/drydock) is installed.

## Installation and activation


It is included with the Drydock installation, so there's no need to install it separately.

You can enable it adding `drydock-backups` to the `plugins` section of the `config.yml` file.

## Configuration variables


- **BACKUP_DOCKER_IMAGE**: The image used to run the cronjob. (default: `ednxops/shipyard-utils:v{{BACKUP_VERSION}}`)
- **BACKUP_CRON_SCHEDULE**: Cron schedule to run the backup. (default: `0 2 * * *`)
- **BACKUP_STORAGE_SERVICE**: Storage service to use. (default: `aws-s3`) (options: `aws-s3`, `azure-blob`)
- **BACKUP_AWS_ACCESS_KEY**: AWS access key to access the bucket or minIO user.
- **BACKUP_AWS_SECRET_KEY**: AWS secret key to access the bucket or minIO password.
- **BACKUP_BUCKET_NAME**: Name of the bucket where the backups will be stored.
- **BACKUP_BUCKET_PATH**: Path inside the bucket where the backups will be stored.
- **BACKUP_CUSTOM_STORAGE_ENDPOINT**: Custom endpoint to access the bucket. (default: `None`)
- **BACKUP_AZURE_CONTAINER_NAME**: Name of the container where the backups will be stored.
- **BACKUP_AZURE_ACCOUNT_NAME**: Name of the account to access the container.
- **BACKUP_AZURE_CONTAINER_SAS_TOKEN**: SAS token to access the container.
- **BACKUP_K8S_USE_EPHEMERAL_VOLUMES**: Use ephemeral volumes to set up the cronjob. (default: `False`)
- **BACKUP_K8S_EPHEMERAL_VOLUME_SIZE**: Size of the ephemeral volume. (default: `8Gi`)
- **BACKUP_K8S_EPHEMERAL_VOLUME_STORAGE_CLASS**: Custom StorageClass name for ephemeral volumes creation. (default: `None`)
- **BACKUP_MINIO_EXPIRATION_DAYS**: Number of days to setup the lifecycle policy when Minio is enabled. (default: `0`)
- **BACKUP_MYSQL_USERNAME**: Username to access the mysql database. (default: `{{ MYSQL_ROOT_USERNAME }}`)
- **BACKUP_MYSQL_PASSWORD**: Password to access the mysql database. (default: `{{ MYSQL_ROOT_PASSWORD }}`)
- **BACKUP_MONGO_PASSWORD**: Password to access the mongodb database. (default: `{{ MONGODB_PASSWORD }}`)
- **BACKUP_MONGO_USERNAME**: Username to access the mongodb database. (default: `{{ MONGODB_USERNAME }}`)

You can set ups these variables in the `config.yml` file.

## Docker image


The docker image used to run the cronjob is `ednxops/shipyard-utils:v1.0.0` and it is available in [DockerHub](https://hub.docker.com/r/ednxops/shipyard-utils).

When `drydock-backups` is installed in your manifests, you can build the Docker image using the following commands:

.. code-block:: bash

    tutor images build backups
    tutor images push backups

## Utilities


In the path `/utils` we have some utilities to help us managing the backups.

- **s3_backups_expiration**: This terraform script is to add to S3 bucket lifecycle rules. Is used to delete the backups that are older than a certain number of days.

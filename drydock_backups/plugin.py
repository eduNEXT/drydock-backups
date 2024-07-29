from glob import glob
import os
import os.path

import importlib_resources

from tutor import hooks as tutor_hooks

from .__about__ import __version__

config = {
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "ednxops/drydock-backups:v{{BACKUP_VERSION}}",
        "CRON_SCHEDULE": '0 2 * * *',
        "STORAGE_SERVICE": "aws-s3",
        "AWS_ACCESS_KEY": "",
        "AWS_SECRET_KEY": "",
        "BUCKET_NAME": "",
        "BUCKET_PATH": "backups",
        "AZURE_CONTAINER_NAME": "",
        "AZURE_CONTAINER_SAS_TOKEN": "",
        "AZURE_ACCOUNT_NAME": "",
        "CUSTOM_STORAGE_ENDPOINT": None,
        "K8S_USE_EPHEMERAL_VOLUMES": False,
        "K8S_EPHEMERAL_VOLUME_SIZE": "8Gi",
        "MYSQL_USERNAME": '{{ MYSQL_ROOT_USERNAME }}',
        "MYSQL_PASSWORD": '{{ MYSQL_ROOT_PASSWORD }}',
        "MONGO_PASSWORD": '{{ MONGODB_PASSWORD }}',
        "MONGO_USERNAME": '{{ MONGODB_USERNAME }}',
    },
    # Add here settings that don't have a reasonable default for all users. For
    # instance: passwords, secret keys, etc.
    "unique": {
        # "SECRET_KEY": "\{\{ 24|random_string \}\}",
    },
    # Danger zone! Add here values to override settings from Tutor core or other plugins.
    "overrides": {
    },
}

tutor_hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"BACKUP_{key}", value)
        for key, value in config["defaults"].items()
    ]
)

tutor_hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"BACKUP_{key}", value)
        for key, value in config["unique"].items()
    ]
)

tutor_hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))

tutor_hooks.Filters.IMAGES_BUILD.add_items([
    (
        "backups",
        ("plugins", "drydock_backups", "build", "backups"),
        "{{BACKUP_DOCKER_IMAGE}}",
        (),
    )
])

tutor_hooks.Filters.IMAGES_PULL.add_items([
    (
        "backups",
        "{{BACKUP_DOCKER_IMAGE}}",
    )
])

tutor_hooks.Filters.IMAGES_PUSH.add_items([
    (
        "backups",
        "{{BACKUP_DOCKER_IMAGE}}",
    )
])

# Plugin templates
tutor_hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("drydock_backups") / "templates")
)

tutor_hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(    [
        ("drydock_backups/build", "plugins"),
        ("drydock_backups/apps", "plugins"),
    ],
)
# Load all patches from the "patches" folder
for path in glob(str(importlib_resources.files("drydock_backups") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# # init script
with open(
    str(importlib_resources.files("drydock_backups") / "templates" / "drydock_backups" / "task" / "mongodb" / "init"),
    encoding="utf-8",
) as fi:


    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mongodb-backup", fi.read()), priority=tutor_hooks.priorities.HIGH)
with open(
    str(importlib_resources.files("drydock_backups") / "templates" / "drydock_backups" / "task" / "mysql" / "init"),
    encoding="utf-8",
) as fi:
    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item(("mysql", fi.read()), priority=tutor_hooks.priorities.HIGH)

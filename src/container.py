"""Containers module."""

from dependency_injector import containers, providers

from repos.users import StaticUserRepo

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["routers.users"])

    config = providers.Configuration(yaml_files=["config.yml"])

    user_repo = providers.Singleton(
        StaticUserRepo
    )

    
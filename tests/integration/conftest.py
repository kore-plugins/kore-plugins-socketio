import pytest

from kore import config_factory, container_factory


@pytest.fixture(scope='session')
def socketio_config():
    return {
        'async_mode': 'aiohttp',
    }


@pytest.fixture(scope='session')
def config(socketio_config):
    return config_factory.create('dict', **{'socketio': socketio_config})


@pytest.fixture
def container(config):
    initial = {
        'config': config,
    }
    return container_factory.create(**initial)


@pytest.fixture
def async_server(container):
    return container('kore.components.socketio.async_server')

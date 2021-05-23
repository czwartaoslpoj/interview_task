import pytest

from standardizing_api.transformer import Transformer


@pytest.fixture(scope='module')
def transformer():
    transformer = Transformer()
    return transformer


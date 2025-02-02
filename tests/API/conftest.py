import pytest
from src.lib.helpers.api_helper import create_account


@pytest.fixture
def new_account():
    def _create(currency="EUR"):
        response = create_account(currency)
        return response

    return _create

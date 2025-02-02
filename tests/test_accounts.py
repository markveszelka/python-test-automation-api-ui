from helpers.api_helper import get_account


def test_create_account(new_account):
    currency = "EUR"
    response = new_account(currency)

    assert response.status_code == 201
    assert response.json()["currency"] == currency


def test_get_account(new_account):
    account = new_account("EUR")
    account_id = account.json()["id"]
    response = get_account(account_id)

    assert response.status_code == 200
    assert response.json()["id"] == f"{account_id}"


def test_get_nonexistent_account():
    non_existent_account_id = 9999
    response = get_account(non_existent_account_id)

    assert response.status_code == 404

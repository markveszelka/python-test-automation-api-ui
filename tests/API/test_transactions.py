from src.lib.helpers.api_helper import *


def test_deposit_money(new_account):
    # ARRANGE: Create an account
    account = new_account()
    account_id, initial_balance = account.json()["id"], account.json()["balance"]

    # ACT: Deposit money
    added_amount = 100
    response = deposit_money(account_id, "EUR", added_amount)

    # ASSERT
    assert response.status_code == 200
    assert response.json()["balance"] == initial_balance + added_amount


def test_withdraw_success(new_account):
    # ARRANGE
    account = new_account()
    account_id, initial_balance = account.json()["id"], account.json()["balance"]

    deposit_amount = 250
    deposit_money(account_id, "EUR", deposit_amount)

    # ACT: Withdraw money
    withdraw_amount = 200
    response = withdraw_money(account_id, "EUR", withdraw_amount)

    # ASSERT
    assert response.status_code == 200
    assert response.json()["balance"] == initial_balance + deposit_amount - withdraw_amount


def test_withdraw_insufficient_balance(new_account):
    # ARRANGE
    account = new_account()
    account_id = account.json()["id"]

    # ACT: Withdraw too much
    withdraw_amount = 1000
    response = withdraw_money(account_id, "EUR", withdraw_amount)

    # ASSERT
    expected_message = f"Account {account_id} has insufficient balance"
    assert response.status_code == 400
    assert expected_message in response.json()["message"]


def test_transfer_success(new_account):
    # ARRANGE
    account_1 = new_account()
    account_2 = new_account()
    account_1_id, account_2_id = account_1.json()["id"], account_2.json()["id"]

    deposit_money(account_1_id, "EUR", 500)

    # ACT: Transfer money
    transfer_amount = 200
    response = transfer_money(account_1_id, account_2_id, "EUR", transfer_amount)

    # ASSERT
    assert response.status_code == 200
    assert response.json()["id"] == account_1_id
    assert response.json()["balance"] == 500 - transfer_amount

    # Verify recipient balance
    account_2_response = get_account(account_2_id)
    assert account_2_response.status_code == 200
    assert account_2_response.json()["balance"] == transfer_amount


def test_transfer_insufficient_funds(new_account):
    # ARRANGE
    account_1 = new_account()
    account_2 = new_account()
    account_1_id, account_2_id = account_1.json()["id"], account_2.json()["id"]

    deposit_money(account_1_id, "EUR", 500)

    # ACT: Attempt to transfer too much
    transfer_amount = 1000
    response = transfer_money(account_1_id, account_2_id, "EUR", transfer_amount)

    # ASSERT
    assert response.status_code == 400
    assert "insufficient balance" in response.json()["message"]


def test_transfer_nonexistent_account(new_account):
    # ARRANGE
    account_1 = new_account()
    account_1_id = account_1.json()["id"]
    invalid_account_id = 999999999

    deposit_money(account_1_id, "EUR", 500)

    # ACT: Transfer to non-existent account
    response = transfer_money(account_1_id, invalid_account_id, "EUR", 200)

    # ASSERT
    assert response.status_code == 404

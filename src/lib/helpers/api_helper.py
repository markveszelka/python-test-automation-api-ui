import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("API_BASE_URL")


def create_account(currency):
    response = requests.post(f"{BASE_URL}/account", json={"currency": currency})
    return response


def deposit_money(account_id, currency, amount):
    response = requests.post(f"{BASE_URL}/transaction/deposit", json={
        "accountId": account_id,
        "currency": currency,
        "amount": amount,
    })
    return response


def withdraw_money(account_id, currency, amount):
    response = requests.post(f"{BASE_URL}/transaction/withdraw", json={
        "accountId": account_id,
        "currency": currency,
        "amount": amount,
    })
    return response


def transfer_money(debit_account_id, credit_account_id, currency, amount):
    response = requests.post(f"{BASE_URL}/transaction/transfer", json={
        "debitAccountId": debit_account_id,
        "creditAccountId": credit_account_id,
        "currency": currency,
        "amount": amount,
    })
    return response


def get_account(account_id):
    response = requests.get(f"{BASE_URL}/account/{account_id}")
    return response

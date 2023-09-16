from scripts.helpful_scripts import get_account
from brownie import TestToken
from web3 import Web3
def deploy_token():
    account = get_account()
    token = TestToken.deploy(Web3.toWei(5000, "ether"), {"from": account})
    print(token.name())

def main():
    deploy_token()
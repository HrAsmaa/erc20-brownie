from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
FORK_BLOCKCHAIN_ENV = ["mainnet-fork-dev"]
def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV or network.show_active() in FORK_BLOCKCHAIN_ENV:
        return accounts [0]
    return accounts.add(config["wallets"]["from_key"])
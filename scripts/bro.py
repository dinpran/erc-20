from brownie import accounts, config, EasyToken

initial_supply = 1000000000000000000000
token_name = "DINPRAN"
token_symbol = "DP"


def main():
    account = accounts[0]
    erc20 = EasyToken.deploy(initial_supply, {"from": account})

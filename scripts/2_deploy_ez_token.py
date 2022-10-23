from brownie import accounts, config, EasyToken

initial_supply = 1000000000000000000000
token_name = "DINPRAN"
token_symbol = "DP"


def main():
    account = accounts[0]
    erc20 = EasyToken.deploy(initial_supply, {"from": account})


# 0x6068f83ee53f3b8e2ad2202d5fec3ddc44ad3826c7cd69342c1da27f65605171

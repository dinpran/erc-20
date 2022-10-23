pragma solidity ^0.6.0;

import "OpenZeppelin/openzeppelin-contracts@3.4.0/contracts/token/ERC20/ERC20.sol";

contract EasyToken is ERC20 {
    constructor() public ERC20("DINPRAN", "DP") {
        _mint(msg.sender, 1000000000000000000000000);
    }
}

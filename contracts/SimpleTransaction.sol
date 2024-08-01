// contracts/SimpleTransaction.sol
pragma solidity ^0.8.0;

contract SimpleTransaction {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function sendINR(address payable recipient) public payable {
        require(msg.value > 0, "Amount must be greater than zero");
        recipient.transfer(msg.value);
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}

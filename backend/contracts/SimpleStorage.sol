// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    string public lastHash;
    event HashStored(string hash);

    function storeHash(string memory h) public {
        lastHash = h;
        emit HashStored(h);
    }

    function getLastHash() public view returns (string memory) {
        return lastHash;
    }
}

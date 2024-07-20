// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract DonationContract is ChainlinkClient {
    address public platformWallet;
    uint public constant TAX_RATE = 15;
    bytes32 private jobId;
    uint256 private fee;
    address private oracle;

    mapping(bytes32 => address) public projectWallets;

    constructor(address _platformWallet, address _oracle, bytes32 _jobId, uint256 _fee, address _linkToken) {
        platformWallet = _platformWallet;
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
        setChainlinkToken(_linkToken);
    }

    function requestProjectWalletValidation(string memory projectId) public returns (bytes32 requestId) {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        request.add("projectId", projectId);
        requestId = sendChainlinkRequestTo(oracle, request, fee);
        projectWallets[requestId] = msg.sender; // Associar a carteira do solicitante com o requestId
        return requestId;
    }

    function fulfill(bytes32 _requestId, bool _isValid) public recordChainlinkFulfillment(_requestId) {
        require(_isValid, "Invalid project wallet");
        // Continuação da lógica após validação
    }
}

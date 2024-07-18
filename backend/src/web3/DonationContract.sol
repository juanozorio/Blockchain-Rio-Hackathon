// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DonationContract {
    address public platformWallet; // Carteira da plataforma para receber a taxa
    uint public constant TAX_RATE = 15; // Taxa de 15%

    constructor(address _platformWallet) {
        platformWallet = _platformWallet;
    }

    function donate(address payable projectWallet, bool isSocialProject) public payable {
        uint amount = msg.value; // Valor enviado na transação

        if (isSocialProject) {
            // Transferir o valor total para a carteira do projeto
            projectWallet.transfer(amount);
        } else {
            // Calcular a taxa
            uint taxAmount = (amount * TAX_RATE) / 100;
            uint donationAmount = amount - taxAmount;

            // Transferir a taxa para a carteira da plataforma
            payable(platformWallet).transfer(taxAmount);
            // Transferir o valor restante para a carteira do projeto
            projectWallet.transfer(donationAmount);
        }
    }

    // Função para receber doações diretas
    receive() external payable {}
}

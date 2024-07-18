import Web3 from 'web3';

export async function getMetaMaskProvider() {
    if (!window.ethereum) throw new Error(`No MetaMask found!`);

    const web3 = new Web3(window.ethereum);

    const accounts = await web3.eth.requestAccounts();
    console.log(accounts)

    if (!accounts || !accounts.length) throw new Error(`Permission required!`)

    return web3;
}

export async function getBalance(address) {
    const web3 = await getMetaMaskProvider();

    return balance;
}

export async function transfer(from, to, quantity) {
    const web3 = await getMetaMaskProvider();
    const value = web3.utils.toWei(quantity, "ether");

    const nonce = await web3.eth.getTransactionCount(from, "latest");
    const transaction = {
        from,
        to,
        value,
        gas: 21000,

    };

    const tx = await web3.eth.sendTransaction(transaction);

    return tx.transactionHash;
}

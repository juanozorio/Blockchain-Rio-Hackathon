"use client";

import { Carousel } from 'react-responsive-carousel';
import { useState, useEffect } from 'react';
import ethers, { BrowserProvider, Contract, parseEther, Wallet, formatEther } from 'ethers';
import { getMetaMaskProvider, getBalance, transfer } from '../../common/MetaMaskService';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import styles from './CarouselBanner.module.css';
import contractData from '../../app/resources/DonationContract.json';

const CarouselBanner = () => {
  const [address, setAddress] = useState("");
  const [to, setTo] = useState("");
  const [quantity, setQuantity] = useState("");
  const [message, setMessage] = useState("");
  const [platformBalance, setPlatformBalance] = useState(0.0);

  const PROJECT_WALLET = "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2" // endereço da carteira que recebe a doação, pode ser trocado por um select que vai pegar os endereços do banco e exibir uma lista de endereços para o usuário que vai doar poder escolher para quem doará
  const DONATION_AMOUNT = "0.1" // valor da doação
  const PLATFORM_WALLET = "0x04EdbfB6D677605aAD0962e62eBBE0d95c84101e" //ENDEREÇO DA PLATAFORMA 0x0b82B600b20868093420BB7623e2D35Fb67D9844
  
  function getBalanceClick() {
    getBalance(PROJECT_WALLET)
      .then(balance => setMessage(balance))
      .catch(err => setMessage(err.message))
  }

  function transferClick() {
    console.log("TransferClick")
    transfer(address, //de - from
      to, //para - to
      quantity) //valor - quantity
      .then(tx => setMessage(tx))
      .catch(err => setMessage(err.message))
  }

  async function donate() {
    setMessage("Enviando transação...");
    try {
      const provider = new BrowserProvider(window.ethereum);
      const signer = await provider.getSigner();
        
        const contract = new Contract(
            contractData.address,
            contractData.abi,
            signer
        );

        //Executar a transação de doação.
        const tx = await contract.donate(
            PROJECT_WALLET, // pra quem vai a doação
            false, // se é social ou não
            {
                value: parseEther(DONATION_AMOUNT),
                gasLimit: 3000000
            }
        );

        setMessage("Transação enviada, aguardando confirmação...");
        await tx.wait();
        setMessage("Doação concluída com sucesso!");

        console.log(tx);
    } catch (error) {
        console.error("Falha ao fazer a doação:", error);
        setMessage(`Erro na doação, verifique o console.`);
    }
}


  const getPlatformBalance = async () => {
    const provider = new BrowserProvider(window.ethereum);
    let balance = (await getBalance(PLATFORM_WALLET)).toString();
    balance = formatEther(balance);
    balance = parseFloat(balance).toFixed(2);
    setPlatformBalance(balance);
  }

  useEffect(() => {
    getPlatformBalance();
  }, []);

  return (
    <Carousel
      showThumbs={false}
      showStatus={false}
      infiniteLoop
      useKeyboardArrows
      autoPlay
      interval={5000}
      showArrows={false}
      className={styles.carousel}
    >
      <div className={styles.slide}>
        <img src="/images/plataforma-logo.jpg" alt="Slide 1" className={styles.image} />
        <div className={styles.textContainer}>
          {/* SALDO DA PLATAFORMA, TÁ MOCKADO NO CENTRO DA TELA PORQUE EU SOU CEGO (leia gritando) */}
          <h1 style={{position: 'absolute', top: '50%', left: '50%', color: 'white'}}>
            {
              platformBalance
            }
          </h1>
          <h2>Plataforma Impact</h2>
          <br />
          <p>Preparamos jovens de alto potencial em comunidades de baixa renda para uma carreira em tecnologia.</p>

          Wallet: <input className={styles.input} type='text' value={address} onChange={(evt) => setAddress(evt.target.value)} />
          <br />
          To: <input className={styles.input} type='text' value={to} onChange={(evt) => setTo(evt.target.value)} />
          <br />
          Quantity: <input className={styles.input} type='text' value={quantity} onChange={(evt) => setQuantity(evt.target.value)} />
          <button className={styles.btn} onClick={() => donate()}>Doe</button>
          <br />
          <button className={styles.btn} onClick={getBalanceClick}>Get Balance</button>
          <br />
          <button className={styles.btn} onClick={transferClick}>Transfer</button>
          <br />
          <span style={{color: 'white'}}>
            {message}
          </span>
        </div>
      </div>
      {/* <div className={styles.slide}>
        <img src="/images/image2.jpg" alt="Slide 2" className={styles.image} />
        <div className={styles.textContainer}>
          <h2>Nebula Web3</h2>
          <br />
          <p>Uma organização sem fins lucrativos comprometida em criar um espaço de tecnologia/NFT mais inclusivo e acessível.</p>
          <br />
          <button className={styles.btn} onClick={() => getMetaMaskProvider()}>Doe</button>

        </div>
      </div> */}
    </Carousel>
  );
};

export default CarouselBanner;
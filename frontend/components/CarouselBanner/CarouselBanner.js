import { Carousel } from 'react-responsive-carousel';
import { useState } from 'react';
import { getMetaMaskProvider, getBalance } from '../../src/app/MetaMaskService';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import styles from './CarouselBanner.module.css';


const CarouselBanner = () => {
  const [message, setMessage] = useState("");
  
  function getBalanceClick(){
    getBalance("0x0b82B600b20868093420BB7623e2D35Fb67D9844")
    .then(balance => setMessage(balance))
  }


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
        <img src="/images/image1.jpg" alt="Slide 1" className={styles.image} />
        <div className={styles.textContainer}>
          <h2>Plataforma Impact</h2>
          <br />
          <p>Preparamos jovens de alto potencial em comunidades de baixa renda para uma carreira em tecnologia.</p>
          <button className={styles.btn} onClick={() => getMetaMaskProvider()}>Doe</button>
          <br />
          <button className={styles.btn} onClick={getBalanceClick}>Get Balance</button>
          <br />
          {message}
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

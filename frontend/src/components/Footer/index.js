import styles from "./Footer.module.css";
import Image from "next/image";

function Footer() {
  return (
    <footer className={styles.rodape}>
     <div>
        <p className={styles.subtitulo}>Criação</p>
        <div>
          <Image
            className={styles.img__block}
            src="/images/block-logo.png"
            alt="logo Bloc.kria"
            width={150}
            height={200}
          />
        </div>  
      </div>
      <div>
        <p className={styles.subtitulo}>Apoio</p>
        <div className={styles.img__container}>
          <Image
            src="/images/its-logo.png"
            alt="logo Its Cripto"
            width={150}
            height={200}
          />
          <Image
            src="/images/nebula-logo.png"
            alt="logo Nebula"
            width={150}
            height={200}
          />
        </div>  
      </div>
    </footer>
  );
}

export default Footer;

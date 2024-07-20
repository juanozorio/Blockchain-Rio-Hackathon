import styles from "./Footer.module.css";
import Image from "next/image";

function Footer() {
  return (
    <footer className={styles.rodape}>
      <p className={styles.subtitulo}>Criação</p>
      <Image
        className={styles.img__criacao}
        src="/images/block-logo.png"
        alt="logo Bloc.kria"
        width={150}
        height={200}
      />
      <p className={styles.subtitulo}>Apoio</p>
      <div className={styles.img__container}>
        <div className={styles.img__apoio}>
          <Image
            src="/images/its-logo.png"
            alt="logo Bloc.kria"
            width={150}
            height={200}
          />
        </div>
        <div className={styles.img__apoio}>
          <Image
            src="/images/nebula-logo.png"
            alt="logo Bloc.kria"
            width={150}
            height={200}
          />
        </div>
      </div>
    </footer>
  );
}

export default Footer;

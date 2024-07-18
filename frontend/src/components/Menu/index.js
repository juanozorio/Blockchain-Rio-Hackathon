import Link from 'next/link';
import styles from './Menu.module.css';
import { FaSearch } from 'react-icons/fa';

const Menu = () => {
  return (
<nav className={styles.nav}>
      <ul className={styles.menu}>
        <li className={styles.menuItem}>
          <a href='./'>BLC.KRIA</a>
        </li>
        <li className={styles.searchBar}>
          <input type="text" placeholder="Pesquisar projetos..." />
          <FaSearch className={styles.searchIcon} />        
        </li>
        <li className={styles.menuItem}>
          <Link href="/IniciarProjeto">Iniciar Projeto </Link>
        </li>
        {/* <li className={styles.menuItem}>
          Services
        </li>
        <li className={styles.menuItem}>
          Contact
        </li> */}
      </ul>
    </nav>
  );
};

export default Menu;

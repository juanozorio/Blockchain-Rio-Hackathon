import Link from 'next/link';
import styles from './Menu.module.css';
import { FaSearch } from 'react-icons/fa';
import Taba from '../Taba/Taba';

const Menu = () => {
  return (
    <nav className="p-6 flex justify-around max-w-full max-h-26 pt-16 ">
      <ul className="align-center flex items-center text-xl text-cyan-50 gap-20 ">
      <Taba/>
        <li className="border-b-2 px-2 pb-2 border-transparent hover:border-cyan-50">
          Home
        </li>
        <li className="border-b-2 px-2 pb-2 border-transparent hover:border-cyan-50">
          About us
        </li>
        <li className="border-b-2 px-2 pb-2 border-transparent hover:border-cyan-50">
          <Link href="/IniciarProjeto">Projects </Link>
        </li>
        <li className="border-b-2 px-2 pb-2 border-transparent hover:border-cyan-50">
          Contact Us
        </li>
      </ul>
    </nav>
  );
};

export default Menu;

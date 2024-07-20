import styles from './Projects.module.css';
import Menu from '@/components/Menu';
import Footer from '@/components/Footer';
import CarouselBanner from '@/components/CarouselBanner/CarouselBanner';

const Projects = () => {
  return (
    <div className={styles.container}>
      <Menu />

      <Footer />
    </div>

  );
};

export default Projects;
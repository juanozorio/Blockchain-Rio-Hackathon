import styles from './Projects.module.css';
import CarouselBanner from '@/components/CarouselBanner/CarouselBanner';

const Projects = () => {
  return (
    <div className={styles.container}>
      <CarouselBanner />
    </div>
  );
};

export default Projects;
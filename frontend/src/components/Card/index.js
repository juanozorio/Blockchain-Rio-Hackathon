import React from "react";
import styles from "./Card.module.css";


const Card = ({ title, description, Image }) => {
  return (
    <div className={styles.card}>
      <div className={styles.overlay}>
        <div className={styles.text}>
          <h2 className={styles.title}>{title}</h2>
          <p className={styles.description}>{description}</p>
        </div>
      </div>
    </div>
  );
};

export default Card;

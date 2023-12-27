import React from 'react'
import { GroupCardProps } from '../../types/types'
import styles from './GroupCard.module.css'
const GroupCard: React.FC<GroupCardProps> = ({ group }) => {
    return (
        <div className={styles.cardContainer}>
            <img
                className={styles.cardImage}
                src={group.image}
                alt={group.name}
            />
            <div className={styles.cardInfo}>
                <span>{group.name}</span>
                <span>{group.description}</span>
            </div>
        </div>
    )
}

export default GroupCard
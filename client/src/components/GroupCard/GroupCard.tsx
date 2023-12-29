import React from 'react'
import { GroupCardProps } from '../../types/types'
import styles from './GroupCard.module.css'
import { Link } from 'react-router-dom'
const GroupCard: React.FC<GroupCardProps> = ({ group }) => {
    return (
        <Link to={`/groups/${group.id}`} >
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
                {window.owner === group.owner
                    ? (
                        <div className={styles.cardActions}>
                            <button className={`${styles.actionButton} ${styles.editGroupButton}`}>Edit</button>
                            <button className={`${styles.actionButton} ${styles.deleteGroupButton}`}>Delete</button>
                        </div>
                    )
                    : (
                        <div className={styles.cardActions}>
                            <button className={`${styles.actionButton} ${styles.joinGroupButton}`}>Request to join</button>
                        </div>

                    )}
            </div>
        </Link>
    )
}

export default GroupCard
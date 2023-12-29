import { GroupCardProps } from '../../types/types'
import styles from './GroupCard.module.css'
import { Link } from 'react-router-dom'

const GroupCard: React.FC<GroupCardProps> = ({ group, currentUserIsOwner, deleteGroup, editGroup, requestJoinGroup }) => {
    const handleEditGroup = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>, id: string | undefined) => {
        e.preventDefault()
        e.stopPropagation()
        if (!id) return
        editGroup(id)
    }

    const handleRequestJoinGroup = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>, id: string | undefined) => {
        e.preventDefault()
        e.stopPropagation()
        if (!id) return
        requestJoinGroup(id)
    }

    const handleDeleteGroup = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>, id: string | undefined) => {
        e.preventDefault()
        e.stopPropagation()
        if (!id) return
        deleteGroup(id)
    }

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
                {currentUserIsOwner
                    ? (
                        <div className={styles.cardActions}>
                            <button
                                className={`${styles.actionButton} ${styles.editGroupButton}`}
                                onClick={e => handleEditGroup(e, group.id)}
                            >
                                Edit
                            </button>
                            <button
                                className={`${styles.actionButton} ${styles.deleteGroupButton}`}
                                onClick={e => handleDeleteGroup(e, group.id)}
                            >
                                Delete
                            </button>
                        </div>
                    )
                    : (
                        <div className={styles.cardActions}>
                            <button
                                className={`${styles.actionButton} ${styles.joinGroupButton}`}
                                onClick={e => handleRequestJoinGroup(e, group.id)}
                            >
                                Request to join
                            </button>
                        </div>

                    )}
            </div>
        </Link>
    )
}

export default GroupCard
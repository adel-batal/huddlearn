import BaseModal from '../BaseModal/BaseModal';
import { CreateGroupModalProps } from '../../../types/modal';
import styles from './CreateGroupModal.module.css';
import { useState } from 'react';
import { Group } from '../../../types/types';

const CreateGroupModal: React.FC<CreateGroupModalProps> = props => {
    const [group, setGroup] = useState<Group | null>(null);
    const {
        contentContainer,
        inputRow,
        modalActions,
        actionButton,
        createButton,
        cancelButton
    } = styles;

    const handleGroupCreateClick = () => {
        if (group?.name && group?.description) {
            props.onCreateGroup(group);
            setGroup(null);
            props.onClose();
        } else {
            alert("Please enter a group name and description");
        }
    };

    const setGroupData = (e: { target: { name: string; value: string; }; }) => {
        setGroup(prevGroup => ({
            ...prevGroup || {},
            [e.target.name]: e.target.value,
            image: "https://picsum.photos/200/300",
        }) as Group | null);
    }
    return (
        <div>
            <BaseModal {...props}>
                <div className={contentContainer}>
                    <h1>Create New Group</h1>
                    <div className={inputRow}>
                        <span>Group name</span>
                        <input
                            name='name'
                            type="text" placeholder="Awesome group"
                            onChange={setGroupData}
                        />
                    </div>
                    <div className={inputRow}>
                        <span>Group description</span>
                        <input
                            name='description'
                            type="text"
                            placeholder="My group description"
                            onChange={setGroupData}
                        />
                    </div>
                    <div className={modalActions}>
                        <button
                            className={`${actionButton} ${createButton}`}
                            onClick={handleGroupCreateClick}
                        >
                            Create Group
                        </button>
                        <button
                            className={`${actionButton} ${cancelButton}`}
                            onClick={props.onClose}
                        >
                            Cancel
                        </button>
                    </div>
                </div>
            </BaseModal>
        </div>
    );
};

export default CreateGroupModal;

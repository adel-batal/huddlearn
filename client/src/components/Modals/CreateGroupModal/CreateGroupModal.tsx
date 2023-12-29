import BaseModal from '../BaseModal/BaseModal';
import { CreateGroupModalProps } from '../../../types/modal';
import modalStyles from '../ModalCommonStyles.module.css';
import styles from './CreateGroupModal.module.css';
import { useEffect, useState } from 'react';
import { Group } from '../../../types/types';

const CreateGroupModal: React.FC<CreateGroupModalProps> = props => {
    const [group, setGroup] = useState<Group | null>(null);

    useEffect(() => {
        if (props?.group) {
            setGroup(props.group);
        }
    }, [props?.group])

    const {
        contentContainer,
        inputRow,
        modalActions,
        actionButton,
    } = modalStyles;
    const {
        createButton,
        cancelButton,
        radioInput
    } = styles;

    const handleGroupCreateClick = () => {
        if (group?.name && group?.description) {
            props.onCreateGroup(group);
            handleClose();
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

    const handleClose = () => {
        setGroup(null);
        props.onClose();
    }

    return (
        <BaseModal {...props}>
            <div className={contentContainer}>
                <h1>{props.isInEditMode ? 'Edit' : 'Create New'} Group</h1>
                <div className={inputRow}>
                    <span>Group name</span>
                    <input
                        name='name'
                        type="text" placeholder="Awesome group"
                        value={group?.name || ''}
                        onChange={setGroupData}
                    />
                </div>
                <div className={inputRow}>
                    <span>Group description</span>
                    <input
                        name='description'
                        type="text"
                        value={group?.description || ''}
                        placeholder="My group description"
                        onChange={setGroupData}
                    />
                </div>
                <div className={inputRow}>
                    <span>Group type</span>
                    <div>
                        <input className={radioInput} type="radio" id="public" name="type" value="public" onChange={setGroupData} />
                        <label htmlFor="public">Project</label>
                    </div>
                    <div>
                        <input className={radioInput} type="radio" id="private" name="type" value="private" onChange={setGroupData} />
                        <label htmlFor="private">Study</label>
                    </div>
                </div>
                <div className={modalActions}>
                    <button
                        className={`${actionButton} ${createButton} ${group?.name && group?.description && group?.type ? '' : 'disabled'}`}
                        onClick={handleGroupCreateClick}
                    >
                        Create Group
                    </button>
                    <button
                        className={`${actionButton} ${cancelButton}`}
                        onClick={handleClose}
                    >
                        Cancel
                    </button>
                </div>
            </div>
        </BaseModal>
    );
};

export default CreateGroupModal;

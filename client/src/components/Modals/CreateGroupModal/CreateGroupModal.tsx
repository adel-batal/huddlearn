import BaseModal from '../BaseModal/BaseModal';
import { CreateGroupModalProps } from '../../../types/modal';
import styles from './CreateGroupModal.module.css';

const CreateGroupModal: React.FC<CreateGroupModalProps> = props => {
    const {
        contentContainer,
        inputRow,
        modalActions,
        actionButton,
        createButton,
        cancelButton
    } = styles;
    return (
        <div>
            <BaseModal {...props}>
                <div className={contentContainer}>
                    <h1>Create New Group</h1>
                    <div className={inputRow}>
                        <span>Group name</span>
                        <input type="text" placeholder="Awesome group" />
                    </div>
                    <div className={inputRow}>
                        <span>Group description</span>
                        <input type="text" placeholder="My group description" />
                    </div>
                    <div className={modalActions}>
                        <button className={`${actionButton} ${createButton}`}>Create Group</button>
                        <button className={`${actionButton} ${cancelButton}`} onClick={props.onClose}>Cancel</button>
                    </div>
                </div>
            </BaseModal>
        </div>
    );
};

export default CreateGroupModal;

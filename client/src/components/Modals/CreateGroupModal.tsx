import BaseModal from './BaseModal';
import { CreateGroupModalProps } from '../../types/modal';

const CreateGroupModal: React.FC<CreateGroupModalProps> = props => {
    return (
        <div>
            <BaseModal {...props}>
                <p>Create Group Modal</p>
            </BaseModal>
        </div>
    );
};

export default CreateGroupModal;

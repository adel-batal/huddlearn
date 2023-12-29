import { Group } from "./types";
import { UserLogin } from "./types";
export type ModalProps = {
    isOpen: boolean;
    onClose: () => void;
    children?: React.ReactNode;
};


export type CreateGroupModalProps = ModalProps & {
    onCreateGroup: (group: Group) => void;
};

export type LoginModalProps = ModalProps & {
    onLogin: (user: UserLogin) => void;
};
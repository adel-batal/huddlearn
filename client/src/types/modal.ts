import { Group } from "./types";

export type ModalProps = {
    isOpen: boolean;
    onClose: () => void;
    children?: React.ReactNode;
};


export type CreateGroupModalProps = ModalProps & {
    onCreateGroup: (group: Group) => void;
};
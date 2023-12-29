export type NavbarProps = {
    openCreateGroupModal: () => void;
}

export type Group = {
    id?: string;
    name: string;
    description: string;
    image?: string;
    members?: number;
    type?: string;
    owner: string;
}

export type GroupsProps = {
    groups: Group[];
    handleEditGroup: (id: string) => void;
    handleDeleteGroup: (id: string) => void;
    handleRequestJoinGroup: (id: string) => void;
  };

export type ContainerComponentProps = {
    children: React.ReactNode;
}

export type GroupCardProps = {
    group: Group;
    deleteGroup: (id: string) => void;
    editGroup: (id: string) => void;
    requestJoinGroup: (id: string) => void;
}
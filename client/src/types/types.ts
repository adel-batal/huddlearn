export type NavbarProps = {
    openCreateGroupModal: () => void;
    openLoginModal: () => void;
    openRegisterModal: () => void;
    loggedInUser: User | null;
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

export type User = {
    id: string;
    name: string;
    email: string;
    groups?: Group[];
    type?: string;
}

export type UserLogin = {
    email: string;
    password: string;
}
export type UserRegister = UserLogin & {
    name: string;
}
export type NavbarProps = {
    openCreateGroupModal: () => void;
}

export type Group = {
    id?: number;
    name: string;
    description: string;
    image?: string;
    members?: number;
    type?: string;
    owner: string;
}

export type GroupsProps = {
    groups: Group[];
  };

export type ContainerComponentProps = {
    children: React.ReactNode;
}

export type GroupCardProps = {
    group: Group;
}
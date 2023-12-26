export type NavbarProps = {
    openCreateGroupModal: () => void;
}

export type Group = {
    id: number;
    name: string;
    description: string;
    image: string;
    members: number;
}

export type GroupsProps = {
    groups: Group[];
  };

export type containerComponentProps = {
    children: React.ReactNode;
}
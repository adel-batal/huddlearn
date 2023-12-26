import { Group, GroupsProps } from "../../types/types";

const Groups: React.FC<GroupsProps> = ({ groups }) => {
    return (
        <div>
            <h1>Groups</h1>
            <ul>
                {groups.map((group: Group) => (
                    <li key={group.id}>{group.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Groups;

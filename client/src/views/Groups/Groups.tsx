import { Group, GroupsProps } from "../../types/types";
import ViewContainer from "../../components/viewContainer/ViewContainer";
const Groups: React.FC<GroupsProps> = ({ groups }) => {
    return (
        <ViewContainer>
            <h1>Groups</h1>
            <div>
                {groups.map((group: Group) => (
                    <span key={group.id}>{group.name}</span>
                ))}
            </div>
        </ViewContainer>
    );
};

export default Groups;

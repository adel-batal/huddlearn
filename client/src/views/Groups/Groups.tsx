import { Group, GroupsProps } from "../../types/types";
import ViewContainer from "../../components/ViewContainer/ViewContainer";
import GroupCard from "../../components/GroupCard/GroupCard";
import styles from "./Groups.module.css";

const Groups: React.FC<GroupsProps> = ({ groups }) => {
    return (
        <ViewContainer>
            <h1>Groups</h1>
            <div className={styles.groupContainer}>
                {groups.map((group: Group) => (
                    <GroupCard key={group.id} group={group} />
                ))}
            </div>
        </ViewContainer>
    );
};

export default Groups;

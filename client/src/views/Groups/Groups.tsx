import { Group, GroupsProps } from "../../types/types";
import ViewContainer from "../../components/ViewContainer/ViewContainer";
import GroupCard from "../../components/GroupCard/GroupCard";
import styles from "./Groups.module.css";

const Groups: React.FC<GroupsProps> = ({ title, groups, loggedInUser, handleEditGroup, handleRequestJoinGroup, handleDeleteGroup }) => {
    return (
        <ViewContainer>
            <div className="view-header">
                <h1>{title}</h1>
            </div>
            <div className={styles.groupContainer}>
                {groups.map((group: Group) => (
                    <GroupCard
                        key={group.id}
                        group={group}
                        editGroup={handleEditGroup}
                        requestJoinGroup={handleRequestJoinGroup}
                        deleteGroup={handleDeleteGroup}
                        currentUserIsOwner={group.creator === loggedInUser?.id}
                        />
                ))}
            </div>
        </ViewContainer>
    );
};

export default Groups;

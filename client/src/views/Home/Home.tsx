import ViewContainer from "../../components/ViewContainer/ViewContainer";
import Groups from "../Groups/Groups";

const Home = ({ groups, handleEditGroup, handleRequestJoinGroup, handleDeleteGroup }) => {
    return (
        <ViewContainer>
            {groups.length
                ? <Groups
                    title="My Groups"
                    groups={groups}
                    handleEditGroup={handleEditGroup}
                    handleRequestJoinGroup={handleRequestJoinGroup}
                    handleDeleteGroup={handleDeleteGroup}

                />
                : <div className="view-header">
                    <h1>You are not in any groups</h1>
                    <h2>Join a group or create your own!</h2>
                </div>
            }

        </ViewContainer>
    );
};

export default Home;

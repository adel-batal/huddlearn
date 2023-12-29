import ViewContainer from "../../components/ViewContainer/ViewContainer";
import Groups from "../Groups/Groups";

const Home = ({
    groups,
    loggedInUser,
    handleEditGroup,
    handleRequestJoinGroup,
    handleDeleteGroup }) => {
    return (
        <ViewContainer>
            {loggedInUser
                ? (groups.length
                    ? <Groups
                        title="My Groups"
                        groups={groups}
                        handleEditGroup={handleEditGroup}
                        handleRequestJoinGroup={handleRequestJoinGroup}
                        handleDeleteGroup={handleDeleteGroup}
                        loggedInUser={loggedInUser}
                    />
                    : <div className="home-empty-content">
                        <h1>You are not in any groups</h1>
                        <h2>Join a group or create your own!</h2>
                    </div>
                )
                : (
                    <div className="home-empty-content">
                        <h1>Welcome to <span className="purple-text">HuddLearn!</span></h1>
                        <h2>Sign up or log in to get started</h2>
                    </div>
                )
            }
        </ViewContainer>
    );
};

export default Home;

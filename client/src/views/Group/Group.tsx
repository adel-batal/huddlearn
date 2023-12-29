import { useParams } from "react-router-dom";
import ViewContainer from "../../components/ViewContainer/ViewContainer";

const Group = () => {
    const { id } = useParams();
    return (
        <ViewContainer>
            <div className="view-header">
                <h1>Group {id}</h1>
            </div>
        </ViewContainer>
    )
}

export default Group
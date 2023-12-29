import { useParams } from "react-router-dom";

const Group = () => {
    const { id } = useParams();
    return (
        <div className="view-header">
            <h1>Group {id}</h1>
        </div>
    )
}

export default Group
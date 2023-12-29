import { useParams } from "react-router-dom";

const Group = () => {
    const { id } = useParams();
    return (
        <div>Group {id}</div>
    )
}

export default Group
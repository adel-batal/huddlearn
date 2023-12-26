import React from "react"
import { ContainerComponentProps } from "../../types/types"
import styles from "./ViewContainer.module.css"
const ViewContainer: React.FC<ContainerComponentProps> = ({ children }) => {
    return (
        <div className={styles.viewContainer}>
            {children}
        </div>
    )
}

export default ViewContainer
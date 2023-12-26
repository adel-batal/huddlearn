import React from "react"
import { containerComponentProps } from "../../types/types"
import styles from "./ViewContainer.module.css"
const ViewContainer: React.FC<containerComponentProps> = ({ children }) => {
    return (
        <div className={styles.viewContainer}>
            {children}
        </div>
    )
}

export default ViewContainer
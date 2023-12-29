import BaseModal from '../BaseModal/BaseModal';
import { UserLogin } from '../../../types/types';
import modalStyles from '../ModalCommonStyles.module.css';
import styles from './LoginModal.module.css';
import { useState } from 'react';
import { LoginModalProps } from '../../../types/modal';
const LoginModal: React.FC<LoginModalProps> = props => {
    const [loginData, setLoginData] = useState<UserLogin>({ name: '', password: '' });
    const {
        contentContainer,
        inputRow,
        modalActions,
        actionButton,
    } = modalStyles;
    const {
        loginButton,
    } = styles;


    const handleLoginClick = () => {
        if (loginData?.name && loginData?.password) {
            props.onLogin(loginData);
            handleClose();
        } else {
            alert("Please enter your username and password");
        }
    }
    const handleLoginDataChange = (e: { target: { name: string; value: string; }; }) => {
        setLoginData(prevLoginData => ({
            ...prevLoginData,
            [e.target.name]: e.target.value,
        }));
    }

    const handleClose = () => {
        setLoginData({ name: '', password: '' });
        props.onClose();
    }

    return (
        <BaseModal {...props}>
            <div className={contentContainer}>
                <h1>Login</h1>
                <div className={inputRow}>
                    <span>username</span>
                    <input
                        name='name'
                        type="text" placeholder="john"
                        onChange={handleLoginDataChange}
                    />
                </div>
                <div className={inputRow}>
                    <span>Password</span>
                    <input
                        name='password'
                        type="text"
                        placeholder="•••••••••"
                        onChange={handleLoginDataChange}
                    />
                </div>
                <div className={modalActions}>
                    <button
                        className={`${actionButton} ${loginButton}`}
                        onClick={handleLoginClick}
                    >
                        Login
                    </button>
                </div>
            </div>
        </BaseModal>
    )
}

export default LoginModal
import BaseModal from '../BaseModal/BaseModal';
import { UserRegister } from '../../../types/types';
import modalStyles from '../ModalCommonStyles.module.css';
import styles from '../LoginModal/LoginModal.module.css';
import { useState } from 'react';
import { RegisterModalProps } from '../../../types/modal';
const RegisterModal: React.FC<RegisterModalProps> = props => {
    const [registerData, setRegisterData] = useState<UserRegister>(
        {
            name: '',
            email: '',
            password: ''
        });
    const {
        contentContainer,
        inputRow,
        modalActions,
        actionButton,
    } = modalStyles;
    const {
        loginButton,
    } = styles;


    const handleRegisterClick = () => {
        if (registerData?.email && registerData?.password) {
            props.onRegister(registerData);
            handleClose();
        } else {
            alert("Please enter your name, email and password");
        }
    }
    const handleregisterDataChange = (e: { target: { name: string; value: string; }; }) => {
        setRegisterData(prevRegisterData => ({
            ...prevRegisterData,
            [e.target.name]: e.target.value,
        }));
    }

    const handleClose = () => {
        setRegisterData({ name: '', email: '', password: '' });
        props.onClose();
    }

    return (
        <BaseModal {...props}>
            <div className={contentContainer}>
                <h1>Register</h1>
                <div className={inputRow}>
                    <span>Name</span>
                    <input
                        name='name'
                        type="text" placeholder="John Doe"
                        onChange={handleregisterDataChange}
                    />
                </div>
                <div className={inputRow}>
                    <span>Email</span>
                    <input
                        name='email'
                        type="text" placeholder="me@example.com"
                        onChange={handleregisterDataChange}
                    />
                </div>
                <div className={inputRow}>
                    <span>Password</span>
                    <input
                        name='password'
                        type="text"
                        placeholder="•••••••••"
                        onChange={handleregisterDataChange}
                    />
                </div>
                <div className={modalActions}>
                    <button
                        className={`${actionButton} ${loginButton}`}
                        onClick={handleRegisterClick}
                    >
                        Register
                    </button>
                </div>
            </div>
        </BaseModal>
    )
}

export default RegisterModal
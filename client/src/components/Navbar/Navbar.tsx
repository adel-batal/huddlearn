import styles from './Navbar.module.css';
import { Link } from 'react-router-dom';
import { NavbarProps } from '../../types/types';

const Navbar: React.FC<NavbarProps> = ({ openCreateGroupModal, loggedInUser, openLoginModal, openRegisterModal, handleLogout }) => {
    return (
        <header className={styles.navbar}>
            <div className={styles.logo}><Link to="/">HuddLearn</Link></div>
            <nav>
                <ul className={styles.navLinks}>
                    <li className={`${!loggedInUser && 'hidden'}`}>
                        <Link to="/groups" className={styles.navLink}>
                            Browse Groups
                        </Link>
                    </li>
                    <li className={`${!loggedInUser && 'hidden'}`}>
                        <span className={styles.cta} onClick={openCreateGroupModal}>
                            Create Group
                        </span>
                    </li>
                    <li className={`${loggedInUser && 'hidden'}`}>
                        <span className={styles.navLink} onClick={openLoginModal}>
                            Login
                        </span>
                    </li>
                    <li className={`${loggedInUser && 'hidden'}`}>
                        <span className={styles.cta} onClick={openRegisterModal}>
                            Register
                        </span>
                    </li>
                    <li className={`${!loggedInUser && 'hidden'}`}>
                        <span className={styles.navLink} onClick={handleLogout}>
                            Logout
                        </span>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Navbar;

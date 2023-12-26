import styles from './Navbar.module.css';
import { Link } from 'react-router-dom';
import { NavbarProps } from '../../types/types';

const Navbar: React.FC<NavbarProps> = ({ openCreateGroupModal }) => {
    return (
        <header className={styles.navbar}>
            <div className={styles.logo}><Link to="/">HuddLearn</Link></div>
            <nav>
                <ul className={styles.navLinks}>
                    <li><Link to="/groups" className={styles.navLink}>Browse Groups</Link></li>
                    <li><span className={styles.cta} onClick={openCreateGroupModal}>Create Group</span></li>
                </ul>
            </nav>
        </header>
    );
};

export default Navbar;

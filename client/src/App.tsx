import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './views/Home/Home'
import Groups from './views/Groups/Groups'
import Navbar from './components/Navbar/Navbar'
import { useEffect, useState } from 'react';
import CreateGroupModal from './components/Modals/CreateGroupModal/CreateGroupModal';
import { Group as GroupType } from './types/types';
import Group from './views/Group/Group';
import axios from 'axios';
import LoginModal from './components/Modals/LoginModal/LoginModal';
import RegisterModal from './components/Modals/RegisterModal/RegisterModal';

const API = 'http://localhost:8000';
function App() {
  const [isCreateGroupModalOpen, setIsCreateGroupModalOpen] = useState(false);
  const [currentGroups, setCurrentGroups] = useState([]);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);
  const [myGroups, setMyGroups] = useState<GroupType[]>([]); // groups that the user is a member of
  const [loggedInUser, setLoggedInUser] = useState(null); // user object
  const [isInEditMode, setIsInEditMode] = useState(false); // whether the create group modal is in edit mode or not
  const [groupToEdit, setGroupToEdit] = useState<GroupType | null>(null); // group object to edit

  const fetchGroups = async () => {
    try {
      const response = await axios.get(`${API}/studygroups`, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('huddle.jwtToken')}`
        },
      });
      setCurrentGroups(response?.data?.studygroup ?? []);
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  };

  useEffect(() => {
    const storedUser = localStorage.getItem('huddle.user');
    if (storedUser) {
      setLoggedInUser(storedUser);
    }
    fetchGroups();
  }, [])

  useEffect(() => {
    setMyGroups(currentGroups.filter(group => group.owner === storedUser?.id));
  }, [currentGroups])


  const handleCreateGroup = (group: GroupType) => {
    const newGroup = { ...group, owner: loggedInUser?.id, type: 'study' };
    try {
      axios.post(`${API}/studygroups/`, newGroup, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('huddle.jwtToken')}`
        },
      });
      setCurrentGroups([...currentGroups, { ...newGroup, id: currentGroups.length + 1 }]);
      setMyGroups([...myGroups, { ...newGroup, id: currentGroups.length + 1 }]);
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  }


  const handleEditGroup = (id: string | undefined) => {
    if (!id) return
    setIsInEditMode(true);
    setGroupToEdit(currentGroups.find(group => group.id === id) || null);
    setIsCreateGroupModalOpen(true);
  }

  const editGroup = (group: GroupType) => {
    if (!group) return
    try {
      axios.put(`${API}/studygroups/${group.id}`, group, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('huddle.jwtToken')}`
        },
      });
      const groupToEdit = currentGroups.find(groupData => groupData.id === group.id);
      if (!groupToEdit) return
      const updatedGroups = currentGroups.map(groupData => {
        if (groupData.id === group.id) {
          return group;
        }
        return groupData;
      });
      setCurrentGroups(updatedGroups);
      setMyGroups(prevMyGroups => {
        const updatedMyGroups = prevMyGroups.map(groupData => {
          if (groupData.id === group.id) {
            return group;
          }
          return groupData;
        });
        return updatedMyGroups;
      });
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  }

  const handleRequestJoinGroup = (id: string | undefined) => {
    if (!id) return
    alert('not implemented yet')
  }
  const handleDeleteGroup = async (id: string | undefined) => {
    if (!id) return
    try {
      await axios.delete(`${API}/studygroups/${id}`, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('huddle.jwtToken')}`
        },
      });
      setCurrentGroups(currentGroups.filter(group => group.id !== id));
      setMyGroups(myGroups.filter(group => group.id !== id));
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  }
  const handleLogin = async ({ name, password }) => {
    try {
      const response = await axios.post(`${API}/auth/login/`, {
        username: name,
        password
      });
      localStorage.setItem('huddle.user', JSON.stringify({ name, email }));
      localStorage.setItem('huddle.jwtToken', response.data.access);
      setLoggedInUser({ name: response.data.user.username, email: response.data.user.email });
      setIsRegisterModalOpen(false);
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  }
  const handleRegister = async ({ name, email, password }) => {
    try {
      const response = await axios.post(`${API}/auth/register/`, {
        username: name,
        email,
        password
      });
      localStorage.setItem('huddle.user', JSON.stringify({ name, email }));
      localStorage.setItem('huddle.jwtToken', response.data.access);
      setLoggedInUser({ name: response.data.user.username, email: response.data.user.email });
      setIsRegisterModalOpen(false);
    } catch (error) {
      console.error('Oops, Django is playing hard to get:', error);
    }
  }

  const handleLogout = () => {
    localStorage.removeItem('huddle.jwtToken');
    localStorage.removeItem('huddle.user');
    setLoggedInUser(null);
  }

  return (
    <>
      <Router>
        <Navbar
          openCreateGroupModal={() => setIsCreateGroupModalOpen(true)}
          openLoginModal={() => setIsLoginModalOpen(true)}
          openRegisterModal={() => setIsRegisterModalOpen(true)}
          handleLogout={handleLogout}
          loggedInUser={loggedInUser}
        />
        <Routes>
          <Route path="/" element={<Home
            groups={myGroups}
            handleEditGroup={handleEditGroup}
            handleRequestJoinGroup={handleRequestJoinGroup}
            handleDeleteGroup={handleDeleteGroup}
            loggedInUser={loggedInUser}
          />
          } />
          <Route path="/groups" element={<Groups
            title="All Groups"
            groups={currentGroups}
            handleEditGroup={handleEditGroup}
            handleRequestJoinGroup={handleRequestJoinGroup}
            handleDeleteGroup={handleDeleteGroup}
            loggedInUser={loggedInUser}
          />
          } />
          <Route path="/groups/:id" Component={Group} />
        </Routes>
      </Router>
      <CreateGroupModal
        isInEditMode={isInEditMode}
        group={isInEditMode ? groupToEdit : undefined}
        onCreateGroup={isInEditMode ? editGroup : handleCreateGroup}
        isOpen={isCreateGroupModalOpen}
        onClose={() => {
          setIsCreateGroupModalOpen(false)
          setIsInEditMode(false)
        }}
      />
      <LoginModal
        onLogin={handleLogin}
        isOpen={isLoginModalOpen}
        onClose={() => setIsLoginModalOpen(false)}
      />
      <RegisterModal
        onRegister={handleRegister}
        isOpen={isRegisterModalOpen}
        onClose={() => setIsRegisterModalOpen(false)}
      />
    </>
  )
}

export default App

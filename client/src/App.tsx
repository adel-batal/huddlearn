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
function App() {
  const [isCreateGroupModalOpen, setIsCreateGroupModalOpen] = useState(false);
  const [currentGroups, setCurrentGroups] = useState(groups);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);
  const loggedInUser = {
    id: '1',
    name: 'John Doe',
    email: 'me@example.com'
  };

  // const fetchData = async () => {
  //   try {
  //     const response = await axios.get('');
  //     console.log('Data:', response.data);
  //   } catch (error) {
  //     console.error('Oops, Django is playing hard to get:', error);
  //   }
  // };


  // temporary code until we have proper authentication and state management
  useEffect(() => {
    interface CustomWindow extends Window {
      owner: string;
    }

    const customWindow = window as unknown as CustomWindow;
    customWindow.owner = '1';
  }, [])

  const handleCreateGroup = (group: GroupType) => {
    if (group) {
      setCurrentGroups([...currentGroups, { ...group, id: currentGroups.length + 1 }]);
    }
  }


  const handleEditGroup = (id: string | undefined) => {
    if (!id) return
    console.log('Edit group with id:', id);
  }

  const handleRequestJoinGroup = (id: string | undefined) => {
    if (!id) return
    console.log('Request to join group with id:', id);
  }
  const handleDeleteGroup = (id: string | undefined) => {
    if (!id) return
    console.log('Delete group with id:', id);
  }
  const handleLogin = () => {
    console.log('Login');
  }
  const handleRegister = () => {
    console.log('Register');
  }

  return (
    <>
      <Router>
        <Navbar
          openCreateGroupModal={() => setIsCreateGroupModalOpen(true)}
          openLoginModal={() => setIsLoginModalOpen(true)}
          openRegisterModal={() => setIsRegisterModalOpen(true)}
          loggedInUser={null}
        />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/groups" element={<Groups
            groups={currentGroups}
            handleEditGroup={handleEditGroup}
            handleRequestJoinGroup={handleRequestJoinGroup}
            handleDeleteGroup={handleDeleteGroup}
          />
          }
          />
          <Route path="/groups/:id" Component={Group} />
        </Routes>
      </Router>
      <CreateGroupModal onCreateGroup={handleCreateGroup} isOpen={isCreateGroupModalOpen} onClose={() => setIsCreateGroupModalOpen(false)} />
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
// fake group data until we connect to the backend
const groups: GroupType[] = [
  {
    id: '1',
    name: "Group 1",
    description: "This is the first group",
    members: 1,
    image: "https://picsum.photos/200/300",
    type: "study",
    owner: '1'
  },
  {
    id: '2',
    name: "Group 2",
    description: "This is the second group",
    members: 2,
    image: "https://picsum.photos/200/300",
    type: "project",
    owner: '1'
  },
  {
    id: '3',
    name: "Group 3",
    description: "This is the third group",
    members: 3,
    image: "https://picsum.photos/200/300",
    type: "study",
    owner: '2'
  },
  {
    id: '4',
    name: "Group 4",
    description: "This is the fourth group",
    members: 4,
    image: "https://picsum.photos/200/300",
    type: "project",
    owner: '4'
  },
  {
    id: '5',
    name: "Group 5",
    description: "This is the fifth group",
    members: 5,
    image: "https://picsum.photos/200/300",
    type: "study",
    owner: '1'
  },
];

export default App

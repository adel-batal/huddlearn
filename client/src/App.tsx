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
  const currentUser = {
    id: '1',
    name: 'John Doe',
    email: 'me@example.com'
  };
  // const currentUser = null;
  const [isCreateGroupModalOpen, setIsCreateGroupModalOpen] = useState(false);
  const [currentGroups, setCurrentGroups] = useState(groups);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);
  const [myGroups, setMyGroups] = useState<GroupType[]>([]); // groups that the user is a member of
  const [loggedInUser, setLoggedInUser] = useState(currentUser); // user object
  const [isInEditMode, setIsInEditMode] = useState(false); // whether the create group modal is in edit mode or not
  const [groupToEdit, setGroupToEdit] = useState<GroupType | null>(null); // group object to edit
  // const fetchData = async () => {
  //   try {
  //     const response = await axios.get('');
  //     console.log('Data:', response.data);
  //   } catch (error) {
  //     console.error('Oops, Django is playing hard to get:', error);
  //   }
  // };


  useEffect(() => {
    setLoggedInUser(currentUser);
    setCurrentGroups(groups);
    setMyGroups(currentGroups.filter(group => group.owner === currentUser?.id));
  }, [])


  const handleCreateGroup = (group: GroupType) => {
    if (group) {
      setCurrentGroups([...currentGroups, { ...group, id: currentGroups.length + 1 }]);
      setMyGroups([...myGroups, { ...group, id: currentGroups.length + 1 }]);
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

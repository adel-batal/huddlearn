import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './views/Home/Home'
import Groups from './views/Groups/Groups'
import Navbar from './components/Navbar/Navbar'
import { useState } from 'react';
import CreateGroupModal from './components/Modals/CreateGroupModal/CreateGroupModal';

function App() {
  const [isCreateGroupModalOpen, setIsCreateGroupModalOpen] = useState(false);
  return (
    <>
      <Router>
        <Navbar openCreateGroupModal={() => setIsCreateGroupModalOpen(true)} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/groups" element={<Groups groups={groups}/>} />
        </Routes>
      </Router>
      <CreateGroupModal isOpen={isCreateGroupModalOpen} onClose={() => setIsCreateGroupModalOpen(false)} />
    </>
  )
}

// fake group data until we connect to the backend
const groups = [
  {
    id: 1,
    name: "Group 1",
    description: "This is the first group",
    members: 1,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 2,
    name: "Group 2",
    description: "This is the second group",
    members: 2,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 3,
    name: "Group 3",
    description: "This is the third group",
    members: 3,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 4,
    name: "Group 4",
    description: "This is the fourth group",
    members: 4,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 5,
    name: "Group 5",
    description: "This is the fifth group",
    members: 5,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 6,
    name: "Group 6",
    description: "This is the sixth group",
    members: 6,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 7,
    name: "Group 7",
    description: "This is the seventh group",
    members: 7,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 8,
    name: "Group 8",
    description: "This is the eighth group",
    members: 8,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 9,
    name: "Group 9",
    description: "This is the ninth group",
    members: 9,
    image: "https://picsum.photos/200/300"
  },
  {
    id: 10,
    name: "Group 10",
    description: "This is the tenth group",
    members: 10,
    image: "https://picsum.photos/200/300"
  }
];

export default App

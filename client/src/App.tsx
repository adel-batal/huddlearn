import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home'
import Groups from './components/Groups/Groups'
import Navbar from './components/Navbar/Navbar'
import { useState } from 'react';
import CreateGroupModal from './components/Modals/CreateGroupModal';

function App() {
  const [isCreateGroupModalOpen, setIsCreateGroupModalOpen] = useState(false);
  return (
    <>
      <Router>
        <Navbar openCreateGroupModal={() => setIsCreateGroupModalOpen(true)}/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/groups" element={<Groups />} />
        </Routes>
      </Router>
      <CreateGroupModal isOpen={isCreateGroupModalOpen} onClose={() => setIsCreateGroupModalOpen(false)}/>
    </>
  )
}

export default App

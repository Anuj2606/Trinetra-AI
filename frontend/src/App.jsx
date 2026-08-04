import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import History from "./pages/History";
import About from "./pages/About";
import Analytics from "./pages/Analytics";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />

      <Route path="/dashboard" element={<Dashboard />} />

      <Route path="/history" element={<History />} />

      <Route path="/about" element={<About />} />

      <Route path="/analytics" element={<Analytics/>}/>
    </Routes>
  );
}

export default App;
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import SearchEngine from "./components/SearchEngine";

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/search" element={<SearchEngine />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

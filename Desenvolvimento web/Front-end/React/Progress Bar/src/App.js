import "./scripts/cardStyle.css"
import Card from "./scripts/Card.js"

export default function App() {
  return (
    <div className="App">
      <div className="container">
        <Card porcentage="85" title="HTML5" color="#04fc43"/>
        <Card porcentage="85" title="JavaScript" color="#fee800"/>
        <Card porcentage="85" title="CSS3" color="#ff00be"/>
        <Card porcentage="70" title="React" color="#06ccff"/>
      </div>
    </div>
  );
}


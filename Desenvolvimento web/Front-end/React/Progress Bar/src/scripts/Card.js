export default function Card(props) {
  console.log(props);

    return (
      <div className="card">
        <div className="percent" style={{ '--clr': props.color, '--num': props.porcentage }}>
            <div className="dot"></div>
            <svg>
                <circle cx="70" cy="70" r="70"></circle>
                <circle cx="70" cy="70" r="70"></circle>
            </svg>
            <div className="number">
                <h2>{props.porcentage}<span>%</span></h2>
                <p>{props.title}</p>
            </div>
        </div>
      </div>
    );
  }
import { Link } from "react-router-dom"

function Header(){
    return (
        
        <div className="headerDiv">
            <span className="headerButtonContainer">
                <Link to = "/dayview">
                <button className="headerButton">My Day</button>
                </Link>
                <Link to = "/dashboard">
                <button className="headerButton">Dashboard</button>
                </Link>
                <Link to = "/info">
                <button className="headerButton">Info</button>
                </Link>
            </span>
            <span className="loginButton">
            <Link to = "/login">
            <button>login</button>
            </Link>
            </span>
        </div>
    )
}

export default Header
import { Link } from "react-router-dom"

function Home(){
    return ( 
        <div>
            
        <h1>Improvement happens one day at a time!</h1>
        <Link to = "/login">
        <button>LogIn</button>
        </Link>
        </div>
    )
}

export default Home
import React, {useState} from "react"

function Login(){

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    function handleSubmit(e) {
        e.preventDefault()
        console.log(username, password)
    }
    return(
        <div className="loginPage">
            <div className="loginContainer">
                <h1 id="loginStyle">Login to track your life!</h1>
                <form  
                onSubmit={handleSubmit}
                className="LoginForm">
                            <div className="loginBoxes">
                                <label className="activityLabel">Username: </label>
                                <div className="loginBoxes"/>
                                <input 
                                onChange={(e) => setUsername(e.target.value)}
                                id="inputField"  
                                type="text"
                                />
                            </div>
                            <div className="loginBoxes">
                                <label className="activityLabel">Password: </label>
                                <div className="loginBoxes"/>
                                <input 
                                onChange={(e) => setPassword(e.target.value)}
                                id="inputField"  
                                type="text"/>
                            </div>
                            <input 
                            type="submit" 
                            />
                </form>
        </div>
        </div>
    )
}

export default Login
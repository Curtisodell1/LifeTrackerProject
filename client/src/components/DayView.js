import React, {useState} from "react"

function DayView(){
    

    const [note, setNote] = useState("")
    const [walk, setWalk] = useState(0)
    const [project, setProject] = useState (0)
    const [other, setOther] = useState (0)

    function handleSubmit(e) {
        e.preventDefault()
        console.log(note, walk, project, other)
        handleReset()

    }
    function handleReset(){
        setNote("")
        setWalk(0)
        setProject(0)
        setOther(0)
    }

    return (
        <div className="dayPage">
            <div className="inputContainer">
                <form onSubmit={handleSubmit} className="feelingForm">
                    <h1 className="feelingHeadLine">How are you feeling?</h1>
                    <div class="slidecontainer">
                    <input type="range" min="1" max="10" value="5" class="slider" id="myRange"/>
                    </div>
                        <div>
                                <label className="activityLabel">Did you go for a walk?</label>
                                    <div className="entryDivs">
                                        <span className="yes">
                                        <label for="work" className="choiceLabels"> Yes!</label>
                                        <input onClick={(e) => setWalk(1)}
                                        className="radioButton"
                                        type="radio" name="walk" />
                                        </span>
                                        <span className="yes">
                                        <label className="choiceLabels"> Not yet...</label>
                                        <input className="radioButton" type="radio" name="walk"></input>
                                        </span>
                                    </div>
                        </div>
                        <div>
                                <label className="activityLabel">Did you work on a project?</label>
                                    <div className="entryDivs">
                                        <span className="yes">
                                        <label className="choiceLabels"> Yes!</label>
                                        <input 
                                        onClick={(e) => setProject(1)}
                                        className="radioButton" 
                                        type="radio" 
                                        name="work"/>
                                        </span>
                                        <span className="yes">
                                        <label className="choiceLabels"> Not yet...</label>
                                        <input className="radioButton" type="radio" name="work"></input>
                                        </span>
                                    </div>
                        </div>
                        <div>
                                <label className="activityLabel"> Did you do your other thing?</label>
                                    <span className="entryDivs">
                                        <span className="yes">  
                                        <label className="choiceLabels"> Yes!</label>
                                        <input 
                                        onClick={(e) => setOther(1)}
                                        className="radioButton" 
                                        type="radio" 
                                        name="other"/>
                                        </span>
                                        <span className="yes">
                                        <label className="choiceLabels"> Not yet...</label>
                                        <input className="radioButton" type="radio" name="other"></input>
                                        </span>
                                    </span>
                        </div>
                            <div className="entryDivs">
                                <label className="activityLabel">What felt good so far today?: </label>
                                <div className="entryDivs">
                                <input 
                                onChange={(e) => setNote(e.target.value)}
                                id="inputField"  
                                type="text"/>
                                </div>
                        </div>
                            <input 
                            type="submit" />
                </form>
        </div>
        </div>
    )
}

export default DayView
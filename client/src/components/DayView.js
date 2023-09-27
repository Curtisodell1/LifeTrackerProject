

function DayView(){

    function handleSubmit(e) {
        e.preventDefault()
        console.log()
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
                                <input className="radioButton" type="radio" name="walk"></input>
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
                                <input className="radioButton" type="radio" name="work"></input>
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
                                <input className="radioButton" type="radio" name="other"></input>
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
                                <input id="inputField" type="text"/>
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
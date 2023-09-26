

function DayView(){
    return (
        <div className="dayPage"> whole page
            <div className="inputContainer"> container for feelings
                <h1 className="feelingHeadLine">How are you feeling?</h1>
                <form className="feelingForm">
                    <div>
                        <span>
                            <label className="activityLabel">Did you go for a walk?</label>
                            <label> Yes!</label>
                            <input className="radioButton" type="radio"></input>
                            <label> Not yet...</label>
                            <input className="radioButton" type="radio"></input>
                        </span>
                    </div>
                    <div>
                        <span>
                            <label className="activityLabel">Did you work on a project?</label>
                            <label> Yes!</label>
                            <input className="radioButton" type="radio"></input>
                            <label> Not yet...</label>
                            <input className="radioButton" type="radio"></input>
                        </span>
                    </div>
                    <div>
                        <span>
                            <label className="activityLabel"> Did you do your other thing?</label>
                            <label> Yes!</label>
                            <input className="radioButton" type="radio"></input>
                            <label> Not yet...</label>
                            <input className="radioButton" type="radio"></input>
                        </span>
                    </div>
                </form>
            </div>
        </div>

    )
}

export default DayView
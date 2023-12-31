import React, { useState, useEffect } from "react"
import { useHistory } from "react-router-dom";

function DayView() {

    const [entry, setEntry] = useState([])
    useEffect(() => {
        fetch(`http://127.0.0.1:5555/entries`)
            .then(res => res.json())
            .then(setEntry)
    }, [])

    const history = useHistory()
    const [formData, setFormData] = useState();
    function handleSubmit(e) {
        e.preventDefault();
        console.log(note, walk, project, other, happiness)

        fetch(`http://127.0.0.1:5555/entries`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
            .then((r) => r.json())
            .then((data) => history.push(`/entries/${data.id}`));

        handleReset()
    }
    const [note, setNote] = useState("")
    const [walk, setWalk] = useState(0)
    const [project, setProject] = useState(0)
    const [other, setOther] = useState(0)
    const [happiness, setHappiness] = useState(5)


    // function handleSubmit(e) {
    //     e.preventDefault()




    // }
    function handleReset() {
        setNote("")
        setWalk(0)
        setProject(0)
        setOther(0)
        setHappiness(5)
    }

    return (
        <div className="dayPage">
            <div className="inputContainer">
                <form onSubmit={handleSubmit} className="feelingForm">
                    <h1 className="feelingHeadLine">How are you feeling?</h1>
                    <div className="slideContainer">
                        <label htmlFor="slider">Happiness Score</label>
                        <input
                            onChange={(e) => setHappiness(document.getElementById("happyMeter").value)}
                            type="range"
                            className="slider"
                            id="happyMeter"
                            min="1" max="10"
                        />
                    </div>
                    <div>
                        <label className="activityLabel">Did you go for a walk?</label>
                        <div className="entryDivs">
                            <span className="yes">
                                <label htmlFor="work" className="choiceLabels"> Yes!</label>
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
                                    onClick={() => setProject(1)}
                                    className="radioButton"
                                    type="radio"
                                    name="work" />
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
                                    name="other" />
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
                                type="text" />
                        </div>
                    </div>
                    <input
                        type="submit"
                        value="Submit" />
                </form>
            </div>
        </div>
    )
}

// const entry = useFormik({
//     initialValues: {
//         name:'',
//         email:'',
//         password:''
//     },
//     validationSchema: formSchema,
//     onSubmit: (values) => {
//         fetch(signUp?'/signup':'/login',{
//             method: "POST",
//             headers: {
//             "Content-Type": "application/json",
//         },
//             body: JSON.stringify(values, null, 2),
//         })
//         .then(res => {
//         if(res.ok){
//             res.json().then(user => {
//                 updateUser(user)
//                 history.push('/')
//             })
//         } else 
//             res.json().then(console.log)
//         })
//     }
//     })
export default DayView
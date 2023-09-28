import { useParams, useHistory } from 'react-router-dom'
import { useEffect, useState } from 'State'
import FeelingTrackerForm from './FeelingTrackerForm';

function FeelingTrackerContainer() {
    const [feeling, setFeeling] = useState();
    const { id } = useParams();

    useEffect(() => {
        fetch('http://127.0.0.1:5555/feelings')
            .then((r) => r.json())
            .then((data) => setFeeling(data))
    }, [id])
}

const renderMorningFeelings = feelings.map((morning_feeling) => <li>{morning_feeling}</li>)
const renderAfternoonFeelings = feelings.map((afternoon_feeling) => <li>{afternoon_feeling}</li>)
const renderEveningFeelings = feelings.map((evening_feeling) => <li>{evening_feeling}</li>)
const renderDescription = feelings.map((description) => <li>{description}</li>)

return (
    <div>
        <div className="morning_feelings">
            <h3>Morning Feelings</h3>
            <h4>{renderMorningFeelings}</h4>
        </div>
        <div className="afternoon_feelings">
            <h3>Afternoon Feelings</h3>
            <h4>{renderAfternoonFeelings}</h4>
        </div>
        <div className="evening_feelings">
            <h3>Evening Feelings</h3>
            <h4>{renderEveningFeelings}</h4>
        </div>
        <div className="description">
            <h3>Dsscription</h3>
            <h4>{renderDescription}</h4>
        </div>
    </div>
)




export default FeelingTrackerContainer;
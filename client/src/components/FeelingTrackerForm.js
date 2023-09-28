import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import FeelingTrackerContainer from "./FeelingTrackerContainer";



function FeelingTrackerForm() {
    const initialState = {
        morning_feeling: '',
        afternoon_feelings: '',
        evening_feeling: '',
        description: []
    }
    const [formData, setFormData] = useState(initialState);
    const history = useHistory();
    const {
        morning_feeling,
        afternoon_feelings,
        evening_feeling,
        description
    } = formData

}

export default FeelingTrackerForm
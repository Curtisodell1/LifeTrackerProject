// import React, { useState } from 'react'
// import { useHistory } from 'react-router-dom'


// const initialState = {
//     username: '',
//     password: ''
// }

// function Authentication({ updateUser }) {
//     const [signUp, setSignUp] = useState(false)
//     const [formState, setFormState] = useState(initialState)

//     const [errors, setErrors] = useState(null)
//     const history = useHistory()

//     const changeFormState = event => {
//         const { name, value } = event.target
//         setFormState({ ...formState, [name]: value })
//     }

//     const handleClick = () => setSignUp((signUp) => !signUp)

//     const postToLoginOrSignup = event => {
//         event.preventDefault()

//         const postRequest = {
//             method: 'POST',
//             headers: {
//                 'content-type': 'application/json',
//                 'accept': 'application/json'
//             },
//             body: JSON.stringify(formState)
//         }


//         fetch(signUp ? '/signup' : '/login', postRequest)
//             .then(r => r.json())
//             .then(userData => {
//                 if (userData.errors)
//                     setErrors(userData.errors)
//                 else {
//                     setErrors(null)
//                     updateUser(userData)
//                     history.push('/')
//                 }
//             })

//         return (
//             <>
//                 <h2 style={{ color: 'red' }}> {
//                     errors ? errors.map(error => <h5>{error}</h5>)
//                         : null
//                 }</h2>
//                 <h2>Please Log in or Sign up!</h2>
//                 <h2>{signUp ? 'Already a member?' : 'Not a member?'}</h2>
//                 <button onClick={handleClick}>{signUp ? 'Log In!' : 'Register now!'}</button>
//                 <Form onSubmit={postToLoginOrSignup}>
//                     <label>
//                         Username
//                     </label>
//                     <input type='text' name='username' value={formState.username} onChange={changeFormState} />
//                     <>
//                         <label>
//                             Password
//                         </label>
//                         <input type='password' name='password' value={formState.password} onChange={changeFormState} />
//                     </>
//                     <input type='submit' value={signUp ? 'Sign Up!' : 'Log In!'} />
//                 </Form>
//             </>
//         )
//     }
// }
// export default Authentication

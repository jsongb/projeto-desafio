import axios from "axios"
import Alert from '@/utils/Alert'

// Método de requisição com a biblioteca axios
const request = (endpoint = '', method = 'GET', data = {}, callback = ()=>{}, callback_error = ()=>{}) => {
    axios({
        method: method,
        url: `http://localhost:8000/${endpoint}`,
        data: data,
        headers: {
            'Content-Type': 'application/json', 
        },
    })
    .then((r)=>{
        callback(r)
    })
    .catch((error)=>{
        console.log(error)
        callback_error(error)
    })
}

export default request
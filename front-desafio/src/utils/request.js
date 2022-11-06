import axios from "axios"
import Alert from '@/utils/Alert'

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
        Alert(
            'Desculpe, houve um problema de comunicação com o servidor',
            'd'
        )
        callback_error()
    })
}

export default request
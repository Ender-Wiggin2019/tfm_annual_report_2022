import axios from 'axios';

const getAPI = axios.create({
    baseURL: 'http://103.152.132.156:8000',
    // baseURL: 'http://localhost:8000',
    timeout: 10000,
    headers:{'Content-Type':'application/json'}
})

export {
    getAPI
}

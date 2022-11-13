import axios from 'axios';

const getAPI = axios.create({
    baseURL: 'http://103.152.132.156:8000',
    timeout: 1000,
})

export {
    getAPI
}

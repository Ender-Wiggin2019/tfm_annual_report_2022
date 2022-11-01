import { createStore } from 'vuex'
import { getAPI } from '../axios.api';

export default createStore({
	state: {
		name: '',
		accessToken: null,
		refreshToken: null,
		userType: '',
		userTotal: ''
	},
	mutations: {
		updateStorage(state, { access, refresh, name, password }){
			state.accessToken = access;
			state.refreshToken = refresh;
			state.name = name;
		},
		destroyToken(state){
			state.accessToken = null;
			state.refreshToken = null;
			state.name = '';
		}
	},
	getters:{
		loggedIn(state){
			return state.accessToken != null
		}
	},
	actions: {
		userLogin(context, credentials){
			const userData = {
				'name': credentials.name,
				'password': credentials.password
			}
			return new Promise((resolve, reject) => {
				getAPI.post('/api/token/',
					userData, {
						headers:{
							'Content-Type': 'application/json'
						}
					}
				)
				.then(response => {
					context.commit('updateStorage', {
						access: response.data.access,
						refresh: response.data.refresh,
						name: credentials.name,
					})
					resolve()
				})
				.catch(err => {
					console.error(err);
					reject();
				})
			})
		},
		userLogout(context){
			if(context.getters.loggedIn){
				context.commit('destroyToken')
			}
		}
	},
	modules: {
	}
})

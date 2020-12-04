// root level actions
import core from '../api/core'
import { setAuthToken, removeAuthToken } from '../api/authToken'

export default {
    async startGame({ commit, dispatch }, { code, gender }) {
        await core
            .getGameState({ code, gender })
            .then(state => {
                setAuthToken(state.token);
                commit("SET_CODE", state.code);
                commit("ADD_TOKEN", state.token);
                commit("ADD_GENDER", state.gender);
                dispatch("finance/loadState", state.finances);
                commit("finance/ADD_INSURANCE", state.insurance);
                commit("levels/LOAD_LEVELS", { remaining: state.remaining, completed: state.completed });
                commit("levels/LOAD_LEVEL", state.current);
                commit("levels/LOAD_PHASE", state.current.phase);
            })
            .catch(err => console.error(err));
    },
    logOut({ commit }) {
        removeAuthToken()
        commit('REMOVE_TOKEN')
        window.location.replace('/login')
    },
    async changeLang({ commit }, lang) {
        commit("SET_LANGUAGE", lang);
    }
}
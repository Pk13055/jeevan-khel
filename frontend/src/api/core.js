import api from './helper';

export default {
    async getGameState({ code, gender }) {
        let url = `/api/core/new?gender=${gender}`;
        if (code && code != '') url += `&code=${code}`;
        return await api
            .get(url)
            .then(response => response.data)
            .then(state => {
                if (!state.success) throw new Error(state.error);
                return state.data;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    }
}

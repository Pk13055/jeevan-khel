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
    },
    async execAction({ levelId, optionId }) {
        return await api
            .post(`/api/core/update`, {
                body: {
                    level_id: levelId,
                    option_id: optionId
                }
            })
            .then(response => response.data)
            .then(modState => {
                if (!modState.success) throw new Error(modState.error);
                return modState.data;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },
    async updateCosts(finances) {
        return await api
            .post(`/api/core/finances`, {
                body: finances
            })
            .then(response => response.data)
            .then(finances => {
                if (!finances.success) throw new Error(finances.error);
                return finances.data;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    }
}

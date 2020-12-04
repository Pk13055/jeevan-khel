import api from "../../api/core";

const state = () => ({
    remaining: [],
    completed: [],
    phase: 1,
    current: {}
});

const getters = {
    currentLevel: state => {
        return state.current;
    },
    progress: state => {
        return 100 * state.completed.length / (state.completed.length + state.remaining.length);
    },
    availableLevels: state => {
        return state.remaining.filter(level => level.phase == state.phase);
    }
};

const actions = {
    async chooseOption({ commit, dispatch }, { levelId, optionId }) {
        await api
            .execAction({ levelId, optionId })
            .then(state => {
                dispatch("finance/loadState", state.finances, { root: true });
                commit("finance/ADD_INSURANCE", state.insurance, { root: true });
                commit("LOAD_LEVELS", { remaining: state.remaining, completed: state.completed });
                commit("LOAD_LEVEL", state.current);
                commit("LOAD_PHASE", state.current.phase);
                // TODO progress conveyor
            })
            .catch(err => console.error(err));
    }
};

const mutations = {
    LOAD_LEVELS: (state, { remaining, completed }) => {
        state.remaining = remaining;
        state.completed = completed;
    },
    LOAD_PHASE: (state, phase) => {
        state.phase = phase;
    },
    LOAD_LEVEL: (state, level) => {
        state.current = level;
    },
    UNLOAD_LEVEL: (state) => {
        state.current = {};
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
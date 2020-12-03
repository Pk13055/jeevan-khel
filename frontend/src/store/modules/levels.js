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
    async getRandomLevel({ commit, getters }) {
        let possibles = getters.availableLevels;
        // TODO add probability weighting instead of random
        commit("LOAD_LEVEL", possibles[possibles.length * Math.random() | 0]);
    }
};

const mutations = {
    LOAD_LEVELS: (state, { remaining, completed }) => {
        state.remaining = remaining;
        state.completed = completed;
    },
    LOAD_CURRENT: (state, phase) => {
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
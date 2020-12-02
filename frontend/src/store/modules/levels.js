const state = () => ({
    remaining: [],
    completed: [],
    current: 1
});

const getters = {
    //
};

const actions = {
    // TODO add chooseOption action
};

const mutations = {
    LOAD_LEVELS: (state, { remaining, completed }) => {
        state.remaining = remaining;
        state.completed = completed;
    },
    LOAD_CURRENT: (state, { current }) => {
        state.current = current;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
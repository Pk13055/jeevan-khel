const state = () => ({
    insurances: {},
    rates: {},
    costs: {},
});

const getters = {
    // TODO add getters for each property
};

const actions = {
    async loadState({ commit }, finances) {
        const { bank, interest, ...costs } = finances;
        commit("ADD_COSTS", costs);
        commit("ADD_INTEREST", { bank, interest });
    }
};

const mutations = {
    ADD_INSURANCE: (state, insurances) => {
        state.insurances = insurances;
    },
    ADD_INTEREST: (state, rates) => {
        state.rates = rates;
    },
    ADD_COSTS: (state, costs) => {
        state.costs = costs;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
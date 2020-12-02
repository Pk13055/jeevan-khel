import Vue from 'vue';
import Vuex from 'vuex';

import rootActions from "./actions";
import rootMutations from "./mutations";
import finance from "./modules/finance";
import levels from "./modules/levels";

Vue.use(Vuex);
const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
    state: {
        code: null,
        token: null,
        isAuthenticated: false,
        gender: 'female'

    },
    mutations: rootMutations,
    actions: rootActions,
    modules: {
        finance,
        levels,
    },
    strict: debug,
});

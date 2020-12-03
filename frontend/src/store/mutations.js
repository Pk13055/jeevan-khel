// root level mutations

export default {
    SET_CODE: (state, code) => {
        state.code = code;
    },
    ADD_TOKEN: (state, token) => {
        state.token = token;
        state.isAuthenticated = true;
    },
    ADD_GENDER: (state, gender) => {
        state.gender = gender;
    },
    REMOVE_TOKEN: state => {
        state.token = null;
        state.isAuthenticated = false;
    },
    SET_LANGUAGE: (state, lang) => {
        state.language = lang;
    }
};
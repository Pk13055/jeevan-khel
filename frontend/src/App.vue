<template>
    <v-app>
        <v-app-bar app>
            <LanguageSelect />
            <v-chip class="text-overline" color="success" small outlined
                >{{ code }}
                <v-icon small right>mdi-clipboard-outline</v-icon></v-chip
            >
            <v-spacer></v-spacer>
            <v-toolbar-title class="text-h4">जीवन का खेल</v-toolbar-title>

            <v-spacer></v-spacer>
            <v-btn @click="open = !open" text>
                {{ open ? 'Hide Finances' : 'Show Finances' }}
                <v-icon right>
                    {{ open ? 'mdi-chevron-right' : 'mdi-chevron-left' }}
                </v-icon>
            </v-btn>
        </v-app-bar>
        <Login v-if="!isAuthenticated" />
        <Finance :open="open" />
        <v-main>
            <router-view></router-view>
        </v-main>
        <Footer />
    </v-app>
</template>

<script>
import { mapState } from 'vuex';

import Finance from './components/Finance';
import Footer from './components/Footer';
import Login from './components/Login';
import LanguageSelect from './components/LanguageSelect';

export default {
    name: 'App',
    components: { Finance, Footer, Login, LanguageSelect },
    data: () => ({
        open: false,
        items: [
            { title: 'Click Me' },
            { title: 'Click Me' },
            { title: 'Click Me' },
            { title: 'Click Me 2' },
        ],
    }),
    computed: {
        ...mapState({
            isAuthenticated: state => state.isAuthenticated,
            code: state => state.code,
        }),
    },
};
</script>

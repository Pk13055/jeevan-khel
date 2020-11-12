<template>
    <v-app>
        <v-app-bar app>
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
        <Finance :open="open" />
        <v-main>
            <router-view></router-view>
        </v-main>

        <Footer />
    </v-app>
</template>

<script>
import Finance from './components/Finance';
import Footer from './components/Footer';
export default {
    name: 'App',
    components: { Finance, Footer },
    data: () => ({
        open: true,
    }),
};
</script>

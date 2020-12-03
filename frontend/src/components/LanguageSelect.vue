<template>
    <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="primary"
                large
                outlined
                class="mx-4 text-h5"
                dark
                v-bind="attrs"
                v-on="on"
            >
                <v-icon left>mdi-translate</v-icon> {{ labels[lang] }}
            </v-btn>
        </template>
        <v-list>
            <v-list-item-group>
                <v-list-item
                    v-for="language in languages"
                    :key="language.key"
                    @click="changeLanguage(language.key)"
                >
                    <v-list-item-title>{{ language.label }}</v-list-item-title>
                </v-list-item>
            </v-list-item-group>
        </v-list>
    </v-menu>
</template>
<script>
import { mapState } from 'vuex';
export default {
    name: 'LanguageSelect',
    data: () => ({
        languages: [
            {
                label: 'English',
                key: 'EN',
            },
            {
                label: 'हिंदी',
                key: 'HI',
            },
        ],
        labels: {
            HI: 'भाषा',
            EN: 'Language',
        },
    }),
    methods: {
        async changeLanguage(lang) {
            await this.$store.dispatch('changeLang', lang);
        },
    },
    computed: {
        ...mapState({
            lang: state => state.language,
        }),
    },
};
</script>
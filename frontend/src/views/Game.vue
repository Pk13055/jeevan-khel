<template>
    <v-container fluid>
        <v-row>
            <Level />
        </v-row>
        <Conveyor :loc="loc" />
    </v-container>
</template>

<script>
import { mapState } from 'vuex';

import Level from '../components/Level.vue';
import Conveyor from '../components/Conveyor.vue';
export default {
    // NOTE: 126ca896-d677-4bf9-9460-a9a08edb3d91
    name: 'Game',
    components: { Level, Conveyor },
    data: () => ({
        loc: 0,
        level: {},
    }),
    computed: {
        ...mapState('levels', {
            phase: state => state.phase,
        }),
        gender() {
            return this.$store.state.gender;
        },
    },
    methods: {
        currentTile(id) {
            console.log(`clicked ${id}!`);
        },
    },
};
</script>

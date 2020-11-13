<template>
    <v-container fluid>
        <v-row>
            <Level :data="level" />
        </v-row>
        <Conveyor :loc="loc" />
    </v-container>
</template>

<script>
import Level from '../components/Level.vue';
import Conveyor from '../components/Conveyor.vue';
export default {
    name: 'Game',
    components: { Level, Conveyor },
    data: () => ({
        loc: 0,
        level: {
            id: 'some id',
            description: 'lorem ipsum',
        },
    }),
    created() {
        setInterval(() => {
            this.loc = this.loc < 8 ? this.loc + 1 : 0;
        }, 4000);
    },
    methods: {
        currentTile(id) {
            console.log(`clicked ${id}!`);
        },
    },
};
</script>

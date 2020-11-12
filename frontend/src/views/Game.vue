<template>
    <v-container fluid>
        <v-row>
            <Level :data="level" />
        </v-row>
        <v-row justify="start">
            <v-spacer v-for="id in Array(this.loc)" :key="id"></v-spacer>
            <div class="spacing">
                <v-img
                    :src="require('../assets/boy.png')"
                    height="100"
                    contain
                />
            </div>
            <v-spacer v-for="id in Array(8 - this.loc)" :key="id"></v-spacer>
        </v-row>
        <v-row justify="space-around">
            <div
                v-for="id in Array(8)
                    .fill()
                    .map((x, i) => i)"
                :key="id"
                @click="currentTile(id)"
                :id="id"
                class="tile"
            ></div>
        </v-row>
    </v-container>
</template>

<script>
import Level from '../components/Level.vue';
export default {
    name: 'Game',
    components: { Level },
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
<style scoped>
.spacing {
    margin-left: 1%;
    margin-right: 1%;
    padding-left: 4%;
    width: auto;
    padding-right: 4%;
}
.tile {
    padding-left: 4%;
    padding-right: 4%;
    padding-top: 2%;
    padding-bottom: 2%;
    margin-left: 1%;
    margin-right: 1%;
    height: 50%;
    width: 10%;
    background-color: grey;
    transform: skewX(-20deg);
    -ms-transform: skewX(-20deg);
    -webkit-transform: skewX(-20deg);
}
</style>

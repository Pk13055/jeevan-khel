<template>
    <v-sheet
        color="yellow"
        rounded="xl"
        class="lighten-3 ma-4 pa-3 elevation-8"
    >
        <v-row justify="center">
            <v-col class="text-center">
                <h2>Phase - {{ phase }}</h2>
            </v-col>
        </v-row>
        <v-row justify="start" class="mb-0">
            <v-spacer v-for="id in Array(this.loc)" :key="id"></v-spacer>
            <div class="spacing">
                <v-img
                    :src="
                        require('../assets/images/conveyor/' +
                            gender +
                            '-' +
                            phase +
                            '.png')
                    "
                    height="100"
                    contain
                />
            </div>
            <v-spacer v-for="id in Array(8 - this.loc)" :key="id"></v-spacer>
        </v-row>
        <v-row justify="space-around" class="mt-0">
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
        <v-row>
            <v-progress-linear
                color="orange"
                buffer-value="0"
                :value="progress"
                stream
            ></v-progress-linear>
        </v-row>
    </v-sheet>
</template>
<script>
import { mapState } from 'vuex';
export default {
    name: 'Conveyor',
    data: () => ({
        //
    }),
    computed: {
        ...mapState('levels', ['phase', 'progress', 'loc']),
        ...mapState(['gender']),
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
    transform: skewX(-20deg);
    -ms-transform: skewX(-20deg);
    -webkit-transform: skewX(-20deg);
    background: radial-gradient(
                circle farthest-side at 0% 50%,
                #fb1 23.5%,
                rgba(240, 166, 17, 0) 0
            )
            21px 30px,
        radial-gradient(
                circle farthest-side at 0% 50%,
                #b71 24%,
                rgba(240, 166, 17, 0) 0
            )
            19px 30px,
        linear-gradient(
                #fb1 14%,
                rgba(240, 166, 17, 0) 0,
                rgba(240, 166, 17, 0) 85%,
                #fb1 0
            )
            0 0,
        linear-gradient(
                150deg,
                #fb1 24%,
                #b71 0,
                #b71 26%,
                rgba(240, 166, 17, 0) 0,
                rgba(240, 166, 17, 0) 74%,
                #b71 0,
                #b71 76%,
                #fb1 0
            )
            0 0,
        linear-gradient(
                30deg,
                #fb1 24%,
                #b71 0,
                #b71 26%,
                rgba(240, 166, 17, 0) 0,
                rgba(240, 166, 17, 0) 74%,
                #b71 0,
                #b71 76%,
                #fb1 0
            )
            0 0,
        linear-gradient(90deg, #b71 2%, #fb1 0, #fb1 98%, #b71 0%) 0 0 #fb1;
    background-size: 40px 60px;
}
</style>

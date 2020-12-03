<template>
    <v-container>
        <v-row>
            <v-col>
                <h3 class="text-h3">{{ data.title }}</h3>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-img
                    max-height="500"
                    max-width="1000"
                    contain
                    :src="require('../assets/images/events/' + data.image)"
                ></v-img>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col class="text-center">
                <p class="text-h4">
                    {{ data.description[language] }}
                </p>
                <audio controls>
                    <source
                        :src="
                            require('../assets/audio/desc/' + data.audio['HI'])
                        "
                        type="audio/mp3"
                    />
                    Your browser does not support the audio element.
                </audio>
            </v-col>
        </v-row>
        <v-row>
            <v-col
                v-for="option in data.options"
                :key="option.id"
                class="text-center"
            >
                <p>
                    <v-btn
                        large
                        block
                        @click="chooseOption(option)"
                        :color="colors[option.id]"
                        outlined
                        class="text-h5"
                    >
                        <span class="text-subtitle" v-if="language == 'EN'">
                            {{ option.description }}
                        </span>
                        <span class="text-subtitle" v-else>
                            {{ option.translation[language] }}
                        </span>
                    </v-btn>
                </p>
                <audio controls>
                    <source
                        :src="
                            require('../assets/audio/options/event_' +
                                data.id +
                                '_option_' +
                                option.id +
                                '.mp3')
                        "
                        type="audio/mp3"
                    />
                    Your browser does not support the audio element.
                </audio>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import { mapGetters, mapState } from 'vuex';
export default {
    name: 'Level',
    data: () => ({
        colors: ['red', 'teal', 'green', 'blue'],
    }),
    methods: {
        async chooseOption(option) {
            // TODO fire action to register option selection
            // TODO update state on action execution
            // TODO progress next level
            console.log(option.id);
            const { action } = option;
            console.log(action);
        },
    },
    computed: {
        ...mapState({
            language: state => state.language,
        }),
        ...mapGetters({
            data: 'levels/currentLevel',
        }),
    },
};
</script>
<template>
    <v-overlay>
        <v-card class="mx-auto" outlined>
            <v-card-text>
                <v-card-title>Jeevan Khel - Login</v-card-title>
                <v-container fluid>
                    <v-row>
                        <v-col>
                            <v-text-field
                                outlined
                                v-model="code"
                                label="Game Code"
                                append-outer-icon="mdi-barcode-scan"
                                hint="Leave blank to start a new game"
                                persistent-hint
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col>Gender</v-col>
                        <v-col>
                            <v-btn-toggle v-model="genderIdx" mandatory shaped>
                                <v-btn x-large>
                                    <v-icon left x-large>
                                        mdi-human-female
                                    </v-icon>
                                    Female
                                </v-btn>
                                <v-btn x-large>
                                    <v-icon left x-large>mdi-human-male</v-icon>
                                    Male
                                </v-btn>
                            </v-btn-toggle>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>
            <v-card-actions>
                <v-btn
                    outlined
                    rounded
                    block
                    @click="startGame({ code: code, gender: gender })"
                >
                    Start Game
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-overlay>
</template>
<script>
import { mapActions } from 'vuex';
export default {
    name: 'Login', 
    data: () => ({
        genderIdx: 0,
        code: '',
    }),
    methods: {
        ...mapActions(['startGame']),
    },
    computed: {
        gender() {
            return ['female', 'male'][this.genderIdx];
        },
    },
};
</script>
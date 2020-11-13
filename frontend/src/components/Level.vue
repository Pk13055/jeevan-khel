<template>
    <v-container>
        <v-row>
            <v-col> Level - {{ id }} </v-col>
        </v-row>
        <v-row>
            <v-col>
                
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
export default {
    name: 'Level',
    props: ['data'],
    data: () => ({
        //
    }),
};
</script>
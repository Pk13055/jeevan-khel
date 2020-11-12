<template>
    <v-footer app>
        <v-col class="text-center" cols="6">
            {{ new Date().getFullYear() }} — All rights reserved &copy;
            <strong></strong>
        </v-col>
        <v-col class="text-center" cols="6">
            <strong>Game Design &amp; Engineering</strong> - International
            Institute of Information Technology, Hyderabad
        </v-col>
    </v-footer>
</template>
<script>
export default {
    name: 'Footer',
};
</script>
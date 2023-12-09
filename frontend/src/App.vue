<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <router-link class="navbar-brand" to="/">Vue Router Example</router-link>

            <div class="navbar-nav d-flex">
                <router-link class="nav-link me-3" to="/" exact>Main Page</router-link>
                <router-link class="nav-link" to="/other">Other Page</router-link>
            </div>
        </div>
    </nav>
    <main class="container pt-4">
        <RouterView class="flex-shrink-0" />
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";

export default defineComponent({
    components: { RouterView },
});

</script>

<style scoped></style>

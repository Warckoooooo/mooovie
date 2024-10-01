<template>
  <div class="min-h-screen bg-gradient-to-r from-blue-500 to-purple-600">
    <MovieList />
  </div>
</template>

<script>
import MovieList from './components/MovieList.vue';

export default {
  components: {
    MovieList,
  },
};
</script>

<template>
  <div class="movie-card cursor-pointer transition-transform transform hover:scale-105" @click="showMovieDetails">
    <img :src="getMoviePoster(movie.poster_path)" alt="Movie Poster" class="w-full h-auto rounded-lg shadow-md">
  </div>
</template>

<script>
export default {
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {

    getMoviePoster(path) {
      return `https://image.tmdb.org/t/p/w500/${path}`;
    },

    showMovieDetails() {
      this.$emit('select', this.movie);
    },
  }
};
</script>

<style scoped>
.movie-card {
  max-width: 200px;
}
</style>

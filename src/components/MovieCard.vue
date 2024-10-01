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
    // Méthode pour générer l'URL de l'affiche du film
    getMoviePoster(path) {
      return `https://image.tmdb.org/t/p/w500/${path}`;
    },
    // Méthode pour afficher plus de détails sur le film
    showMovieDetails() {
      this.$emit('select', this.movie); // Emet l'événement 'select' avec l'objet movie
    },
    // Méthode pour formater la date de sortie
    formatReleaseDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString('fr-FR', options);
    }
  }
};
</script>

<style scoped>
.movie-card {
  max-width: 200px;
}
</style>

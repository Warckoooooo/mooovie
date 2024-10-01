<template>
  <div class="container mx-auto p-4">
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
      <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          @select="selectMovie"
          class="flex-shrink-0"
      />
    </div>
    <MovieModal
        v-if="selectedMovie"
        :movie="selectedMovie"
        @close="selectedMovie = null"
    />
  </div>
</template>

<script>
import axios from 'axios';
import MovieCard from './MovieCard.vue';
import MovieModal from './MovieModal.vue';

export default {
  data() {
    return {
      movies: [],
      selectedMovie: null,
    };
  },
  methods: {
    async fetchMovieById(movieId) {
      try {
        const response = await axios.get(
            `https://api.themoviedb.org/3/movie/${movieId}?api_key=${process.env.VUE_APP_TMDB_API_KEY}`
        );
        return response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération du film:', error);
        return null;
      }
    },

    async fetchRandomMovies(count) {
      const movies = [];
      for (let i = 0; i < count; i++) {
        const movieId = Math.floor(Math.random() * 128188) + 1; // Générer un ID aléatoire
        const movie = await this.fetchMovieById(movieId);
        if (movie) {
          movies.push(movie);
        }
      }
      this.movies = movies;
    },

    calculateNumberOfMovies() {
      const width = window.innerWidth; // Obtenir la largeur de la fenêtre
      const cardWidth = 200; // Largeur estimée d'une carte en pixels (ajustez si nécessaire)
      const count = Math.floor(width / cardWidth); // Calculer le nombre de films à afficher
      return count > 0 ? count : 1; // Retourner au moins 1 film
    },

    async getMovies() {
      const numberOfMovies = this.calculateNumberOfMovies();
      await this.fetchRandomMovies(numberOfMovies);
    },

    selectMovie(movie) {
      this.selectedMovie = movie;
    },
  },
  mounted() {
    this.getMovies(); // Appeler la méthode pour récupérer les films lors du montage du composant
  },
  components: {
    MovieCard,
    MovieModal,
  },
};
</script>

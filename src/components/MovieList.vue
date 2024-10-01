<template>
  <div class="container mx-auto p-4">
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-2">
      <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          @select="selectMovie"
          class="animate__animated animate__fadeIn"
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
      while (movies.length < count) {
        const movieId = Math.floor(Math.random() * 128188) + 1; // ID aléatoire
        const movie = await this.fetchMovieById(movieId);
        if (movie && !movie.adult) { // Vérifie si le film n'est pas pour adultes
          movies.push(movie);
        }
      }
      this.movies = movies;
    },

    async getMovies() {
      const numberOfMovies = 24;
      await this.fetchRandomMovies(numberOfMovies);
    },

    selectMovie(movie) {
      this.selectedMovie = movie;
    },
  },
  mounted() {
    this.getMovies();
  },
  components: {
    MovieCard,
    MovieModal,
  },
};
</script>

<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white p-8 rounded-lg shadow-lg relative max-w-lg mx-auto">
      <button class="absolute top-2 right-2 text-black" @click="$emit('close')">❌</button>
      <img :src="getMoviePoster(movie.poster_path)" alt="Movie Poster" class="w-full rounded mb-4">
      <h2 class="text-2xl font-bold mb-2">{{ movie.title }}</h2>
      <p class="mb-2"><strong>Summary:</strong> {{ movie.overview }}</p>
      <p><strong>Release Date:</strong> {{ movie.release_date }}</p>
      <p><strong>Rating:</strong> {{ movie.vote_average }}/10</p>
      <p><strong>Genres:</strong> {{ movie.genres.map(genre => genre.name).join(', ') }}</p>
      <p><strong>Runtime:</strong> {{ movie.runtime }} minutes</p>
      <p><strong>Language:</strong> {{ movie.original_language.toUpperCase() }}</p>
      <p><strong>Budget:</strong> ${{ movie.budget.toLocaleString() }}</p>
      <p><strong>Revenue:</strong> ${{ movie.revenue.toLocaleString() }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getMoviePoster(path) {
      return `https://image.tmdb.org/t/p/w500/${path}`;
    },
  },
};
</script>

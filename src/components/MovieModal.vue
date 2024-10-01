<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white p-8 rounded-lg shadow-lg relative max-w-lg mx-auto">
      <button class="absolute top-2 right-2 text-black" @click="$emit('close')">❌</button>
      <img :src="getMoviePoster(movie.poster_path)" alt="Movie Poster" class="w-full rounded mb-4">
      <h2 class="text-2xl font-bold mb-2">{{ movie.title }}</h2>
      <p class="mb-2"><strong>Résumé :</strong> {{ movie.overview }}</p>
      <p><strong>Date de sortie :</strong> {{ movie.release_date }}</p>
      <p><strong>Note :</strong> {{ movie.vote_average }}/10</p>
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

<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-base-100 p-8 rounded-lg shadow-lg relative max-w-lg mx-auto flex">
      <button class="absolute top-2 right-2 btn btn-circle btn-sm" @click="$emit('close')">
        ❌
      </button>

      <img
          :src="getMoviePoster(movie.poster_path)"
          alt="Movie Poster"
          class="h-2/3 w-2/3 rounded mr-4"
      />

      <div class="flex-1">
        <h2 class="text-2xl font-bold mb-2">{{ movie.title }}</h2>

        <div class="stats shadow mb-4">
          <div class="stat">
            <div class="stat-title">Rating</div>
            <div class="stat-value">{{ movie.vote_average }}/10</div>
          </div>
        </div>

        <p class="mb-2"><strong>Summary:</strong> {{ movie.overview }}</p>
        <p><strong>Release Date:</strong> {{ movie.release_date }}</p>
        <p><strong>Genres:</strong> {{ movie.genres.map(genre => genre.name).join(', ') }}</p>
        <p><strong>Runtime:</strong> {{ movie.runtime }} minutes</p>
        <p><strong>Language:</strong> {{ movie.original_language.toUpperCase() }}</p>
      </div>
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

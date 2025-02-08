<template>
  <div>
    <h2>Blog Posts</h2>
    <div v-for="post in posts" :key="post.id">
      <h3>{{ post.title }}</h3>
      <p>{{ post.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
    };
  },
  async created() {
    const response = await axios.get("http://127.0.0.1:8000/posts/");
    this.posts = response.data;
  },
};
</script>

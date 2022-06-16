<template>


    <br />
  <br />
  <br />
  <button @click="fetchData">Github</button>
</template>

<script>
import { ref, computed, onMounted } from "vue";

export default {
  name: 'Repos',
  props: {
  },
  setup() {
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);

     

    onMounted(() => {
  //    fetchData();
    });

    return {
      data,
      loading,
      error
    };
  },

    methods: {


     fetchData() {
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);

  loading.value = true;
  // I prefer to use fetch
  // you can use use axios as an alternative
  return fetch('https://api.github.com/users/JeffRice/repos', {
    method: 'get',
    headers: {
      'content-type': 'application/json'
    }
  })
    .then(res => {


      // a non-200 response code
      if (!res.ok) {
        // create error instance with HTTP status text
        const error = new Error(res.statusText);
              
        error.json = res.json()
        console.log(error.json)
        throw error;
      }

        console.log(res.json)
        return res.json();
    })
    .then(json => {
      // set the response data
      data.value = json.data;
      console.log(data.value);
        const obj = JSON.parse(data.value)
        console.log(obj)

    })
    .catch(err => {
      error.value = err;
      // In case a custom JSON error response was provided
      if (err.json) {
        return err.json.then(json => {
          // set the JSON response message
          error.value.message = json.message;
        });
      }
    })
    .then(() => {
      loading.value = false;
    });
} 

   }
}
</script>
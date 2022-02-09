<template>
  <div id="app">

    <form @submit.prevent="submitFile">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="file.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="Description" v-model="file.description">
        <input type="date" class="form-control col-3 mx-2" placeholder="Date" v-model="file.date_added">
        <button class="btn btn-success">Submit</button>
      </div>

    </form>



    <table class="table">
      <thead>
        <th>Name</th>
        <th>Description</th>
        <th>Date added</th>
      </thead>
      <tbody>
        <tr v-for="file in files" :key="file.id" @dblclick="$data.file = file">
          <td>{{ file.name }}</td>
          <td>{{ file.description }}</td>
          <td>{{ file.date_added }}</td>
          <td><button class="btn btn-outline-danger btn-sm mx-1" @click="deleteFile(file)">x</button></td>
        </tr>
      </tbody>
    </table>
  </div>


  <div>
    <file-upload />
  </div>
</template>

<script>
import FileUpload from '../src/components/file-upload.vue';

export default {
  name: "App",
  data() {
    return {
      file: {
        'name': '',
        'description': '',
        'date_added': '',
      },
      files: []
    };
  },
  async created(){
    await this.getFiles();
  },

  methods: {
    submitFile(){
      if (this.file.id === undefined){
        this.createFile();
      } else {
        this.editFile();
      }
    },

    async getFiles(){
      var response = await fetch('http://localhost:8000/api/files/')
      this.files = await response.json()
    },

    async createFile(){
      await this.getFiles();

      await fetch('http://localhost:8000/api/files/', {
        method: 'post',
        headers: {
          'Content-Type' : 'application/json'
        },
        body: JSON.stringify(this.file)
      });
      await this.getFiles();
    },

    async editFile(){
      await this.getFiles();

      await fetch(`http://localhost:8000/api/files/${this.file.id}/`, {
        method: 'put',
        headers: {
          'Content-Type' : 'application/json'
        },
        body: JSON.stringify(this.file)
      });
      await this.getFiles();
      this.file = {};
    },

    async deleteFile(file){
      await this.getFiles();

      await fetch(`http://localhost:8000/api/files/${file.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type' : 'application/json'
        },
        body: JSON.stringify(this.file)
      });
      await this.getFiles();
    }
  }
  ,
  components: { FileUpload }


};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

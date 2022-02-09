<template>
    <div class="formdiv">
    <h4>Remove trailing whitespace</h4>
    <form enctype="multipart/form-data" class="form" @submit.prevent="sendFile">
        <!-- <div class="field">
            <label for="file" class="label">Upload File</label>
            <input 
                type="file" 
                ref="file"
                @change="selectFile"
            />
        </div> -->
    <div class="file is-boxed is-primary">
        <label class="file-label">
            <input
                type="file"
                ref="file"
                @change="selectFile"
                class="file-input"
            />

            <span class="file-cta">
                <span class="file-icon">
                    <i class="fas fa-upload"></i>
                </span>
            </span>
        </label>
    </div>

    <div class="field">
        <button class="button is-info">Send</button>
    </div>
    </form>
</div>
</template>

<script>
import axios from 'axios';
export default {
    name: "FileUpload",

    data(){
        return {
            file: ""
        }
    },

    methods: {
        selectFile(){
            this.file = this.$refs.file.files[0];
        },


        async sendFile(){
            const formData = new FormData();
            formData.append('file', this.file);
            try{
                await axios.post('http://localhost:8000/api/files/upload/', formData);
            } catch(error){
                console.log(error);
            }
        }
    },

    


}
</script>

<style>
.formdiv{
    padding-top:20%;
}
</style>
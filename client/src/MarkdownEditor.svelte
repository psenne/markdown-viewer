<script>
   	const axios = require('axios');
    export let docInfo = null

    let text = "";
    let uuid = "";

    if(docInfo){
        text = docInfo.text
        uuid = docInfo.uuid
    }

    function SaveText(){
        axios.patch(`/api/document/${uuid}`, {
            text: text,
            userID: 1
        });
    }
</script>

<style>
    div.md-editor {
        border: 1px solid red;
    }
</style>

<div class="md-editor">
    <textarea class="editor" bind:value={text} placeholder="Add your markdown here"></textarea>
    <div>
    <button on:click={SaveText}>Save</button>
    </div>
</div>
<script>
   	const axios = require('axios');
    // import MarkdownEditor from "./MarkdownEditor.svelte"
    // import MarkdownViewer from "./MarkdownViewer.svelte"

    export let params = {};
    const uuid = params.uuid;
    let text = "";

    $: document = GetDocumentByUUID(params.uuid);
    $: text = document.text;

    function SaveText(){
        axios.patch(`/api/document/${uuid}`, {
            text: text,
            userID: 1
        });
    }
    
	async function GetDocumentByUUID(uuid){
		try {
            const data = await axios.get(`/api/document/${uuid}`);
			return data.data;
		}
		catch(e){
            axios.post(`/api/document/${uuid}`, {
                uuid: uuid,
                userID: 1
            });
            return "";
		}
    }

    
</script>

<style>
    div.md-editor {
        border: 1px solid red;
    }
</style>


{@debug text,document}
{#await document then docInfo}
    <div class="md-editor">
        <textarea class="editor" bind:value={text} placeholder="Add your markdown here"></textarea>
        <div>
        <button on:click={SaveText}>Save</button>
        </div>
    </div>
    <div class="md-viewer">
        {#if docInfo.text}
            {@html docInfo.text}
        {/if}
    </div>
{/await}
<script>
    import {marked} from 'marked'
    export let docInfo = null

    console.log(docInfo)
</script>

<div class="md-viewer">
    {#if docInfo.text}
        {@html docInfo.text}
    {/if}
</div>
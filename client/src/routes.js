import Home from './Home.svelte'
import MarkdownPage from './MarkdownPage.svelte'
import MarkdownViewer from './MarkdownViewer.svelte'
import NotFound from './NotFound.svelte'

export const routes = {
    "/:uuid/edit": MarkdownPage,
    "/:uuid": MarkdownViewer,
    "/": Home,
    "*": NotFound
}
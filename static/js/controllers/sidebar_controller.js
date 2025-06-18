import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"

export default class extends Controller {
    static targets = ["panel"]

    toggle() {
        this.panelTarget.classList.toggle("-translate-x-full")
    }
}
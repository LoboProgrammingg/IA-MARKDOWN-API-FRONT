import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"

export default class extends Controller {
    static targets = ["menu"]

    connect() {
        this.boundHide = this.hide.bind(this)
    }

    toggle() {
        this.menuTarget.classList.toggle("hidden")
    }

    hide(event) {
        if (!this.element.contains(event.target)) {
            this.menuTarget.classList.add("hidden")
        }
    }
}
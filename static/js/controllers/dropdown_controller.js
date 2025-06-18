import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"

// Conecta-se ao data-controller="dropdown"
export default class extends Controller {
    static targets = ["menu"]

    connect() {
        this.boundHide = this.hide.bind(this)
        document.addEventListener("click", this.boundHide)
    }

    disconnect() {
        document.removeEventListener("click", this.boundHide)
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
import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"

// Conecta-se ao data-controller="theme"
export default class extends Controller {
    static targets = ["darkIcon", "lightIcon"]

    connect() {
        this.updateIcons()
    }

    toggle() {
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.remove('dark')
            localStorage.setItem('color-theme', 'light')
        } else {
            document.documentElement.classList.add('dark')
            localStorage.setItem('color-theme', 'dark')
        }
        this.updateIcons()
    }

    updateIcons() {
        if (document.documentElement.classList.contains('dark')) {
            this.lightIconTarget.classList.remove('hidden')
            this.darkIconTarget.classList.add('hidden')
        } else {
            this.lightIconTarget.classList.add('hidden')
            this.darkIconTarget.classList.remove('hidden')
        }
    }
}
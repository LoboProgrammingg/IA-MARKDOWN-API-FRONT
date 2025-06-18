import "./controllers/application.js"
import Dropdown from "./controllers/dropdown_controller.js"
import Sidebar from "./controllers/sidebar_controller.js"
import Theme from "./controllers/theme_controller.js"

Stimulus.register("dropdown", Dropdown)
Stimulus.register("sidebar", Sidebar)
Stimulus.register("theme", Theme)
# Pavel Švec

Desktopové nástroje, embedded hardware a utilitky pro Linux/KDE.
*Desktop tools, embedded hardware and Linux/KDE utilities — mostly in Czech.*

## Veřejné projekty

### [Svec Studio Fedora theme](https://github.com/pauliquib/svec-studio-fedora-theme)
Sada nástrojů pro vzhled Fedory s KDE Plasma 6 v jednom repozitáři. Každá část je samostatná:

- **Panel & Window Colours** — nativní nastavení (KCM) pro barvy panelu, záhlaví oken, okraje, stíny a uložené motivy s živým náhledem (`colors/`)
- **Outline Icons** — obrysová sada ikon, varianta Accent se přebarvuje podle Plasma akcentní barvy, plus pevné White a Black (`icons/`, Python, freedesktop)
- **Expanding Icons Task Manager** — správce úloh jen s ikonami; ikona pod kurzorem se plynule rozbalí do štítku s názvem okna a sousední ikony uhnou do stran. Je to port lišty aplikací z hlavičky svec-elektro.cz. Ikony i popisky zůstávají čitelné na jakémkoli pozadí díky kontrastnímu obrysu z vlastního shaderu (`taskbar/`, QML, GLSL, KDE Plasma 6 widget)
- **Plasma Search Bar** — command palette in the KDE panel, VS Code style: live KRunner results and prefix modes (`>` terminal, `/` files, `:` system actions, `!` web, `?` help), aliases, recent items and configurable features (QML, KDE Plasma 6 widget) (`search-bar/`)

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/icons"><img src="assets/thumbs/svec-studio-iconpack-screenshots-white-on-dark.webp" width="100%" alt="Outline Icons"></a></td>
<td width="33%" valign="top">
<a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/taskbar"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/taskbar/docs/screenshots/hover-label.png" width="100%" alt="Taskbar: hover label"></a><br>
<a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/taskbar"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/taskbar/docs/screenshots/light-background.png" width="100%" alt="Taskbar: light background"></a><br>
<a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/taskbar"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/taskbar/docs/screenshots/accent-color.png" width="100%" alt="Taskbar: accent colour"></a>
<a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/search-bar"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/search-bar/docs/screenshots/dark-theme.png" width="100%" alt="Search Bar: dark theme"></a><br>
<a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/search-bar"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/search-bar/docs/screenshots/light-theme.png" width="100%" alt="Search Bar: light theme"></a>
</td>
<td width="33%" valign="top"><a href="https://github.com/pauliquib/svec-studio-fedora-theme/tree/main/colors"><img src="https://raw.githubusercontent.com/pauliquib/svec-studio-fedora-theme/main/colors/docs/screenshots/panel-window-colours.png" width="100%" alt="Panel &amp; Window Colours"></a></td>
</tr>
</table>

### [Stone & Clay](https://github.com/pauliquib/stone-and-clay)
Open-world simulátor vesnice Dukelčice nad reálným katastrem — NPC dialogy, práce, dovednosti, počasí, zvěř, létání (Godot 4.3, GDScript)

<a href="https://github.com/pauliquib/stone-and-clay"><img src="assets/thumbs/stone-and-clay-dron-ves.webp" width="49%"></a>
<a href="https://github.com/pauliquib/stone-and-clay"><img src="assets/thumbs/stone-and-clay-javor-kyvacka.webp" width="49%"></a>

### [HardCore Mode](https://github.com/pauliquib/HardCoreMode)
Plošinovková hra běžící čistě v prohlížeči (vanilla JS, Canvas, Web Audio API), vlastní editor map

<a href="https://github.com/pauliquib/HardCoreMode"><img src="https://raw.githubusercontent.com/pauliquib/HardCoreMode/main/docs/screenshots/game.jpg" width="32%"></a>
<a href="https://github.com/pauliquib/HardCoreMode"><img src="https://raw.githubusercontent.com/pauliquib/HardCoreMode/main/docs/screenshots/sectors.jpg" width="32%"></a>
<a href="https://github.com/pauliquib/HardCoreMode"><img src="https://raw.githubusercontent.com/pauliquib/HardCoreMode/main/docs/screenshots/editor.jpg" width="32%"></a>

### [InfoFlowLab](https://github.com/pauliquib/infoflowlab)
Interaktivní simulátor komprese a komunikace — vizuální editor uzlů se simulací toku dat v reálném čase (Python, PySide6)

<a href="https://github.com/pauliquib/infoflowlab"><img src="assets/thumbs/infoflowlab-screenshot.webp" width="70%"></a>

### [Vlnky](https://github.com/pauliquib/Vlnky)
KDE Plasma 6 wallpaper renderující animované PSP XMB vlny z `system_plugin_bg.rco` souborů (C++, Vulkan/OpenGL RHI)

<a href="https://github.com/pauliquib/Vlnky"><img src="https://raw.githubusercontent.com/pauliquib/Vlnky/main/docs/screenshots/vlna-ps2.jpg" width="49%"></a>
<a href="https://github.com/pauliquib/Vlnky"><img src="https://raw.githubusercontent.com/pauliquib/Vlnky/main/docs/screenshots/vlna-sony.jpg" width="49%"></a>

### [Fedora-SecuriTUI](https://github.com/pauliquib/Fedora-SecuriTUI)
TUI správce diagnostických, bezpečnostních a pentest nástrojů pro Fedora KDE (bash, whiptail/dialog)

<a href="https://github.com/pauliquib/Fedora-SecuriTUI"><img src="https://raw.githubusercontent.com/pauliquib/Fedora-SecuriTUI/main/docs/screenshots/fedora-stui-main.png" width="49%"></a>
<a href="https://github.com/pauliquib/Fedora-SecuriTUI"><img src="https://raw.githubusercontent.com/pauliquib/Fedora-SecuriTUI/main/docs/screenshots/fedora-stui-recon.png" width="49%"></a>

## Privátní projekty

Interní / neveřejné repozitáře — kód, konfigurace a interní dokumentace zůstávají soukromé.
Stručný přehled bez citlivých detailů (bez credentials, interních IP adres, zákaznických dat apod.):

### Sencurio
Monorepo pro asistované bydlení a bezpečnostní přehled v domácnosti (AAL / smart home): mmWave radar + ESP32-S3 edge zařízení, Laravel backend, Next.js dashboard, Expo mobilní app a PySide6 desktop monitor. *Není značkováno jako zdravotnický prostředek.*
`PHP/Laravel` `TypeScript/Next.js` `Python/PySide6` `ESP-IDF` `MQTT`

<img src="assets/thumbs/sencurio-device-exploded.webp" width="49%"> <img src="assets/thumbs/sencurio-floorplan3d-dark.webp" width="49%">

### Svec Studio
Desktopové GUI/TUI pracovní prostředí pro Fedoru: kiosk shell (Wayland), plugin API, lokální AI agent, správa statického webu svec-elektro.cz. Nástroj pro vlastní denní provoz, ne produkt pro distribuci.
`Python` `PySide6/Qt` `JavaScript` `Rust`

<img src="assets/thumbs/svec-studio-splash.webp" width="24%"> <img src="assets/thumbs/svec-studio-desktop.webp" width="24%"> <img src="assets/thumbs/svec-studio-tui-os.webp" width="24%"> <img src="assets/thumbs/svec-studio-pdf-viewer.webp" width="24%">

### PRE2MULTI
Nezávislý multiplayer engine (Godot 4) nad fyzikou klasické DOS plošinovky, LAN deathmatch pro 2–4 hráče. *BYOG (Bring Your Own Game)* — repozitář neobsahuje originální herní assety.
`GDScript` `Python`

<img src="assets/thumbs/pre2multi-arena.webp" width="70%">

### K3X020 Nucleo
STM32 Nucleo-H753ZI jako náhradní řídicí jednotka průmyslové 24V I/O desky — reverse engineering hardwaru pro vlastní dílnu, dokumentace svorek a RE nálezů.
`C` `STM32 HAL`

<img src="assets/thumbs/k3x020-pcb-horni.webp" width="49%"> <img src="assets/thumbs/k3x020-pcb-spodni.webp" width="49%">

## Jazyky

Souhrn přes **všechny** repozitáře, veřejné i privátní (`stone-and-clay`, `HardCoreMode`, `infoflowlab`, `Vlnky`, `Fedora-SecuriTUI`, `plasma-search-bar`, `k3x020-nucleo`, `svec-studio`, `PRE2MULTI`, `sencurio-developer`) podle bajtů kódu dle GitHubu — žádný obsah souborů. Vendor knihovny a third-party addony (STM32 HAL/CMSIS, ESP-IDF managed components, Godot addony, Three.js/floorplan3d JS knihovny) jsem vyřadil pomocí `.gitattributes` (`linguist-vendored`), ať graf odpovídá skutečně napsanému kódu, ne nalinkovaným SDK a pluginům:

![Jazyky — veřejné i privátní](assets/projects/languages-all.png)

## Technologie

`Python` `JavaScript / TypeScript` `Rust` `PySide6 / Qt` `C++` `GDScript` `Bash` `STM32 / ESP32` `Godot` `Laravel` `Next.js`

🌐 **Web:** [svec-elektro.cz](https://svec-elektro.cz) · [sencurio.com](https://sencurio.com)

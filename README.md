# 🩱 Bikini Engine

> **Минималистичный движок для текстовых квестов на Python.**
> Пишешь сценарий в `qwerty.txt` — получаешь игру с артом, развилками и меню.

---

## ✨ Что это

**Bikini Engine** — крошечный движок для текстовых приключений. Игра описывается обычным текстовым файлом простыми командами вида `команда<аргумент>`. Арт — ASCII-графика в папке `art/`. Развилки — через `choice` / `option`. Никаких сторонних библиотек, только стандартная и Python 3.10+.

```
set_pictures<start.txt>
draw<Ты стоишь на перекрёстке.>

choice<Куда пойдёшь?>
option<Налево>
    draw<Ты пошёл налево и нашёл клад!>
option<Направо>
    draw<Ты пошёл направо и встретил дракона.>
option<Нахуй>
    draw<Ты пошёл нахуй. Приключение окончено.>
choice<end>

draw<Конец.>
end<>
```

---

## 🚀 Установка

### Через установщик

```bash
python installer.py
```

| Шаг | Действие |
|-----|----------|
| `[1]` | Указать путь, где создать папку проекта |
| `[2]` | Ввести имя игры |
| `install` | Запустить установку |

Установщик создаст:

```
<путь>/<имя_игры>/
├── main.py        # точка входа
├── engine.py      # движок
├── qwerty.txt     # сценарий
└── art/
    └── start.txt  # стартовый арт
```

Запуск:

```bash
cd <путь>/<имя_игры>
python main.py
```

### Вручную

Скопируй `engine.py`, `main.py`, `qwerty.txt` и папку `art/` в любую папку — и запускай `python main.py`.

---

## 📜 Формат сценария

Каждая команда — на отдельной строке:

```
команда<аргумент>
```

Строки без `<...>` игнорируются.

### Команды

| Команда | Что делает |
|---|---|
| `draw<текст>` | Показывает арт + печатает текст по буквам. Ждёт ввода. `quit` / пусто — выход. |
| `set_pictures<файл>` | Загружает арт из `art/<файл>` и запоминает. |
| `choice<вопрос>` | Начало развилки. Показывает вопрос и варианты, ждёт номер. Выполняет **только выбранную** ветку. |
| `option<подпись>` | Вариант ответа внутри `choice`. Всё до следующего `option` / `choice<end>` — команды этой ветки. |
| `choice<end>` | Конец развилки. |
| `end<>` | Конец сценария. |

### Пример с вложенной развилкой

```
set_pictures<crossroad.txt>
draw<Ты стоишь на перекрёстке.>

choice<Куда пойдёшь?>
option<Налево>
    draw<Ты пошёл налево и нашёл клад!>
option<Направо>
    draw<Ты пошёл направо и встретил дракона.>
    choice<Дракон перед тобой. Что делаешь?>
    option<Сражаться>
        draw<Ты победил дракона!>
    option<Убежать>
        draw<Ты убежал. Жив, но без славы.>
    choice<end>
option<Нахуй>
    draw<Ты пошёл нахуй. Приключение окончено.>
choice<end>

draw<Конец.>
end<>
```

> При выборе **«Направо»** игра покажет дракона и спросит «Сражаться / Убежать». Ветки **«Налево»** и **«Нахуй»** не выполнятся.

---

## 🎨 Арт

Арт — обычные текстовые файлы в `art/`. Рисуй ASCII в блокноте:

```
+--------------------+
|   НОВАЯ ИГРА       |
|   Bikini Engine    |
+--------------------+
```

Подключение:

```
set_pictures<start.txt>
```

Движок ищет `art/start.txt` **относительно папки игры**.

---

## ⚙️ Как работает движок

```
main.py
  └── run_script("qwerty.txt", "art")
        └── run_lines(lines, art_dir)
              ├── parse_line   — "draw<текст>" → ("draw", "текст")
              ├── draw         — арт + текст + ввод
              ├── set_pictures — чтение файла из art/
              ├── choice       — collect_choice + меню + рекурсия
              └── end          — выход
```

**Ключевая идея:** на `choice<Вопрос>` движок вызывает `collect_choice`, который собирает все `option`-ветки в список **(не выполняя их)**. Затем — меню, игрок вводит номер, и `run_lines` **рекурсивно** запускается только для тела выбранной ветки. Поэтому вложенные `choice` работают из коробки.

---

## 📦 Требования

- **Python 3.10+** (`match` / `case`)
- **Никаких** сторонних библиотек

---

## 📁 Структура проекта

```
bikini-engine/
├── installer.py     # установщик
├── engine.py        # движок
├── main.py          # точка входа
├── qwerty.txt       # пример сценария
├── art/
│   └── start.txt    # пример арта
└── README.md
```

---

## ⚠️ Ограничения

- ❌ Нет сохранений / загрузок — игра всегда с начала `qwerty.txt`
- ❌ Нет флагов и `if/else` — только развилки `choice`
- ❌ Арт только текстовый (ASCII), без картинок
- ❌ `choice` не поддерживает «вернуться в меню» после ветки

---

## 📄 Лицензия

**MIT** — делай что хочешь, только не продавай как свой движок.


# 🩱 Bikini Engine

> **A minimalist engine for text quests in Python.**
> Write a script in `qwerty.txt` — get a game with art, branching, and menus.

---

## ✨ What is it

**Bikini Engine** is a tiny engine for text adventures. A game is described in a plain text file using simple commands of the form `command<argument>`. Art is ASCII graphics in the `art/` folder. Branching is done with `choice` / `option`. No third-party libraries — only the standard ones and Python 3.10+.

```
set_pictures<start.txt>
draw<You stand at a crossroads.>

choice<Where will you go?>
option<Left>
    draw<You went left and found a treasure!>
option<Right>
    draw<You went right and met a dragon.>
option<To hell>
    draw<You went to hell. The adventure is over.>
choice<end>

draw<The end.>
end<>
```

---

## 🚀 Installation

### Via the installer

```bash
python installer.py
```

| Step | Action |
|------|--------|
| `[1]` | Specify the path where the project folder will be created |
| `[2]` | Enter the game name |
| `install` | Start the installation |

The installer will create:

```
<path>/<game_name>/
├── main.py        # entry point
├── engine.py      # the engine
├── qwerty.txt     # script
└── art/
    └── start.txt  # starting art
```

Run:

```bash
cd <path>/<game_name>
python main.py
```

### Manual

Copy `engine.py`, `main.py`, `qwerty.txt` and the `art/` folder into any directory — and run `python main.py`.

---

## 📜 Script format

Each command is on its own line:

```
command<argument>
```

Lines without `<...>` are ignored.

### Commands

| Command | What it does |
|---|---|
| `draw<text>` | Shows the art + prints the text character by character. Waits for input. `quit` / empty — exit. |
| `set_pictures<file>` | Loads art from `art/<file>` and remembers it. |
| `choice<question>` | Starts a branch. Shows the question and options, waits for a number. Executes **only the chosen** branch. |
| `option<label>` | An answer option inside `choice`. Everything up to the next `option` / `choice<end>` is that branch's commands. |
| `choice<end>` | Ends the branch. |
| `end<>` | Ends the script. |

### Example with a nested branch

```
set_pictures<crossroad.txt>
draw<You stand at a crossroads.>

choice<Where will you go?>
option<Left>
    draw<You went left and found a treasure!>
option<Right>
    draw<You went right and met a dragon.>
    choice<A dragon stands before you. What do you do?>
    option<Fight>
        draw<You defeated the dragon!>
    option<Run away>
        draw<You ran away. Alive, but without glory.>
    choice<end>
option<To hell>
    draw<You went to hell. The adventure is over.>
choice<end>

draw<The end.>
end<>
```

> Choosing **"Right"** shows the dragon and asks "Fight / Run away". The **"Left"** and **"To hell"** branches are not executed.

---

## 🎨 Art

Art is just plain text files in `art/`. Draw ASCII in a text editor:

```
+--------------------+
|   NEW GAME         |
|   Bikini Engine    |
+--------------------+
```

Attach it:

```
set_pictures<start.txt>
```

The engine looks for `art/start.txt` **relative to the game folder**.

---

## ⚙️ How the engine works

```
main.py
  └── run_script("qwerty.txt", "art")
        └── run_lines(lines, art_dir)
              ├── parse_line   — "draw<text>" → ("draw", "text")
              ├── draw         — art + text + input
              ├── set_pictures — reads a file from art/
              ├── choice       — collect_choice + menu + recursion
              └── end          — exit
```

**Key idea:** on `choice<Question>` the engine calls `collect_choice`, which gathers all `option` branches into a list **(without executing them)**. Then it shows a menu, the player enters a number, and `run_lines` **recursively** runs only the body of the chosen branch. That's why nested `choice` works out of the box.

---

## 📦 Requirements

- **Python 3.10+** (`match` / `case`)
- **No** third-party libraries

---

## 📁 Project structure

```
bikini-engine/
├── installer.py     # installer
├── engine.py        # the engine
├── main.py          # entry point
├── qwerty.txt       # sample script
├── art/
│   └── start.txt    # sample art
└── README.md
```

---

## ⚠️ Limitations

- ❌ No saves / loads — the game always starts from the beginning of `qwerty.txt`
- ❌ No flags or `if/else` — only `choice` branches
- ❌ Text-only art (ASCII), no images
- ❌ `choice` doesn't support "return to menu" after a branch

---

## 📄 License

**MIT** — do whatever you want, just don't sell it as your own engine.

// АКТУАЛЬНЫЕ НАСТРОКИ ТУТ ----> https://t.me/jun_python/422/34691
// ПЛЮС МНОГО БЕСПЛАТНОЙ ИНФЫ ПО PYTHON

{
    "[python]": {
        "editor.formatOnType": true,
        "editor.defaultFormatter": "ms-python.autopep8", // Форматирование кода при вводе для языка Python
    },
    "workbench.iconTheme": "material-icon-theme", // Форматирование кода при сохранении файла
    "workbench.layoutControl.enabled": false, // Отключение разметки для области видимости
    "code-runner.clearPreviousOutput": true, // Очистка предыдущего вывода перед выполнением кода в Code Runner
    "code-runner.showExecutionMessage": false, // Отключение отображения сообщений о выполнении в Code Runner
    "code-runner.saveFileBeforeRun": true, // Автоматическое сохранение файла перед выполнением кода в Code Runner
    "editor.accessibilityPageSize": 12, // Размер страницы доступности редактора
    // "editor.minimap.enabled": false, // Отключение мини-карты
    "editor.lineHeight": 28, // Высота строки
    "editor.hover.delay": 1500, // Задержка при отображении всплывающей подсказки
    "editor.fontSize": 22, // Размер шрифта редактора
    "editor.letterSpacing": 0.3, // Межбуквенное расстояние
    "editor.mouseWheelZoom": true, // Включение масштабирования колесиком мыши
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": [
                    // Области, для которых задается цвет
                    "source",
                    "variable",
                    "constant",
                    "variable.other.constant",
                    "punctuation.definition.constant",
                    "constant.other.symbol",
                    "constant.language.symbol",
                    "support.constant",
                    "support.variable.magic.python",
                    "variable.other.enummember"
                ],
                "settings": {
                }
            }
        ]
    },
    "scm.inputFontSize": 14, // Размер шрифта в интегрированном терминале
    "editor.scrollbar.horizontalScrollbarSize": 14, // Размер горизонтальной полосы прокрутки
    "editor.insertSpaces": true, // Вставка пробелов вместо табуляции
    "files.trimFinalNewlines": true, // Удаление пустых строк в конце файла
    "editor.wordWrap": "on", // Включение переноса строк
    "editor.formatOnSave": true, // форматирование при сохранении
    "editor.defaultFormatter": "ms-python.autopep8",
    "terminal.integrated.mouseWheelZoom": true,
    "autopep8.args": [
        "--ignore=E731", // игнор замены лямбды на функцию согласно PEP8
        // "--max-line-length 1000" // увеличение длины не работает
    ],
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "terminal.integrated.gpuAcceleration": "on",
    "terminal.integrated.fontSize": 21,
    "terminalThemes.style": "3024 (base16)",
    "editor.fontLigatures": false,
    "workbench.colorTheme": "Atom One Dark",
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "cSpell.language": "en,ru",
    "interactiveWindow.executeWithShiftEnter": true,
    "cSpell.userWords": [
        "beegeek",
        "stepik"
    ],
    "editor.minimap.showSlider": "always",
    "editor.minimap.scale": 2,
    "python.terminal.activateEnvInCurrentTerminal": true,

    "indentRainbow.ignoreErrorLanguages" : [
        "python",
    ],
      // Using the light mode
    "indentRainbow.indicatorStyle": "light",
  // we use a simple 1 pixel wide line
    "indentRainbow.lightIndicatorStyleLineWidth": 1,
  // the same colors as above but more visible
    "indentRainbow.colors": [
    "rgba(255,255,64,0.3)",
    "rgba(127,255,127,0.3)",
    "rgba(255,127,255,0.3)",
    "rgba(79,236,236,0.3)"
    ]
}

// justMyCode" (по умолчанию == true) выключен обход библиотеки

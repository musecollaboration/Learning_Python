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
    "editor.minimap.enabled": false, // Отключение мини-карты
    "editor.lineHeight": 24, // Высота строки
    "editor.hover.delay": 1500, // Задержка при отображении всплывающей подсказки
    "editor.fontSize": 22, // Размер шрифта редактора
    "editor.letterSpacing": 0.3, // Межбуквенное расстояние
    "editor.mouseWheelZoom": true, // Включение масштабирования колесиком мыши
    "editor.tokenColorCustomizations": {
        "variables": "#DCDEDF", // Изменение цвета переменных
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
                    "foreground": "#DCDEDF" // Задание цвета текста
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
        "--ignore=E731" // игнор замены лямбды на функцию согластно PEP8
    ],
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.enableMultiLinePasteWarning": "never",
    "terminal.integrated.gpuAcceleration": "on",
    "terminal.integrated.fontSize": 20,
    "terminalThemes.style": "3024 (base16)",
}

# Автоматизация отчетности

Данный проект представляет собой набор скриптов для автоматизации процесса обработки отчетности. Он разработан с целью упростить и ускорить процедуру генерации отчетов для различных типов выгрузок.

## Описание

В проекте содержатся скрипты для обработки следующих типов выгрузок:

### Дополнительные выгрузки

- Affinity
- TVR
- Reach
- Positioning

Каждый скрипт предоставляет функциональность для обработки соответствующего типа выгрузок. Они позволяют считывать, анализировать и генерировать отчеты.

## Установка Git

Для работы с нашим проектом вам понадобится установить Git. Вот инструкции по установке Git на различных операционных системах:

### Windows

1. Перейдите на официальный сайт Git: [https://git-scm.com/downloads](https://git-scm.com/downloads).
2. Скачайте установочный файл для Windows.
3. Запустите загруженный установочный файл и следуйте инструкциям мастера установки.
4. После завершения установки Git будет доступен из командной строки.

### macOS

1. Откройте терминал.
2. Установите Homebrew, если вы еще не установили его, выполнив команду:

   ```shell
   /bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'
   ```

3. Установите Git, выполнив команду:

   ```shell
   brew install git
   ```

### Linux

1. Откройте терминал.
2. Выполните следующую команду для установки Git:

   - Ubuntu и Debian:

     ```shell
     sudo apt update
     sudo apt install git
     ```

   - Fedora:

     ```shell
     sudo dnf install git
     ```

   - CentOS:

     ```shell
     sudo yum install git
     ```

   После завершения установки Git будет доступен из командной строки.

## Установка Python

Для работы с нашим проектом вам понадобится установить Python. Вот инструкции по установке Python на различных операционных системах:

### Windows

1. Перейдите на официальный сайт Python: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
2. Скачайте установочный файл для Windows.
3. Запустите загруженный установочный файл.
4. В мастере установки выберите опцию 'Add Python to PATH' и следуйте инструкциям мастера.
5. После завершения установки Python будет доступен из командной строки.

### macOS

1. Откройте терминал.
2. Установите Homebrew, если вы еще не установили его, выполнив команду:

   ```shell
   /bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'
   ```

3. Установите Python, выполнив команду:

   ```shell
   brew install python
   ```

### Linux

1. Откройте терминал.
2. Выполните следующую команду для установки Python:

   - Ubuntu и Debian:

     ```shell
     sudo apt update
     sudo apt install python3
     ```

   - Fedora:

     ```shell
     sudo dnf install python3
     ```

   - CentOS:

     ```shell
     sudo yum install python3
     ```

   После завершения установки Python будет доступен из командной строки.

Обратите внимание, что приведенные инструкции предполагают использование стандартных инструментов установки для каждой операционной системы. Если вы предпочитаете использовать другие инструменты или специфические настройки установки, адаптируйте инструкции соответствующим образом.

## Установка проекта

1. Склонируйте репозиторий на свою локальную машину:

  ```shell
  git clone https://github.com/Neyslutrans/.git
  ```

2. Перейдите в папку проекта:

  ```shell
  cd 
  ```

3. Установите необходимые зависимости:

  ```shell
  pip install -r requirements.txt
  ```

## Обновления

Ваш репозиторий будет периодически обновляться, и вам будут отправляться сообщения о внесенных изменениях. Каждое из таких сообщений содержит префикс, который указывает на тип обновления. Вот основные префиксы, используемые в сообщениях об обновлениях.

- **build**: Сборка проекта или изменения внешних зависимостей
- **ci**: Настройка CI и работа со скриптами
- **docs**: Обновление документации
- **feat**: Добавление нового функционала
- **fix**: Исправление ошибок
- **perf**: Изменения направленные на улучшение производительности
- **refactor**: Правки кода без исправления ошибок или добавления новых функций
- **revert**: Откат на предыдущие коммиты
- **style**: Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)
- **test**: Добавление тестов

## Структура проекта

Данный репозиторий содержит следующую структуру:

### Вспомогательные файлы

- `README.md` - файл, с описанием проекта, его функциональности, инструкции по установке, настройке и использованию, а также другой полезной информацией для пользователей и разработчиков
- `requirements.txt` - файл, в котором перечислены зависимости проекта
- `.gitignore` - файл, определяющий игнорируемые Git'ом файлы и папки
- `restore.py` - скрипт для восстановления репозитория в случае критического нарушения его структуры

### Модули

- `modules` - папка, содержащая необходимые для работы модули
    - `paths.py` - модуль для манипулирования путями
    - `logics.py` - модуль, содержащий логику обработки различных типов выгрузок
    - `workbook.py` - модуль, содержащий функции обработки Excel объектов
    - `dataframe.py` - модуль для работы с dataframe

### Вспомогательные файлы
- `addons` - папка, содержащая необходимые для работы скриптов вспомогательные файлы
  - `ad_channels.csv` - содержит перечень рекламных каналов
  - `auditory.csv` - содержит перечень баинговых аудиторий
  - `channels.csv` - содержит перечень основных каналов
  - `dates.csv` - содержит данные для обработки дат
  - `off_prime.csv` - содержит временные интервалы для определения Prime / Off prime
  - `round.csv` - содержит округления

### Основные скрипты

- `main.py` - скрипт, представляющий собой терминальный интерфейс для управления запуском скриптов

Ниже представлен перечень скриптов для обработки выгрузок:

#### Дополнительные выгрузки

- `affinity.py` - скрипт для обработки выгрузок типа 'Affinity'
- `tvr.py` - скрипт для обработки выгрузок типа 'TVR'
- `reach.py` - скрипт для обработки выгрузок типа 'Reach'
- `positioning.py` - скрипт для обработки выгрузок типа 'Positioning'
- `national.py` - скрипт для обработки национальной выгрузки

## Вклад

Все виды вклада приветствуются! Если вы обнаружите ошибку, у вас есть предложение по улучшению или хотите внести свой вклад, пожалуйста, сообщите об этом.

## Контактная информация

Если у вас возникли вопросы или предложения, пожалуйста, свяжитесь со мной по электронной почте: [neyslutrans@outlook.com](mailto:neyslutrans@outlook.com).
# Chepuha

  Онлайн-игра "Чепуха" (Android). 
  Доступны два режима: онлайн и офлайн игра.
  При входе в игровую комнату доступен комнатный чат.
  При запуске игры появляется экран меню (создать онлайн-игру, присоединиться по ip, присоединиться к любой игре, оффлайн-игра).
### Создание онлайн-игры
  При создании онлайн-игры создается сервер (не на телефоне создателя комнаты, т.к. если он отключится, то сервер упадет). **_Подумать, где будут создаваться игровые сервера._** После создания и запуска сервера, высвечивается ip, которое создатель может скопировать и показать/отправить тем, с кем собирается играть (если своя компания).
### присоединиться по ip
  При присоединении к игре по уже изветному ip, пользователь попадает в игровую комнату. До начала игры создателю доступна кнопка "начать" и чат между игроками в комнате, всем кроме создателся доступен только чат. После запуска игры у всех одинаковый интерфейс: кнопка выхода, чат, поле для ввода ответа и вопроса, кнопка завершения игры и показа полученной истории.
### присоединиться к любой игре
  При присоединении к игре не по ip, пользователь попадает в рандомную комнату, где игра еще не начата, либо создает такую комнату.
### оффлайн-игра
  В оффлайн игре пользователю предоставляется интерфейс для выбора количества игроков и ввода их имён, после чего начинается игра.


## Процесс разработки приложения

Выполнить/Пофиксить:

* После сборки в apk файл, возникает ошибка при попытке обращения к объекту аудиозаписи.
* При нажатии на любую кнопку должен появлятся звук нажатия, но он проигрывается только один раз. При повторном нажатии звук не воспроизводится и ошибок приложения при этом не возникает.
* При нажатии на кнопку выключения звука не изменяется иконка кнопки (вероятно не верно обращаюсь к свойству кнопки)
* При первом ходу в поле вывода не выводится имя игрока.
* При передаче хода следующем игроку генерируется новый экран. На данном этапе просто очищаются поля ввода и обновляется поле вывода.
* У TextField статическая ширина виджета, необходимо, чтобы она занимала ширину родителя.
* Добавить кнопку удаления игрока справа от поля ввода TextField

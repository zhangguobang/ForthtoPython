*forth | stack |  harv | hw | tick | struct | trap | port | pstr  | prob1 | spi
# Forth Программирование
* Сама директива не различает размер записи, за исключением символических заявлений. Например, LD # 1 равен LD # 1
* Первая функция - это... start, то есть ввод.
* Директивы выполняются последовательно. Операционная интерпретация директивы выглядит следующим образом:

- 'ld Параметры' - Загрузить. Его функция - загружать данные из памяти в регистр.

- 'st Параметры' - Удаление. Удалить значение из регистра в память

- 'add параметр' - Добавить указанное значение в регистр

- 'sub - параметр' - Удалить указанное значение из регистра

- 'mul параметр' - умножить регистр на указанное значение

- 'div параметр' - - разделить регистр на указанный

- 'cmp параметр' - Сравните значение регистра с указанным значением и установите значение состояния

- "параметр jmp" - безусловный переход на целевой адрес, указанный в директиве, и выполнение с этого адреса. Адрес цели может быть получен непосредственно из команды или из регистра или памяти, указанной в инструкции.

- 'jz параметр' - простая команда условной передачи - равномерная передача

- 'параметр js' - - одноусловная команда передачи - - предыдущая операция дала отрицательный результат передачи

- 'jnz параметр' - простая команда условного перехода - неравномерный переход (с JNE)

- 'HLT - Параметры' - - Команда останавливает процессор

- 'push Параметры' - - в стек. Вставить слово в регистр сегментов в стек

- 'pop параметр' - - Выход из стека. Отправить всплывающий элемент верхней части стека в регистр

- ' Call ПараметрЫ' - Вызов программы
- 'ret Параметры' - Возвращение

- 'параметр inv' - получение обратного числа регистров

- 'split Параметры string'- - разделить строку

- 'pstr параметр' - - Строка печати

LD: Загрузить значение в накопитель.
ST: Сохранить значение накопителя на указанный адрес.
ADD, SUB, MUL, DIV: Выполнение основных арифметических операций и обновление логотипа.
CMP: Сравните значение накопителя с другим значением, обновите нулевой знак (Z) и символьный знак (S).
JMP: безусловный переход на указанный адрес.
JZ, JNZ: Если нулевой знак является истинным / ложным, перейдите на указанный адрес.
JE, JNE: Условный прыжок на основе нулевого знака.
PUSH, POP: Операция со стеком.
CALL, RET: Функция вызывает и возвращает.
Split string, pstr: Поддерживаются три действия: перевернуть строку, преобразовать в заглавный регистр и преобразовать в нижний регистр

* Содержание после повторной запятой будет считаться примечанием


* Поддержка символического кодирования. Символы хранятся в цифровой форме в памяти:


```

' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32,'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43,'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52, '':53, '0':54,'1':55, '2':56, '3':57, '4':58, '5':59, '6':60, '7':61, '8':62, '9':63, '!':64, ',':65,'.':66, '-':67, '*':68, '?':69, '+':70, '/':71, '@':72, '\0':73, '\n':74

```
* Метки элементов управления:

- « section.data» - метка, указывающая начало области данных. После этого вы можете объявить переменные, но не можете написать код.
- 'section.text' - Метка, указывающая начало кода

* Функции & теги:

* Функция определяется следующим образом: « Название функции»
* Давайте определим этикетку следующим образом: '... > Название метки > >
Функция отличается от тега тем, что тег начинается с «...». Когда мы хотим перейти на определенный ярлык, мы должны использовать его следующим образом:
jmp.label Имя

* Поиск адреса (формат параметров):

* Чистое число: если число параметров, то оно считается адресом. То есть, LD 29 - означает загрузку значения 30 - й ячейки в аккумулятор.
* Только значение: если параметр имеет "#" и следует за цифрой, этот параметр считается значением. LD # 29 - это загрузка 29 в батарею.
* Переменная: Если параметр является переменной, определенной в разделе данных, он рассматривает адрес как переменную.
* Символы: закодированы в цифры на основе таблицы символов. Например, ld 'A' = ld # 27

* Определение значения состояния:


  * True = 1
  * Flase = 0

* Определение переменной:


* Определяется следующим образом: < Name: Value >. Это значение может быть числом или строкой. Если это строка, она будет иметь столько же ячеек, сколько и число символов.


# # Память


Память команд и данных.


Память - это список ячеек. Клетки реализуются классом Cell.


* Или цифра - то есть данные. Машинный разряд - 32 бита * *. В ячейке сохраняется только один символ. В соответствии с таблицей символов, определенной в ISA, символ также имеет цифровую форму * *

* Или инструкция, обозначенная как класс - Instruction * *. В объекте класса, Instruction хранит тип команды и параметры * *

Дизайн стека.


Последняя часть * * 1 / 4 * * - это порт IO, который используется только для IO.

# # Командная система


* Машинная позиция - 32 бита.

* Основатель - Чжан Гобан

* Регистр:


* Счетчик IP

* Обмен -

* Регистр

* Заимствовано из стека

* Сохранить результат любой функции

* Сохранить результаты любых математических операций

* BR - буфер для временного хранения данных. Например, он используется для хранения результатов функции в команде ret.

* AR - это указанный адрес ячейки, с которой они взаимодействуют, т.е. регистр. Все еще указывает? "Адрес" стека.

* PS - условный код.

* SP - указатель стека.

# # Код команды


Машинный код хранится в формате CSV


Вся процедура состоит из четырех частей. Отличить по указанной метке,


- Часть первая Директива, метка FUNCTION перед набором инструкций. Содержание директивы делится на три столбца "" в каждой строке:

- Первая колонка - указатель инструкций.

- Вторая колонка - инструкции.

- Параметры третьей колонки (если есть)

- Вторая часть является функцией, а после FUNCTION и до LABEL выполняется функция. Функция содержимого функции делится на две колонки в каждой строке ":":

- Первая колонка называется.

- Вторая колонка - указатель инструкций.

- Третья часть - этикетка, после LABEL и до VARIABLE - этикетка. Содержание этикетки разделено на три столбца в каждой строке ":"

- Первый столбец - это имя функции.

- Во второй колонке - название метки.

- Третья колонка - указатель инструкций.

- Четвертая часть - переменная, а после тега VARIABLE - переменная. Переменная делится на три столбца с ":"

- Первый столбец - это имя переменной.

- Вторая колонка - это значение.

- Третья колонка - длина строки (если есть)

Пример:

```
0 LD 'H' 
1 ST OUTPUT 
2 LD 'e' 
3 ST OUTPUT 
4 LD 'l' 
5 ST OUTPUT 
6 LD 'l' 
7 ST OUTPUT 
8 LD 'o' 
9 ST OUTPUT 
10 LD ',' 
11 ST OUTPUT 
12 LD 'w' 
13 ST OUTPUT 
14 LD 'o' 
15 ST OUTPUT 
16 LD 'r' 
17 ST OUTPUT 
18 LD 'l' 
19 ST OUTPUT 
20 LD 'd' 
21 ST OUTPUT 
22 HLT 
FUNCTION
_START:0
LABEL
_START:.LOOP:0
VARIABLE

```
# Переводчик


Выполнить команду: 'Python Forth Как Компилер CLI.Py "


Поддерживает фундаментальные ошибки:


* Невозможно определить две переменные с тем же именем

* Не используйте "Input" или "Output" в качестве имени переменной.

Проверка правильности определения параметров пользователем. Например, вы можете определить параметры для команд без параметров.

* Проверьте формат переменных.

* Информация об ошибке указывает неправильное местоположение.


Функции переводчика:


1. Проверьте часть этикетки. Данные

Прочитайте переменные и сохраните их в

3. Проверка части этикеток

4.Читать код

* Если строка является меткой, сохраните ее расположение, в том числе на славянском label Ин Функции и названия в Fun.

* Если строка является функцией, то она находится в function Сохранить местоположение и имя в точке

* Если строка является инструкцией, храните ее расположение, тип и параметры в строке результата

Когда он читает строку, он автоматически игнорирует комментарии

Перед любой обработкой 1 - 4 инструкции будут преобразованы в заглавный регистр.

7.По результатам, переменная, label Ин Функции и функции Point генерирует выходной файл.

# Компьютерное моделирование

Команда выполнения: "Python Machine.py"

Процессор:

* Операции с одним и тем же объектом не выполняются в одной шкале.
* Выполнение операций с различными объектами в течение одного и того же цикла.

Алгоритм реализован:

* pstr,prob1,if,loop,trap        : /Enhanced_ISA.py
* I/O                            : /Enhanced_Machine_IO.py
* SPI 

# # Ручное тестирование:


* Тестирование компилятора: выполнение Forth_Like_Compiler.py

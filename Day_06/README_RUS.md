# Day 02 - Python Bootcamp
*`Topics:`* **Domain-Driven Design, Decorator**

## Exercise 00: Old Style

-----

Вам нужно написать скрипт cache_wiki.py, основной задачей которого будет загрузка страниц из Википедии, но интересующие нас данные - это ссылки в тексте и разделах "См. также", ведущие на другие страницы в самой Википедии. Это означает, что вам не нужно загружать содержимое, а только сохранить представление графа в виде JSON-файла wiki.json, так что вершины хранят страницы, а направленные ребра - ссылки.

Вы можете выбрать любую статью Википедии в качестве стартовой позиции по умолчанию. Кроме того, ваш код должен уметь принимать в качестве аргумента название существующей статьи, чтобы использовать ее вместо статьи по умолчанию (не обязательно связанной с Гарри Поттером). Таким образом, при запуске программы, например:

~$ python cache_wiki.py -p 'Erdős number'

он должен начать парсинг с этой страницы. Обратите внимание на специальную кодировку символов в URL.

Цель состоит в том, чтобы следующие ссылки (только те, которые ведут на другие страницы Википедии, а не во внешний интернет) уходили как минимум на три страницы вглубь каждой ссылки. Этот параметр должен настраиваться с помощью параметра -d, поэтому по умолчанию значение будет равно 3. Но если результат слишком велик (>1000 страниц), ваш код должен прекратить обработку ссылок. Если же он слишком мал (<20 страниц), то выберите какую-нибудь другую начальную страницу по умолчанию. Не забывайте следить за ссылками, ведущими на страницы, которые вы уже посетили. Если страница A ссылается на страницу B, а страница B ссылается на страницу A - это два ребра направленного графа, а не одно.

Каждая страница, которую посещает ваш код, должна записываться в stdout с помощью модуля logging Python с уровнем лога 'INFO'.


Строгих требований к формату JSON-файла, создаваемого вашим кодом, нет, но имейте в виду, что вам придется работать с этим файлом в следующих упражнениях, поэтому вы можете рассмотреть возможность использования существующих библиотек Python для обработки графов, которые поддерживают чтение/запись JSON-файлов.

Чтобы получить дополнительный балл за это упражнение, ваш код может также поддерживать хранение графа в базе данных Neo4J.

<h2 id="chapter-v" >Chapter V</h2>
<h3 id="ex01">Exercise 01: Shortcuts</h3>

 "I see. But why are Welsh Corgi so close to King Solomon?"

Harry wanted to say that he has no idea, but then he noticed the smiling eyes of the wizard. 

 "Frankly speaking, I highly doubt it's the weirdest connection there," said the boy, "but
 don't you think, sir, it's..."
 
 "..absolutely fascinating!" finished the wizard. "I think I've underestimated muggles'
 technologies here, well done. Anyway, but how do we figure out how closely are two pages 
 connected to each other?"

Harry thought for a moment. 

 "I assume we can try and find the shortest path from one page to another. This is a pretty
 complicated task with a regular book, but it becomes a lot easier on a serialized graph."

-----

Теперь нужно написать программу shortest_path.py, которая должна будет найти длину кратчайшего пути между двумя страницами в вашей сериализованной базе данных (если такие страницы есть):

~$ python shortest_path.py --from 'Welsh Corgi' --to 'Solomon'
3
~$ python shortest_path.py --from 'Solomon' --to 'Welsh Corgi' --non-directed
3
Обратите внимание на флаг --non-directed. Он означает, что мы рассматриваем все связи как "ненаправленные" или "двунаправленные", поэтому каждое ребро рассматривается одинаково в обоих направлениях. В этом случае между любыми двумя узлами в сериализованном графе существует путь.

По умолчанию (если не указано --non-directed) мы следуем только за направленными ребрами графа. Это означает, что не все страницы в базе данных могут быть доступны с других страниц, особенно если они имеют небольшое количество входящих ссылок. Если путь не существует, ваш скрипт должен вывести 'Path not found'.

Местоположение вики-файла должно быть прочитано из переменной окружения WIKI_FILE. Если файл базы данных не найден, код должен вывести 'Database not found'.

Кроме того, добавьте флаг -v, который включит запись в журнал найденного пути, как показано ниже:

~$ python shortest_path.py -v --from 'Welsh Corgi' --to 'Solomon'
'Вельш-корги' -> 'Дрессировка собак' -> 'Кольцо царя Соломона (книга)' -> 'Соломон'
3
В этом упражнении вы не должны использовать существующую реализацию алгоритма "кратчайшего пути", предоставляемую существующими библиотеками. Пожалуйста, напишите его самостоятельно.


<h2 id="chapter-vi" >Chapter VI</h2>
<h3 id="ex01">Exercise 02: Greatest Magicians</h3>

  "Now I can see the relation with "six handshakes" rule you mentioned. Great magicians 
 can be quite popular, right?"

The boy stared at him, trying to understand what's going on in old wizard's head.

 "Oh, Harry, don't you know the definition of popularity? The more fans you have, the more
 well known overall you are. Like with rock bands."

Dumbledore stood up and went to the entrance of the office. Then he stopped right before the door
and turned back to Harry with a smile.

 "I think all we have to do is visualize the data. To find out who's the greatest, I mean."

Harry raised an eyebrow and looked at the wizard in surprise. It was said pretty loud and looked
like Dumbledore was serious. Find out who is the greatest? Okay, from the graph standpoint it
shouldn't be that hard...

...Draco Malfoy managed to escape from being caught eavesdropping. He was hiding around the corner
from the headmaster's office when Dumbledore left, and now his mind was filled with thoughts about
'greatest wizards'. He firmly decided that the next owl he will send to his father will be about 
connecting Malfoy Manor to the Internet.

-----

Следующий скрипт render_graph.py должен визуализировать ваш граф страниц (из файла, сгенерированного в EX00, также считывая его из переменной WIKI_FILE env) в виде PNG-изображения wiki_graph.png, с узлами и ребрами. Вы можете использовать для этого любую стороннюю библиотеку.

Главное правило здесь - размер узла должен соответствовать количеству входящих соединений. Чем больше связей - тем больше узел при рендеринге. Таким образом, "самые большие страницы" в вашем наборе данных будут лучше всего видны.

Вы можете получить дополнительный результат в этой задаче, если ваш скрипт опционально сможет генерировать не только .png-файл, но и страницу wiki_graph.html, которая покажет интерактивную визуализацию того же графа. Для этого можно использовать такие библиотеки, как Altair или Bokeh.


**Please leave your feedback [here](https://forms.gle/ZmAjM5qJ3uEnADen6)**

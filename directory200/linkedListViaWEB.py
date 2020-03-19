import copy

"""

В информатике, свя́зный спи́сок — структура данных, состоящая из узлов, каждый из которых содержит как собственные данные,
 так и одну или две ссылки («связки») на следующий и/или предыдущий узел списка. Принципиальным преимуществом перед
 массивом является структурная гибкость: порядок элементов связного списка может не совпадать с порядком расположения
 элементов данных в памяти компьютера, а порядок обхода списка всегда явно задаётся его внутренними связями.


Основные правила реализации связных списков
Список состоит из элементов, называемых узлами (node).
Первый узел списка называется «головным» (head),
а последний - «хвостовым» (tail).


Каждый элемент состоит из 3-х полей, два из которых являются указателями на предыдущий или следующий узел.
Элемент может указывать и более чем на два узла, и в этом случае список называется многосвязным.
Помимо упоминавшихся ранее стандартных массивов существуют еще динамические массивы. Размер обычного массива является
фиксированной величиной, а в динамический массив можно добавлять или удалять из него элементы. Если элемент добавляется
в середину динамического массива, то происходит перераспределение элементов, находящихся справа от него, так как все
элементы массива должны быть расположены в памяти строго по порядку. Поэтому вставка элемента в динамический массив
требует дополнительных ресурсов, если элемент добавляется не в конец массива. Преимущество связного списка в том, что
не требуется перестраивать последовательность узлов, независимо от того, в какую позицию списка вставляется новый элемент.
Недостаток связных списков – это последовательный доступ (sequential access) к элементам, тогда как для массивов время
доступа постоянно и не зависит от размера - random access. Если приложению требуется быстрый поиск элемента по индексу,
то в данном случае списки не подходят, и лучше воспользоваться массивами.
Еще один негативный момент при использовании связных списков связан с нерациональным использованием памяти. Если в узле
хранится небольшая порция данных, например, булевское значение, то список становится неэффективными из-за того, что
объем памяти, выделяемой под хранение связей, превышает объем памяти, выделяемой под хранение «полезной нагрузки».

Связный список - это рекурсивная структура, так как узел всегда содержит указатель на следующий узел. Это позволяет
использовать простой рекурсивный алгоритм для таких операций, как объединение двух списков или изменение порядка
элементов на обратный. У односвязных списков есть важное преимущество: если к вершине такого списка добавляется новый
элемент, то старый список будет по прежнему доступен по ссылке на только что добавленный узел. Этот прием называется
persistent data structure (постоянное хранение данных). У двусвязных списков есть свои преимущества, так как они
позволяют выполнять итерацию в обоих направлениях, в отличие от односвязных списков.
Если последний элемент будет указывать на первый элемент списка, то такая структура называется циклическим замкнутым
(или кольцевым (circular)) списком. Кольцевые списки можно использовать для списка процессов, в которых применяется
«карусельный» (round-robin) алгоритм. Для такого списка достаточно иметь один указатель, который одновременно указывает
и на конец, и на начало очереди. Кольцевой список можно разбить на два кольцевых списка или, наоборот, объединить.

Преимущества:

1) Удаление элементов в таком списке более эффективно, нежели удаление элементов из стандартного списка Python, который
рассматривался в предыдущем разделе. Так как этот элемент удаляется из середины стандартного списка, то время,
необходимое на эту операцию, будет зависеть от нескольких факторов: размера списка, положения удаляемого элемента
относительно конца. Чем больше размер списка, тем медленнее будет происходить данная операция. В данном случае со
ссылочной организацией списка удаление будет происходить одинаково быстро, независимо от размера списка и относительного
положения элемента, так как потребуется всего лишь перевести ссылку в предыдущем элементе на следующий за удаляемым
элемент.
2) То же самое можно сказать и про вставку элементов - она выполняется так же эффективно, как и удаление.
3) Объединение или разбиение 2-х списков будет выполняться быстрее, нежели в стандартном варианте.
4) Преимуществом связных списков является и то, что элемент такого списка может иметь произвольную структуру, и
включать не одну, а сразу несколько ссылок, что является отличительной особенностью деревьев.

Недостатки:
1) Требуется выделять дополнительную память на ссылки, которые сами по себе не несут никакой полезной информации.
2) Доступ к произвольному элементу для стандартного массива в Си и для стандартного списка в Python есть величина
постоянная и не зависящая от величины массива. В случае со ссылочными списками время доступа будет зависеть от величины
списка, так как потребуется выполнить итерацию по всему списку.
"""

#класс Node для определения элемента списка
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

# Для определения связного списка потребуется еще один класс – LinkedList, в конструкторе которого будут определяться
# первый и последний элементы списка и его длина. Также в классе будут использоваться встроенный метод str для распечатки
# содержимого списка и метод clear для очистки списка.

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = '<LinkedList --->\n' +str(current.value) +'\n'

            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + '<\LinkedList>'
        return 'LinkedList []'

    def clear(self):
        self.__init__()


    # Добавление элементов в конец списка.
    # Может я чего накрутил, но во первых я не понял, зачем была нужна секция "elif" и вообще я её немного упростил)
    def add (self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)



    # А не научиться ли нам вставлять эл-ты в начало списка?)
    # В реализации нужно учитывать два варианта: в первом случае список пуст, а во втором создается
    # новый узел, в конструктор которого в качестве второго параметра передается головной элемент списка.
    #     Комментарии по коду, те же, что и в предыдущем листинге.
    def push (self, x):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.first = Node(x, self.first)



    # Давайте усложним себе задачу и вставим новый элемент в место, куда хотим!)
    # Я посмел чуточку исправить код, чтобы он заработал, а так все как и там. Необходимо сначала
    # проверить, что список не пуст, а затем, что вставка не происходит на нулевую позицию.
    # Если оба условия не выполняются, то происходит итерация по списку до нужной позиции и добавление элемента:
    def InsertNth (self, i, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next


    # Научились добавлять, пора всех их посчитать!)
    # Я не очень понял, зачем в статье для этого пишется отдельная функция, видимо, чтобы просто
    # поиграть извилинами. Раз уж используем ООП, то просто при добавлении инкриментируем встроенную
    # переменную length, а при удалении дикрементируем, ну или как там?) Что я собственно и сделаю,
    # тогда длина списка всегда будет статична и не нужно будет бегать по списку для её нахождения,
    # хотя это и увеличит добавление и удаление элементов на несколько процессор-итераций.)
    # Но все же приведу ту ф-цию! Для определения длины списка в используется функция len,
    # которая вначале проверяет, не является ли список пустым, а затем выполняет итерацию по элементам списка.
    def len (self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first


    # Удаление головного элемента
    # В реализации потребуется проверить список на пустоту и объявить две локальных переменных:
    # первая будет хранить текущий элемент, а вторая - предыдущий. Потом выполняется итерация по
    # списку для поиска удаляемого элемента и проверка того, не является ли он последним в списке.
    # Если удаляемый элемент является последним, то предыдущий узел становится последним,
    # в противном случае предыдущий узел связывается со следующим узлом вместо текущего.
    def Del (self, i):
        if (self.first == None):
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    # Вставка элемента в отсортированный список
    # В данной реализации выполняется проверка списка на пустоту, а затем выполняется
    # итерация с помощью двух временных переменных, как и в прошлом листинге.
    def SortedInsert (self, x):
        if self.first == None:
            self.first = Node(x, self.last)
            return
        if self.first.value > x:
            self.first = Node(x, self.first)
            return
        curr = self.first
        while curr != None:
            if curr.value > x:
                old.next = Node(x, curr)
                return
            old = curr
            curr = curr.next
        self.last = old.next = Node(x, None)



    # Удаление повторяющихся значений
    # Сначала напишем данную функцию для общего случая. Она будет проходить по всему списку
    # от начала, до конца, для каждого элемента. Это приблизительно N2/2 проходов!
    def RemoveDuplicates (self):
        if (self.first == None):
            return
        old = curr = self.first
        while curr != None:
            if curr.next != None:
                if old.value == curr.next.value:
                    curr.next = curr.next.next
            else:
                old = curr = old.next
            curr = curr.next


    # Но куда более оптимальнее проводить данную операция для уже отсортированного списка,
    # т.к. это экономит нам много итераций по списку(т.к. не нужно проходить весь список).
    # Если в ходе итерации текущий элемент оказывается равным следующему за ним, то текущий элемент удаляется.
    def RemoveSortedDuplicates (self):
        if (self.first == None):
            return
        curr = self.first
        while curr != None:
            _del = 0
            if curr.next != None:
                if curr.value == curr.next.value:
                    curr.next = curr.next.next
                    _del = 1
            if _del == 0:
                curr = curr.next

    #Пузырьковая сортировка
    def BubbleSort (self):
        a = Node(0, None)
        b = Node(0, None)
        c = Node(0, None)
        e = Node(0, None)
        tmp = Node(0, None)

        while (e != self.first.next):
            c = a = self.first
            b = a.next

            while a != e:
                if a and b:
                    if a.value > b.value:
                        if a == self.first:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.first = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a

    #Функция получения элемента, обращаться можно по индексу L[n]:
    def __getitem__ (self, key):  # поддержка обращения по ключу
        length = 0
        current = None
        if self.first != None:
            current = self.first
            while key != length or current.next != None:
                current = current.next
                length += 1
            if key == length: current = current.value
        return current




if __name__ == "__main__":
    L = LinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(1)


    print(L)
    L.RemoveDuplicates()
    print(L)

    # Копирование списков
    # Это последнее, что мы с вами реализуем!) Если в СИ в реализации данной ф-ии используется три указателя:
    # на первый элемент оригинального списка и на первый и последний элементы скопированного списка и много кода,
    # то в Python для копирования списков можно использовать стандартный модуль copy, как показано ниже.
    #LTwo = copy.deepcopy(L) #// создание копии списка L

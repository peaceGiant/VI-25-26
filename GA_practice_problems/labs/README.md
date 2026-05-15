# Задача 1. / Problem 1.

Еден градски блок се соочува со опасно високи температури поради одбивање на сончевата светлина од блиските згради. Одредени точки стануваат екстремно жешки и небезбедни. За да ги заштитите пешаците, треба да поставите чадори за сонце така што сите опасни точки ќе бидат покриени.

Дадена ви е **област со големина 10 × 10** и **N опасни точки** прочитани од влезот, секоја со координати (x\_i, y\_i).

Можете да поставите **најмногу M чадори**, секој претставен како **круг со фиксен радиус R**, каде M и R се читаат од влезот. Секој чадор е дефиниран со координатите на неговиот **центар**. Не мора да ги користите сите чадори.

Целта е да **се покријат сите опасни точки користејќи што е можно помалку чадори**, при што се минимизира преклопувањето на чадорите и се осигурува дека чадорите остануваат во рамките на градскиот блок.

*   Точка се смета за покриена ако нејзиното растојание до барем еден центар на чадор е помало од радиусот R.
*   Чадорите МОРА целосно да се наоѓаат во рамките на градскиот блок. Не смее да постои решение/хромозом каде дел од чадорот е надвор од мрежата.
*   Нека d е растојанието помеѓу два центри на чадори. Велиме дека:
    *   нема преклопување ако d е поголемо од 2R;
    *   има големо преклопување ако d е помало од 8R/5;
    *   има мало преклопување во останатиот случај.

Дел 1.
------

Дополнете делови од дадениот почетен код. Не ги менувајте останатите параметри.

Дефинирајте соодветен gene space за овој проблем за секој тест пример. (Размислете за валиден начин за кодирање на решенијата)

Дизајнирајте decode функција која како влез прима решение/хромозом, а како излез враќа листа од торки со координати на центрите на **искористените чадори**. Поточно, вратете `[(x1, y1), (x2, y2), ...]`.

Дизајнирајте fitness функција која ги следи следниве принципи:

*   **Непокриени точки** → многу голема казна
    
*   **Големи преклопувања** → голема казна
    
*   **Мали преклопувања** → казна **10× помала** од големото преклопување
    
*   **Број на искористени чадори** → мала казна (се поттикнува користење на помал број чадори)
    

Валидно решение кое ги покрива сите точки секогаш треба да биде подобро од кое било решение кое остава непокриени точки.

Дел 2.
------

Во овој дел строго ќе работиме само со следниот влез:

    3 3 1  # N M R
    1 1
    1.1 1
    5 5

Конструирајте листа од **5 пример хромозоми** подредени во растечки редослед според квалитетот на fitness функцијата.

Вашите примери треба да бидат избрани така што ќе ги демонстрираат специфичните аспекти на fitness функцијата (непокриени точки, преклопувања, број на искористени чадори).

На крај, предадете ја fitness функцијата, decode функцијата, пример хромозомите и најдобрите хромозоми од секоја генерација до grader-от.

Внимавајте на fitness и decode функциите, тие треба да работат со хромозоми од различни должини, оние од тест примерите, како и пример хромозомите кои вие ги дефинирате. Дополнително, кога работите локално можете да ја искоментирате `submit_data` функцијата.


**Во оваа верзија постои опасност обичен чадор да се оштети доколку покрива две или повеќе опасни точки. За таа цел може да се искористи надграден чадор кој е отпорен на штетата од опасните точки. Само еден надграден чадор е на располагање, и истиот секогаш се користи. Да се дефинира соодветна казна за обичните чадори кои покриваат две или повеќе опасни точки. Декодирачката функција треба да враќа листа од чадори, така што надградениот чадор е секогаш на крај. Вкупно има M чадори (вклучувајќи го и надградениот чадор).**

* * *

A city block is experiencing dangerously high temperatures due to sunlight reflecting off nearby buildings. Certain spots become extremely hot and unsafe. To protect pedestrians, you must place sun umbrellas so that all dangerous spots are covered.

You are given a **10 × 10 area** and **N dangerous points** read from the input, each with coordinates (x\_i, y\_i).

You may place **at most M umbrellas**, each represented as a **circle with fixed radius R**, where M and R are read from input. Each umbrella is defined by the coordinates of its **center**. You don't have to use all umbrellas.

The goal is to **cover all dangerous points using as few umbrellas as possible**, while minimizing overlap and ensuring umbrellas stay inside the grid.

*   A point is considered covered if its distance to at least one umbrella center is less than the radius R.
*   Umbrellas MUST lie completely inside the grid. There mustn't be a solution/chromosome where an umbrella has a part of it outside the grid.
*   Let d be the distance between two umbrella centers. We say there is: 
    *   no overlap if d is greater than 2R;
    *   large overlap if d is smaller than 8R/5;
    *   small overlap otherwise.

Part 1.
-------

Complete parts of the provided template code. Do not modify other parameters.

Define the appropriate gene space for this problem for each test case. (Think about a valid way to encode the solutions)

Design a decode function which as input takes a solution/chromosome, and as output returns a list of tuples of coordinate centers of the **used umbrellas**. More precisely, return `[(x1, y1), (x2, y2), ...]`.

Design a fitness function that follows these principles:

*   **Uncovered points** → very large penalty
    
*   **Large overlaps** → large penalty
    
*   **Small overlaps** → penalty **10× smaller** than large overlap
    
*   **Number of umbrellas used** → small penalty (encourage fewer umbrellas)
    

A valid solution that covers all points should always be better than any solution that leaves points uncovered.

Part 2.
-------

In this section we will be strictly working with the following input:

    3 3 1  # N M R
    1 1
    1.1 1
    5 5

Construct a list of **5 example chromosomes** in increasing order of fitness quality.

Your examples need to be picked such that it demonstrates the specific aspects of the fitness function (uncovered points, overlaps, number of umbrellas used).

At the end, submit the fitness function, decoding function, the example chromosomes and the best chromosomes from each generation to the grader. Pay attention to the fitness and decode functions, they must work with chromosomes of different length, like the ones from the input test cases, as well as the example chromosomes that you provide. When working locally, you can comment out the `submit_data` function.


**In this version, there is a risk that a regular umbrella gets damaged if it covers two or more dangerous points. For this purpose, an upgraded umbrella can be used, which is resistant to damage from dangerous points. Only one upgraded umbrella is available, and it is always used. Define an appropriate penalty for regular umbrellas that cover two or more dangerous points. The decoding function should return a list of umbrellas such that the upgraded umbrella is always at the end. In total there are M umbrellas (including the upgraded umbrella).**


---

---

# Задача 2. / Problem 2.

Двајца пријатели планираат да истражуваат мрежа од **N** градови. Тие започнуваат од истиот почетен град **S** и сакаат да ги посетат сите останати градови што е можно поефикасно. По посетата на градовите, двајцата мора да ја завршат својата рута во одреден заеднички град **E**, каде повторно ќе се сретнат.

Пријателите можат да ја поделат работата меѓу себе на било кој начин. Секој град (освен почетниот и крајниот) мора да биде посетен точно еднаш од еден од пријателите, односно сите градови мора да бидат посетени, и ниту еден град не смее да биде посетен и од едниот, и од другиот (освен S и E). Целта е да се организираат нивните рути така што вкупното време потребно за двајцата да завршат ќе биде минимизирано.

Од влезот ви се дадени **N**, бројот на градови означени со вредности од **0** до **N-1**. Во следниот ред ви се дадени почетниот град **S** и крајниот град **E**. Дополнително, дадена е матрица `dist` со димензии **N x N**, каде `dist[i][j]` го претставува времето потребно да се патува од град i до град j.

Секој пријател започнува од градот S, посетува подмножество од градовите, и потоа продолжува кон градот E. Рутата е дефинирана како низа од градови која започнува со S и завршува со E.

Целта е да се распределат градовите меѓу двајцата пријатели и да се одреди редоследот во кој ќе ги посетуваат така што сите градови (освен S и E) ќе бидат посетени точно еднаш, и времето потребно за двајцата да завршат ќе биде минимизирано.

Вкупното време на еден пријател се дефинира како збир од времињата на патување помеѓу паровите соседни градови во неговата рута. Бидејќи пријателите се движат паралелно, целта е да се минимизира максималното време помеѓу двете рути.

Користејќи генетски алгоритми, дополнете делови од дадениот почетен код за алгоритмот да функционира правилно. Менувајте параметри на сопствен ризик.

Дефинирајте соодветен gene space за овој проблем. Размислете како да го енкодирате редоследот на посетување на градовите, како и кој пријател е одговорен за секој град.

Дизајнирајте decode функција која како влез прима решение/хромозом, а како излез враќа две рути, по една за секој пријател. Секоја рута мора да започнува со S и да завршува со E. Decode функцијата мора да осигура дека секој град (освен S и E) се појавува точно еднаш во двете рути. Пример излез: `[[S, A, B, C, E], [S, D, E]]` каде сите градови се цели броеви.

Дизајнирајте fitness функција која ги следи следниве принципи:

*   Целта е да се **минимизира максималното време на патување помеѓу двајцата пријатели**.
*   Доколку еден пријател има **значително подолго време** од другиот (значи повеќе од двојно), треба да се додели **голема казна**.
*   Доколку бројот на градови распределени меѓу двајцата пријатели е нерамномерен, треба да се додели **помала казна** за да се поттикнат побалансирани решенија.

Направете submit на fitness функцијата, decode функцијата и најдобрите хромозоми од секоја генерација до grader-от.

**Во оваа верзија, почетниот град не е зададен на влез. Двајцата пријатели заедно започнуваат од произволен град и треба да ги посетат сите градови и да завршат до градот Е. Направете промени во вашиот код за да го моделирате тоа.**

* * *

Two friends are planning to explore a network of **N** cities. They both start from the same starting city **S** and want to visit all other cities as efficiently as possible. After visiting the cities, they must both end their journey in a designated meeting city **E**, where they will reunite.

The friends can split the work between them in any way they want. Each city (except the starting and ending cities) must be visited exactly once by one of the two friends, i.e. all cities must be visited, and a city mustn't be visited by both friends (except for S and E). The goal is to organize their routes so that the total time required for both friends to finish is minimized.

From the input you are given **N**, the number of cities which will be labeled from **0** to **N-1**. In the next line you are given a starting city **S** and an ending city **E**. Additionally, you are given a matrix dist of size **N x N**, where `dist[i][j]` represents the time required to travel from city i to city j.

Each friend starts at city S, visits a subset of the cities, and then travels to city E. A route is defined as a sequence of cities starting with S and ending with E.

The goal is to distribute the cities between the two friends and determine the order in which they visit them such that all cities (except S and E) are visited exactly once, and the time required for both friends to finish is minimized.

The total time of a friend is defined as the sum of travel times along their route. Since the friends travel in parallel, the objective is to minimize the maximum of the two travel times.

Using genetic algorithms, complete parts of the provided template code to ensure the algorithm works properly. Modify parameters at your own risk.

Define an appropriate gene space for this problem. Think about how to encode both the order in which cities are visited and which friend is responsible for visiting each city.

Design a decode function which takes a solution/chromosome as input and returns two routes, one for each friend. Each route must start at S and end at E. The decode function must ensure that every city (except S and E) appears exactly once across both routes. Example output: `[[S, A, B, C, E], [S, D, E]]` where all cities are integers..

Design a fitness function that follows these principles:

*   The objective is to **minimize the maximum travel time between the two friends**.
*   If one friend takes **significantly longer** than the other (here significantly means more than double the time), a **large penalty** should be applied.
*   If the number of cities assigned to the two friends is unbalanced, a **smaller penalty** should be applied to encourage more balanced solutions.

Submit the fitness function, decode function, and the best chromosomes from each generation to the grader.

**In this version, the starting city is not given in the input. Both friends start together from an arbitrary city and must visit all cities, finishing in city E. Modify your code to model this.**
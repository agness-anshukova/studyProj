## Логика функционала учебной группы в парадигме ООП

- Класс Mentor является родительским классом для классов Lecturer и Reviewer.
  Имя, фамилия и список закрепленных курсов реализуются на уровне родительского класса. 

- Класс Lecturer (лектор)
  Лекторы могут получать оценки за лекции от студентов.
  Атрибут-словарь хранит оценки по 10-балльной шкале. Ключи – названия курсов, а значения – списки оценок. 
  count_avarage(self) - метод подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
  __str__(self), __lt__(self, other), __gt__(self, other), __eq__(self, other) - методы сравнения лекторов по их оценкам. 

- Класс Reviewer (эксперты, проверяющие домашние задания)  
  rate_homework(self, student, course, estimation) - метод выставляет студентам оценки за домашние задания.

- Класс Student
  Student имеет метод выставления оценок лекторам. При этом выставить оценку можно только тому лектору, который закреплен за тем курсом, на который записан студент.
  Содержит списки завершенных курсов и курсов в процессе изучения.
  count_avarage(self) - метод для подсчета средней оценки за домашние задания.
  __str__(self), __lt__(self, other), __gt__(self, other), __eq__(self, other) - методы сравнения студентов по их оценкам. 


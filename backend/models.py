from django.db import models


class Group(models.Model):
    name = models.CharField("Наименование", max_length=20)
    date_start = models.DateField("Начало обучения")
    date_end = models.DateField("Окончание обучения")
    date_exam = models.DateField("Дата сдачи экзаменов")
    category = models.CharField("Категория обучения", max_length=3)
    teacher = models.CharField("Преподаватель", max_length=100)
    time = models.CharField("Время занятий", max_length=100)

    def __str__(self):
        return f'{self.name}, категория: {self.category}'

    class Meta:
        verbose_name = "Группа обучения"
        verbose_name_plural = "Группы обучения"


class Instructor(models.Model):
    fio = models.CharField("ФИО инструктора", max_length=100)
    car = models.CharField("Машина", max_length=100)
    phone = models.CharField("Номер телефона", max_length=13)
    login = models.EmailField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=50)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"


class Student(models.Model):
    fio = models.CharField("ФИО ученика", max_length=100)
    birthday = models.DateField("Дата рождения")
    drive_count = models.PositiveSmallIntegerField("Кол-во часов вождения", default=16)
    login = models.EmailField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=50)
    instructor = models.ForeignKey(Instructor, verbose_name="Инструктор", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    phone = models.CharField("Номер телефона", max_length=13)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Schedule(models.Model):
    datetime = models.DateTimeField("Дата и время занятия")
    instructor = models.ForeignKey(Instructor, verbose_name="Инструктор", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="Ученик", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.instructor.fio}, {self.datetime}'

    class Meta:
        verbose_name = "Расписание вождения"
        verbose_name_plural = "Расписания вождения"


class Status(models.Model):
    status = models.CharField("Статус", max_length=20)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Request(models.Model):
    name = models.CharField("Имя", max_length=100)
    mail = models.EmailField("Почта", max_length=100)
    phone = models.CharField("Телефон", max_length=15)
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка на обучение"
        verbose_name_plural = "Заявки на обучение"

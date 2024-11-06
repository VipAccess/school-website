from django.db import models

class Disciplines(models.Model):
    """Модель преподаваемых дисциплин"""
    discipline_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    discipline_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Преподаваемые дисциплины'

    def __str__(self):
        return self.discipline_name

class Teachers(models.Model):
    """Модель преподавателей"""
    teacher_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=50)  # Ф.И.О.
    photo = models.FileField(null=True, blank=True, upload_to='photo/teachers/')  # Фото
    position = models.CharField(max_length=50)  # Должность.
    education_level = models.CharField(max_length=50)  # Уровень образования.
    qualification = models.CharField(max_length=50)  # Квалификация.
    degree = models.CharField(max_length=50)  # Ученая степень.
    academic_rank = models.CharField(max_length=50)  # Ученое звание.
    advanced_training_info = models.TextField()  # Сведения о повышении квалификации.
    professional_retraining_info = models.TextField()  # Сведения о профессиональной переподготовке.
    experience = models.IntegerField() # Стаж
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    educational_programs = models.CharField(max_length=50)  # Образовательные программы.
    discipline = models.ManyToManyField('Disciplines', blank=True)

    def get_discipline(self):
        return ", ".join([str(d) for d in self.discipline.all()])

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.full_name


class Awards(models.Model):
    """Модель наград"""
    award_name = models.CharField('Имя', max_length=255)
    photo = models.FileField(upload_to='photo/awards/')
    info = models.TextField('Описание')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

    def __str__(self):
        return self.award_name

class Licenses(models.Model):
    """Модель лицензий"""
    licenses_name = models.CharField('Имя', max_length=255)
    photo = models.FileField(upload_to='photo/licenses/')
    info = models.TextField('Описание', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

    def __str__(self):
        return self.licenses_name


class Documents(models.Model):
    """Модель для документов"""
    document_name = models.CharField('Имя', max_length=255)
    category = models.CharField('Категория', max_length=15)
    file = models.FileField(upload_to='documents/')
    info = models.TextField('Описание')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.document_name


class RequestsForAdmission(models.Model):
    """Модель заявок на поступление"""
    request_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    student_name = models.CharField('Ф.И.О Ученика', max_length=50)
    birth_certificate = models.FileField('Свидетельство о рождении', null=True, blank=True, upload_to='passports/') # Убрать нал и бланк
    parents_name = models.CharField('Ф.И.О Родителя', max_length=50)
    passport_details = models.FileField('Паспортные данные', upload_to='passports/')
    file = models.FileField('Заявление', upload_to='applications/')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    school_class = models.IntegerField(default=1, verbose_name='Класс')
    date_of_request = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.student_name

class Contacts(models.Model):
    """Модель контактов"""
    full_name = models.CharField('Ф.И.О', max_length=100)
    position = models.CharField('Должность', max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.full_name

class Questions(models.Model):
    """Модель задаваемых вопросов"""
    CATEGORY_CHOICES = (
        ('1', 'Общие вопросы'),
        ('2', 'Платные услуги'),
        ('3', 'Поступление'),
        ('4', 'Питание'),
    )
    question_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    category =  models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Категория')
    text =  models.TextField(verbose_name='Вопрос')
    email =  models.EmailField(verbose_name='Электронный адрес')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.question_id)



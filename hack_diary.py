import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from datacenter.models import *


def get_schoolkid(name):
    if name:
        try:
            schoolkid = Schoolkid.objects.get(full_name__contains=name)
        except ObjectDoesNotExist:
            print('Ошибка! Ученик отсутствует в базе данных')
        except MultipleObjectsReturned:
            print('Ошибка! Существует несколько учеников с таким именем')
        else:
            return schoolkid
    else:
        print('Ошибка! Не введено имя ученика')


def fix_marks(schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2, 3]
        ).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name, subject_title):
    commendation_list = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        ]
    text = random.choice(commendation_list)

    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_title
            ).order_by('date').reverse()
        if lessons.count() == 0:
            print('Ошибка! В базе не найдено уроков с таким названием.', subject_title)
        else:
            lesson = lessons[0]
            Commendation.objects.create(
                text=text,
                created=lesson.date,
                schoolkid=schoolkid,
                subject=lesson.subject,
                teacher=lesson.teacher
                )


def improve_progress(name):
    schoolkid = get_schoolkid(name)
    if schoolkid:
        fix_marks(schoolkid)
        remove_chastisements(schoolkid)

        subjects = Subject.objects.filter(
            year_of_study=schoolkid.year_of_study
            ).values_list('title', flat=True)
        subject = random.choice(subjects)
        create_commendation(name, subject)

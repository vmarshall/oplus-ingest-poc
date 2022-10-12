# Create your tasks here

from partner_records.models import PartnerRecord

from celery import shared_task

from partner_records.utils import count_partner_patient_data_records, count_partner_doctor_notes, \
    fetch_partner_doctor_notes


@shared_task
def task_partner_record_count():
    res = count_partner_patient_data_records()
    return res

@shared_task
def task_count_partner_doctor_notes():
    res = count_partner_doctor_notes()
    return res


@shared_task
def task_fetch_partner_doctor_notes():
    new_count = fetch_partner_doctor_notes()
    return new_count

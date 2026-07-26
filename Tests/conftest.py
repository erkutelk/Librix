# conftest.py
import pytest
import requests
from random import randint


URL = "http://127.0.0.1:8000/"
KATEGORI_EKLE_URL = f"{URL}categori-add/"
KATEGOR_SIL = f"{URL}categori-delete/"
KATEGORI_GUNCELLE = f"{URL}categori-update/"


@pytest.fixture
def create_category():
    def _create(book_name="erkut", durum=True):

        data = {
            "book_categori": book_name,
            "categori_isActive": durum
        }

        response = requests.post(
            url=KATEGORI_EKLE_URL,
            json=data
        )

        return response

    return _create



@pytest.fixture
def delete_category():
    def _delete(test_value):

        url = f"{KATEGOR_SIL}{test_value}/"

        response = requests.delete(url)

        return response

    return _delete



@pytest.fixture
def update_category(create_category, delete_category):

    def _update(old_name,new_name):

        create_response = create_category(old_name)

        assert create_response.status_code == 201


        url = f"{KATEGORI_GUNCELLE}{old_name}/"

        data = {
            "book_categori": new_name
        }


        response = requests.patch(
            url=url,
            json=data
        )


        delete_category(new_name)

        return response


    return _update
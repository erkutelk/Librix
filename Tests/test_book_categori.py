import pytest
from random import randint

class TestApi:
    random_category_name=randint(1,999)
    def test_kategori_ekle_sil(self,create_category,delete_category):
        category_name = f"erkut{TestApi.random_category_name}"
        response=create_category(category_name)
        slug=response.json()['data']['book_categori']
        assert response.status_code==201


        delete_category=delete_category(slug)
        assert delete_category.status_code==200
        
    def test_ayni_kategoriyi_ekleme(self,create_category,delete_category):
        data=create_category("erkut")
        response=create_category("erkut")

        assert response.status_code==400
        assert (
            response.json()['error']['book_categori'][0]
            ==
            "Aynı kategori adında bir kategori mevcut"
        )
        delete_category("erkut")
        delete_category("erkut")



    def test_olmayan_kategori_silme(self,delete_category):
        response=delete_category("olmayan")
        assert response.status_code==404
        assert response.json()['error']=="Kategori bulunamadı"



    @pytest.mark.parametrize(
        "kategori_name,expected_status,mesaj",
        [
            ("isim",201,"Basariyla Eklendi"),
            ("deneme",201,"Basariyla Eklendi"),
            ("",400,"Bu alan boş bırakılmamalı."),
            ("    ",400,"Bu alan boş bırakılmamalı.")
        ]
    )
    def test_kategori_ekleme(self,kategori_name,expected_status,mesaj,create_category,delete_category):
        response=create_category(kategori_name)
        body=response.json()
        assert response.status_code==expected_status
        if response.status_code==201:
            assert body['status']==mesaj
            delete_category(kategori_name)

        else:
            assert body['error']['book_categori'][0]==mesaj



    def test_emoji_kontrol(
        self,
        create_category
    ):

        response=create_category(
            "😊😊😊😊"
        )


        assert response.status_code==400

        assert (
            response.json()['error']['book_categori'][0]
            ==
            "Kategori emojilerden oluşamaz"
        )
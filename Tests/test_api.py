import pytest
import requests


class TestApi:

    URL = "http://127.0.0.1:8000/book-categori/"
    KATEGORI_EKLE = "categori-add/"
    KATEGOR_SIL = "categori-delete/"
    KATEGORI_GUNCELLE = "categori-update/"

    @pytest.fixture
    def create_category(self):
        def _create(test_value="erkut", durum=True):
            data = {
                "book_categori": test_value,
                "categori_isActive": durum
            }
            url = f"{self.URL}{self.KATEGORI_EKLE}"
            response=requests.post(url=url, json=data)
            print('Kategori Eklendi')
            return response

        return _create

    @pytest.fixture
    def delete_category(self):
        def _delete(test_value):
            url = f"{self.URL}{self.KATEGOR_SIL}{test_value}/"
            response = requests.delete(url)
            print('Kategori Silindi')
            return response

        return _delete

    def test_kategori_duzenle(self,create_category,delete_category):
        '''Eklenen bir kategoriyi silmek ve güncellemek'''
        ornek_veri='erkut_elik'
        create_response=create_category(ornek_veri)

        slug_ = create_response.json()
        url = f"{self.URL}{self.KATEGORI_GUNCELLE}{ornek_veri}/"

        data = {
            "book_categori": "naberererer"
        }

        response = requests.patch(url=url, json=data)
        assert response.status_code == 200

        delete_category('naberererer')

    def test_eklenen_kategoriyi_sil(self, create_category, delete_category):
        '''Kategoriye eklenen değer başarıli bir şeklde siliniyor mu?'''
        ekle=create_category("erkut")
        response = delete_category("erkut")

        print('Eklenen değer',ekle.status_code)
        print('silinen değer',response.status_code)
        assert response.status_code in [201,200]

    def test_ayni_kategoriyi_tekrar_ekleme(self,create_category):
        '''Kategoyiye aynı isimde bir kategori ekleme'''
        first_value=create_category('erkut')
        last_value=create_category('erkut')

        assert last_value.json()['status']['book_categori'][0]=="Aynı kategori adında bir kategori mevcut"

    def test_olmayan_kategoriyi_silme(self,delete_category):
        '''Eğer bir kategori mevcut olmadığı halde silmeye çalışırsa kullanıcı bu hatayı versin'''
        last_value=delete_category('olmaayan_deger')
        assert last_value.json()['status']=='Kategori bulunamadı'
        assert last_value.status_code==404

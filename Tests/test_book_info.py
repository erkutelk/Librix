import pytest
import requests
from random import randint

class TestBookInfo:
    URL         =   "http://127.0.0.1:8000"
    GET_ALL     =   f"{URL}/book-all/"
    GET_POST    =   f"{URL}/book-add/"
    GET_DELETE  =   f"{URL}/book-delete/"
    GET_PATCH   =   f"{URL}/book-update/"
    GET_FIRST   =   f"{URL}/book-get/"
    GET_SEARCH  =   f"{URL}/search/"

    @pytest.fixture
    def create_book_info(self):
        import random
        def _create(book_name=f"erkut{random.randint(1000,9999)}",
                    barcode=random.randint(1000,9999),
                    price=12,
                    write=1,
                    kategori=1,
                    stock=1,
                    description='Bur bir açıklama',
                    language=1
                    ):
            data = {
                "book_name": book_name,
                "barcode": f"1231{barcode}",
                "price": price,
                "writer_book": write,
                "kategori": kategori,
                "language": language,
                "stock": stock,
                "description": description
            }
            try:
                response = requests.post(url=TestBookInfo.GET_POST,json=data)
                return response

            except Exception as e:
                return {'erorr':f'Hata meydana geldi{e}'}

        return _create

    @pytest.fixture
    def book_info_delete(self):
        'kitap silme fixture'
        def _delete(slug):
            url_=f'{TestBookInfo.GET_DELETE}{slug}/'
            response=requests.delete(url=url_)
            return response

        return _delete

    def test_kitap_ekleme(self, create_book_info,book_info_delete):
        "Yeni bir kitap ekleme"
        add_response=create_book_info()
        delete_slug=add_response.json['data']['book_slug']
        delete_response=book_info_delete(delete_slug)

    def test_kitap_silme(self,create_book_info,book_info_delete):
        'yeni bir kitap ekle ve kitabı sil'
        ekle_=create_book_info()
        assert ekle_.status_code==201
        assert ekle_.json()['status']=='Başarıyla yeni kitap eklendi'
        slug=ekle_.json()['data']['book_slug']

        sil=book_info_delete(slug)
        assert sil.status_code==200
        assert sil.json()['message']=='Kitap silindi'


    def test_ayni_isimde_kitap_ekleme(self,create_book_info,book_info_delete):
        first_book=create_book_info()
        assert first_book.status_code==201

        slug=first_book.json()['data']['book_slug']
        ikinci=create_book_info(slug)
        assert ikinci.status_code==400
        print(ikinci.json())
        silme=book_info_delete(slug)
        assert silme.status_code==200

    def test_kitap_düzenleme(self,create_book_info,book_info_delete):
        "bir kitap ekle ve üzerinde güncelleme yap"
        from time import sleep
        new_book=create_book_info()
        assert new_book.status_code==201
        assert new_book.json()['status']=='Başarıyla yeni kitap eklendi',new_book.text


        guncel_veriler={
            'book_name':'isim_12321'
        }


        eski_slug=new_book.json()['data']['book_slug']
        response=requests.patch(url=f'{self.GET_PATCH}{eski_slug}/',json=guncel_veriler)

        assert response.status_code==200
        assert response.json()['status']=='Güncelleme işlemi tamamlandı'

        response=response.json()['data']['book_slug']

        sil_=book_info_delete(response)
        assert sil_.status_code==200
        assert sil_.json()['message']=='Kitap silindi'



    def test_kitap_search(self,create_book_info,book_info_delete):
        yeni_eklenen_kitap=create_book_info('bu deneme yazısıdır')
        ara=requests.get(url=f'{self.GET_SEARCH}{yeni_eklenen_kitap.json()['data']['book_slug']}',)
        new_add_book=yeni_eklenen_kitap.json()['data']
        search_value=ara.json()['data'][0]

        assert search_value['book_slug']==new_add_book['book_slug'],'book_slug değerinde hata meydana geldi'
        assert search_value['book_name']==new_add_book['book_name'],'book_name değerinde hata meydana geldi'
        assert search_value['barcode']==new_add_book['barcode'],'barcode değerinde hata meydana geldi'
        assert search_value['price']==new_add_book['price'],'price değerinde hata meydana geldi'
        assert search_value['writer']==new_add_book['writer'],'writer değerinde hata meydana geldi'
        assert search_value['kategori']==new_add_book['kategori'],'kategori değerinde hata meydana geldi'



        book_info_delete(new_add_book['book_slug'])
        






# {
# "book_name": book_name,
# "barcode": f'1231{barcode}',
# "price": price,
# "kategori": kategori,
# "stock":1,
# "writer_book_id":1
# }






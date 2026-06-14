import pytest
import requests


class TestBookInfo:
    URL = "http://127.0.0.1:8000/book-categori"
    GET_ALL = f"{URL}/book-all/"
    GET_POST = f"{URL}/book-add/"
    GET_DELETE = f"{URL}/book-delete/"
    GET_PATCH = f"{URL}/book-update/"
    GET_FIRST = f"{URL}/book-get/"
    GET_SEARCH=f"{URL}/search/"

    @pytest.fixture
    def create_book_info(self):
        "Yeni kitap oluşturma fixture"
        import random
        def _create(book_name="test123",barcode=random.randint(1000,9999),price=12,write="Kitap yazarı test",kategori=1,stock=1):
            data = {
                "book_name": book_name,
                "barcode": f'1231{barcode}',
                "price": price,
                "kategori": kategori,
                "stock":1,
                "writer_book_id":1
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
        VALUE='erkut-elik-deneme'
        add_response=create_book_info(VALUE)
        delete_response=book_info_delete(VALUE)

    def test_kitap_silme(self,create_book_info,book_info_delete):
        'yeni bir kitap ekle ve kitabı sil'
        VALUE='Erkut Elik Yazı'
        ekle_=create_book_info(VALUE)
        assert ekle_.status_code==201
        assert ekle_.json()['status']=='Başarıyla yeni kitap eklendi'
        slug=ekle_.json()['data']['book_slug']

        sil=book_info_delete(slug)
        assert sil.status_code==200
        assert sil.json()['message']=='Kitap silindi'


    def test_ayni_isimde_kitap_ekleme(self,create_book_info,book_info_delete):
        "Yeni bir kitap ekleme"
        from time import sleep
        VALUE='eererewew'
        deger1=create_book_info(VALUE)
        assert deger1.status_code==201
        assert deger1.json()['status']=='Başarıyla yeni kitap eklendi'
        sleep(2)
        deger=create_book_info(VALUE)
        assert deger.status_code==400
        assert deger.json()['status']=='hata meydana geldi'
        sleep(2)
        silme=book_info_delete(VALUE)

    def test_kitap_düzenleme(self,create_book_info,book_info_delete):
        "bir kitap ekle ve üzerinde güncelleme yap"
        from time import sleep
        new_book=create_book_info('isim')
        assert new_book.status_code==201,new_book.text
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
        















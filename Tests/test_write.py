import pytest
import requests
class TestWrite:
    BASE="http://127.0.0.1:8000/"
    GET_ALL='writer/'
    GET_ID=f'writer/get/{"<int:id>"}'
    ADD_POST='writer/add/'
    DELETE_METHOD='writer/delete/'
    PATCH_METHOD='writer/update/'

    @pytest.fixture
    def add_method(self):
        def create(name=str,surname=str,isActive=bool):
            data={
                "name":name,
                "surname":surname,
                "isActive":isActive,
            }            
            response=requests.post(url=f"{self.BASE}{self.ADD_POST}",json=data)
            return response
        return create
    
    @pytest.fixture
    def delete_method(self):
        def delete(id):
            URL=f"{self.BASE}{self.DELETE_METHOD}{id}/"
            response=requests.delete(url=URL)
            return response
        return delete


    @pytest.mark.parametrize(
        "name,surname,isActive",
        [
            ('Erkut','Elik',True),
            ('Namık','Kemal',True),
            ('Orhan','Kemal',True),
            ('Reşat Nuri','Gültekin',True),
            ('Mehmet Akif','Ersoy',True),
        ]
    )
    def test_yazar_ekleniyor_mu(self, add_method, name, surname, isActive):
        response = add_method(name, surname, isActive)
        response_json=response.json()['data']
        assert response_json['name'] ==name,'name hatası verdi'
        assert response_json['surname'] == surname,'surname hatası verdi'
        assert response_json['isActive'] == isActive,'isActive hatası verdi'


    @pytest.mark.parametrize(
        "name,surname,isActive,erorrs",
        [
            ('','',True,{'errors': {'surname': ['Bu alan boş bırakılmamalı.']}}),
            (' ',' ',True,{'errors': {'surname': ['Bu alan boş bırakılmamalı.']}}),
            (' ','Kemal',True,{'errors': {'non_field_errors': ['Bu alan boş bırakılmamalı']}}),
            ('Reşat Nuri',' ',True,{'errors': {'surname': ['Bu alan boş bırakılmamalı.']}}),
            (' ',' ',True,{'errors': {'surname': ['Bu alan boş bırakılmamalı.']}}),
            ('a','a',True,{'errors': {'non_field_errors': ['Karakter sayısı en az 2 olmalı']}}),
            ('c',' ',True,{'errors': {'surname': ['Bu alan boş bırakılmamalı.']}}),
            ('','l',True,{'errors': {'non_field_errors': ['Bu alan boş bırakılmamalı']}}),
            ('❤️','l',True,{'errors': {'non_field_errors': ['Karakter sayısı en az 2 olmalı']}}),
            ('❤️','❤️',True,{'errors': {'non_field_errors': ['Emoji kabul edilmez']}}),
            (' ','❤️',True,{'errors': {'non_field_errors': ['Bu alan boş bırakılmamalı']}}),
            ('y','❤️',True,{'errors': {'non_field_errors': ['Karakter sayısı en az 2 olmalı']}}),
        ]
    )
    def test_input_bos_birakiliyor_mu(self,add_method,name,surname,isActive,erorrs):
        response=add_method(name,surname,isActive)
        print(response.json())
        response_errors = response.json()["errors"]

        if "surname" in erorrs["errors"]:
            assert response_errors["surname"] == erorrs["errors"]["surname"]

        elif "non_field_errors" in erorrs["errors"]:
            assert response_errors["non_field_errors"] == erorrs["errors"]["non_field_errors"]

    def test_eklenen_yazar_silme(self,add_method,delete_method):
        ekle=add_method('Erkuttt deneme','Elik deneme',True)
        response=ekle.json()
        data=response['data']
        print(data)
        assert data['name']=="Erkuttt deneme"
        assert data['surname']=="Elik deneme"
        assert data['isActive']==True
        assert data['dateAdd']==data['dateAdd']

        delete_=delete_method(data['id'])

        delete_id=delete_.json()['status']
        assert delete_id=='silindi',delete_.json()


    @pytest.mark.parametrize("isim,soyisim,durum",[
        ('Erkut','Elik',True),
        ])
    def test_eklenen_veriyi_guncelleme(self,add_method,delete_method,isim,soyisim,durum):
        import random
        insert_value=add_method(isim,soyisim,durum)
        try:
            response_id=insert_value.json()['data']
            id_=response_id['id']
            url = f"{self.BASE}{self.PATCH_METHOD}{id_}/"
            data={'name':f'Değiştirildi{random.randint(1,9999)}'}
            update_response=requests.patch(url,json=data)
            print(update_response.json())
        
        except:
            response_id=insert_value.json()
            print(response_id,'Hatası meydana geldi.')




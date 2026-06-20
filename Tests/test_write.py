import pytest
import requests
class TestWrite:
    BASE="http://127.0.0.1:8000/"
    GET_ALL=f'{BASE}writer/'
    GET_ID=f'{BASE}writer/get/{"<int:id>"}'
    ADD_POST=f'{BASE}writer/add/'
    DELETE_METHOD=f'{BASE}writer/delete/'
    PATCH_METHOD=f'{BASE}writer/update/'

    @pytest.fixture
    def add_method(self):
        def create(name=str,surname=str,isActive=bool):
            data={
                "name":name,
                "surname":surname,
                "isActive":isActive,
            }            
            response=requests.post(url=f"{self.ADD_POST}",json=data)
            return response
        return create
    
    @pytest.fixture
    def delete_method(self):
        def delete(id):
            URL=f"{self.DELETE_METHOD}{id}/"
            response=requests.delete(url=URL)
            return response
        return delete


    @pytest.mark.parametrize(
        "name,surname,isActive",
        [
            ('Namık','Kemal',True),
            ('Orhan','Kemal',True),
            ('Reşat Nuri','Gültekin',True),
            ('Mehmet Akif','Ersoy',True),
        ]
    )
    def test_yazar_ekleniyor_mu(self, add_method, name, surname, isActive,delete_method):
        try:
            response = add_method(name, surname, isActive)
            response_json=response.json()['data']
            assert response_json['name'] ==name,'name hatası verdi'
            assert response_json['surname'] == surname,'surname hatası verdi'
            assert response_json['isActive'] == isActive,'isActive hatası verdi'
        except Exception as e:
            print(e,'Hata meydana geldi')
        finally:
            writer_id=response_json['id']
            delete_method(writer_id)


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

    @pytest.mark.parametrize("isim,soyisim,durum",[(f'Erkut','Eliksss',True),])
    def test_eklenen_veriyi_guncelleme(self,add_method,delete_method,isim,soyisim,durum):
        import random
        insert_value=add_method(isim,soyisim,durum)
        print(insert_value.json())
        assert insert_value.status_code in (200,201),'veri eklenmedi'

        response=insert_value.json()['data']
        url = f"{self.PATCH_METHOD}{response['id']}/"
        random_value=f'Değiştirildi{random.randint(1,9999)}'
        data={'surname':random_value}
        update_response=requests.patch(url=url,json=data)

        
        assert update_response.status_code in (201,200),'veri güncellenmedi'
        assert update_response.status_code==200,'Güncellemede hata meydana geldi'
        assert response['name']=='Erkut','name değerinde hata meydana geldi'
        assert data['surname']==random_value
        assert response['dateAdd']==update_response.json()['data']['dateAdd'],'dateAdd değerinde hata meydana geldi'
        assert response['isActive']==True
        delete_method(response['id'])




    @pytest.mark.parametrize('isim,soyisim,isActive',
        [
            ('Erkut TEST','Elik TEST',True),
            ('Namık TEST','Kemal TEST',True),
            ('Orhan TEST','Kemal TEST',True),
            ('Reşat Nuri TEST','Gültekin TEST ',True),
            ('Mehmet Akif TEST','Ersoy TEST',True),
        ]
    )
    def test_butun_yazarlari_getirme(self,isim,soyisim,isActive,add_method,delete_method):
        url=f'{self.GET_ALL}'
        try:
            add_writer=add_method(isim,soyisim,isActive)
            response=requests.get(url=url)
            json_data=add_writer.json()['data']
        except Exception as e:
            print('hata meydana geldi',e)
        finally:
            assert response.status_code==200,'Bütün yazarlar getiriliken hata meydana geldi'
            assert len(json_data)==5
            delete_method(json_data['id'])



import pytest
import requests


class TestUser:
    BASE='http://127.0.0.1:8000/'
    ADMIN_LOGIN=f'{BASE}user/login/'
    CREATE_USER_URL=f'{BASE}user/create/'
    USER_LIST_URL=f'{BASE}user/list/'
    USER_DEACTIVE_URL=f'{BASE}user/deactive/'

    @pytest.fixture
    def login_admin(self):
        def login_Admin():
            data={'username':'admin','password':'admin'}
            admin_response=requests.post(self.ADMIN_LOGIN,data=data)
            access=admin_response.json()['access']
            refresh=admin_response.json()['refresh']
            return {"access":access,
                    "refresh":refresh,
                    "status_code":admin_response.status_code}
        return login_Admin
    


    @pytest.fixture
    def kullanici_olustur(self,login_admin):
        def crete_user():
            token=login_admin()['access']
            headers={
                "Authorization": f"Bearer {token}"}
            data={"username":"denaskullanici",
                  "lastname":"iisesmas",
                "password":"123211251",
                "phone":"55379888840",
                "relative_id_number":"14318888344",
                "role":"user"}
            
            response=requests.post(url=self.CREATE_USER_URL,json=data,headers=headers)
            return response
        return crete_user


    def test_tum_kullanicilari_gor(self,login_admin):
        token=login_admin()['access']
        status=login_admin()['status_code']
        assert status==200
        headers={
                "Authorization": f"Bearer {token}"}
        
        response=requests.get(url=self.USER_LIST_URL,headers=headers)
        print(response.json()),
        assert response.status_code==200,'hata kullanıcılar yüklenirken hata meydana geldi'
        print(response.status_code)

    def test_kullanici_pasife_al(self,login_admin):
        token=login_admin()['access']
        headers={"Authorization": f"Bearer {token}"}
        response=requests.patch(url=f'{self.USER_DEACTIVE_URL}{12}/'.format(),headers=headers)
        assert response.status_code==200,'Kullanıcı pasife alınamadı'
        assert response.json()['status']=='Kullanıcı pasif hale getirildi','Beklenen status kodu gelmedi'



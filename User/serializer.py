from rest_framework import serializers
from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    bekleyen_kitap_sayisi=serializers.IntegerField()
    class Meta:
        model = UserInfo
        fields = [
            'id',
            'username',
            'last_name',
            'phone',
            'role',
            'is_active',
            'bekleyen_kitap_sayisi'
        ]



class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True,
                                     required=True,
                                     allow_blank=False,#Boş stringe izin vermemek için kullanılıyor
                                     error_messages={
                                     "blank":"Şifre boş olamaz",
                                     "required":"Şifre zorunlu alandır"})
    
    password2=serializers.CharField(write_only=True,
                                     required=True,
                                     allow_blank=False,#Boş stringe izin vermemek için kullanılıyor
                                     error_messages={
                                     "blank":"Şifre boş olamaz",
                                     "required":"Şifre zorunlu alandır"})
    
    username=serializers.CharField(write_only=False,
                                     required=True,
                                     allow_blank=False,#Boş stringe izin vermemek için kullanılıyor
                                     error_messages={
                                     "blank":"Kullanıcıadı kısmı boş olamaz",
                                     "required":"Şifre zorunlu alandır"})
    last_name=serializers.CharField(write_only=False,
                                     required=True,
                                     allow_blank=False,#Boş stringe izin vermemek için kullanılıyor
                                     error_messages={
                                     "blank":"lastname kısmı boş olamaz",
                                     "required":"lastnama zorunlu alandır"})
    phone=serializers.CharField(write_only=False,
                                     required=True,
                                     allow_blank=False,#Boş stringe izin vermemek için kullanılıyor
                                     error_messages={
                                     "blank":"telefon alanı boş bırakılamaz",
                                     "required":"Telefon numaranızı giriniz"})
    class Meta:
        model = UserInfo
        fields = ["username","last_name", "password1","password2", "phone", "relative_id_number"]

    def validate(self, data):
        password1=data['password1']
        password2=data['password2']
        if password1 != password2:
            raise serializers.ValidationError('Girilen parolalar farklı')

        return data

    def create(self, validated_data):
        password = validated_data["password1"]
        user = UserInfo.objects.create_user(
            username=validated_data["username"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            relative_id_number=validated_data["relative_id_number"],
            password=password,
            role="user"
        )

        return user
    


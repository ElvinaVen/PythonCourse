from rest_framework import serializers

from vehicle.models import Car, Moto, Milage

from vehicle.validators import TitleValidator

from vehicle.services import convert_currencies


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(
        source="milage.all.first.milage", read_only=True
    )  # 1 метод вычисляемое значение
    milage = MilageSerializer(many=True, read_only=True)
    usd_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = "__all__"


    def get_usd_price(self, instance):
        return convert_currencies(instance.price)


class MotoSerializer(serializers.ModelSerializer):
    last_milage = (
        serializers.SerializerMethodField()
    )  # 2 метод подгрузка из связ.модели

    class Meta:
        model = Moto
        fields = "__all__"

    @staticmethod
    def get_last_milage(obj):
        if obj.milage.all().first():
            return obj.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = (
            "milage",
            "year",
            "moto",
        )


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = "__all__"
        validators = [
            TitleValidator(field="title"),
            serializers.UniqueTogetherValidator(
                fields=["title", "description"], queryset=Moto.objects.all()
            ),
        ]

    def create(self, validated_data):
        milage = validated_data.pop("milage")
        moto_item = Moto.objects.create(**validated_data)
        for m in milage:
            Milage.objects.create(**m, moto=moto_item)
        return moto_item

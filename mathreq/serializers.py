from rest_framework import serializers
from mathreq.models import MathReq, LANGUAGE_CHOICES, STYLE_CHOICES
from math import factorial


class MathReqSerializer(serializers.Serializer):

    class Meta:
        model = MathReq
        fields = ('id', 'title', 'code', 'value','input','output')

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    output = serializers.CharField(required=False, allow_blank=True, max_length=100)
    input = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        code = validated_data.get('code')
        return MathReq.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.output = validated_data.get('output', instance.output)
        instance.input = validated_data.get('input', instance.input)
        instance.save()
        return instance
# -*- coding: utf-8 -*-
from rest_framework import serializers
from mathreq.models import MathReq, LANGUAGE_CHOICES, STYLE_CHOICES


class MathReqSerializer(serializers.Serializer):

    class Meta:
        model = MathReq
        fields = ('input')

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(required=False, allow_blank=True, max_length=100)
    output = serializers.CharField(required=False, allow_blank=True, max_length=100)
    input = serializers.CharField(required=False, allow_blank=True, max_length=100)
    error_msg = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        code = validated_data.get('code')
        return MathReq.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.output = validated_data.get('output', instance.output)
        instance.input = validated_data.get('input', instance.input)
        instance.error_msg = validated_data.get('error_msg', instance.error_msg)

        instance.save()
        return instance
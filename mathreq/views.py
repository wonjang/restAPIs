# -*- coding: utf-8 -*-
from math import factorial

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mathreq.models import MathReq
from mathreq.serializers import MathReqSerializer


class MathReqList(APIView):
    def get(self, request, format=None):
        math_reqs = MathReq.objects.all()
        serializer = MathReqSerializer(math_reqs, many=True)
        return Response(serializer.data)

class MathReqFactorial(APIView):
    """
    post 인수로 input 을 추가해서 1개의 숫자를 입력한다.
    """
    serializer_class = MathReqSerializer
    def get(self, request, format=None):
        math_reqs = MathReq.objects.filter(code=u'factorial')
        serializer = MathReqSerializer(math_reqs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        input_value = request.data['input']
        request.data['code'] = u'factorial'
        request.data['output'] = self.calc_factorial(input_value)
        serializer = MathReqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def calc_factorial(self,input_value):
        return  str(factorial(int(input_value)))


class MathReqCombination(APIView):
    """
    post 인수로 input 을 추가해서 ',' 를 구분자로 2개의 숫자를 입력한다.
    """
    serializer_class = MathReqSerializer
    def get(self, request, format=None):
        math_reqs = MathReq.objects.filter(code=u'combination')
        serializer = MathReqSerializer(math_reqs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        input_value = request.data['input']
        request.data['output'] = self.calc_combination(input_value)
        request.data['code'] = u'combination'
        serializer = MathReqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calc_combination(self,input_value):
        try:
            temp = input_value.split(",")
            first = int(temp[0])
            second = int(temp[1])
            return str(factorial(first) / factorial(second) / factorial(first - second))
        except:
            self.request.data['error_msg'] = "please input value like 10,2"
            return 0


class MathReqDetail(APIView):
    def get_object(self, pk):
        try:
            return MathReq.objects.get(pk=pk)
        except MathReq.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        math_req = self.get_object(pk)
        serializer = MathReqSerializer(math_req)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        math_req = self.get_object(pk)
        serializer = MathReqSerializer(math_req, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        math_req = self.get_object(pk)
        math_req.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
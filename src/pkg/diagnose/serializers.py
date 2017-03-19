from rest_framework import serializers
from pkg.diagnose.models import Diagnose
from pkg.diagnose.models import DiagnoseFile


class DiagnoseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnoseFile
        fields = ('id', 'file', 'diagnose')


class DiagnoseSerializer(serializers.ModelSerializer):
    files = DiagnoseFileSerializer(many=True, read_only=True)

    class Meta:
        model = Diagnose
        fields = ('id', 'text', 'files')

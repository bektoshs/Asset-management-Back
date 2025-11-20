from rest_framework import serializers
from .models import Department, Location, Employee, Device


class EmployeeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "position",
            "email",
            "phone",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeMiniSerializer(many=True, read_only=True)
    employee_count = serializers.IntegerField(source='employees.count', read_only=True)
    class Meta:
        model = Department
        fields = "__all__"


class DepartmentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class DeviceMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentMiniSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="department",
        write_only=True,
    )

    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location",
        write_only=True,
    )

    devices = DeviceMiniSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = [
            "id", "first_name", "last_name",
            "email", "phone", "position",
            "department", "department_id",
            "location", "location_id",
            "created_at", "devices",
        ]


class DeviceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source="employee",
        write_only=True,
        required=False,
    )

    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="department",
        write_only=True,
        required=False,
    )

    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location",
        write_only=True,
        required=False,
    )

    class Meta:
        model = Device
        fields = "__all__"

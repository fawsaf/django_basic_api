from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data})
        return Response({'status': 400, 'payload': serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({'status': 404, 'message': 'Employee not found'})

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response({'status': 200, 'payload': serializer.data})

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response({'status': 400, 'errors': serializer.errors})

    elif request.method == 'DELETE':
        employee.delete()
        return Response({'status': 204, 'message': 'Deleted'})

    return Response({'status': 405, 'message': 'Method Not Allowed'})

@api_view(['GET', 'POST'])
def vacations(request):
    if request.method == 'GET':
        vacations = Vacation.objects.all()
        serializer = VacationSerializer(vacations, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    elif request.method == 'POST':
        employee_id = request.data.get('employee')  # Replace with the actual field name for the employee ID in the request data
        max_vacation_count = 4  # Replace with the desired maximum vacation count
        try:
            employee = Employee.objects.get(id=employee_id)
            current_vacation_count = Vacation.objects.filter(employee=employee).count()

            if current_vacation_count >= max_vacation_count:
                return JsonResponse({'error': 'Maximum vacation request limit reached'}, status=400)

        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)

        serializer = VacationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response({'status': 400, 'errors': serializer.errors})

@api_view(['GET', 'PUT', 'DELETE'])
def vacation_detail(request, id):
    try:
        vacation = Vacation.objects.get(id=id)
    except Vacation.DoesNotExist:
        return Response({'status': 404, 'message': 'Vacation not found'})

    if request.method == 'GET':
        serializer = VacationSerializer(vacation)
        return Response({'status': 200, 'payload': serializer.data})

    elif request.method == 'PUT':
        serializer = VacationSerializer(vacation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response({'status': 400, 'errors': serializer.errors})

    elif request.method == 'DELETE':
        vacation.delete()
        return Response({'status': 204, 'message': 'Deleted'})

@api_view(['GET'])
def get_vacation_status(request, id):
    try:
        vacation = Vacation.objects.get(id=id)
        status = vacation.status
        return JsonResponse({'status': status})
    except Vacation.DoesNotExist:
        return JsonResponse({'error': 'Vacation request not found'}, status=404)

from django.http import JsonResponse
from .models import Employee, Vacation

@api_view(['GET'])
def get_employee_vacation_count(request, id):
    try:
        employee = Employee.objects.get(id=id)
        vacation_count = Vacation.objects.filter(employee=employee).count()
        return JsonResponse({'count': vacation_count})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)


from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from ..models import Guest
from .GuestSerializer import GuestSerializer
from rest_framework import serializers
from rest_framework import status
@api_view(['GET'])

def ApiOverview(request):
	api_urls = {
		'all_guests': '/',
		'Search by name': '/?name=name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/guest/pk/delete'
	}

	return Response(api_urls)


@api_view(['POST'])
def add_guests(request):
	guest = GuestSerializer(data=request.data)

	# validating for already existing data
	if Guest.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if guest.is_valid():
		guest.save()
		return Response(guest.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_guests(request):
    # checking for the parameters from the URL
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests, many=True)

    # if there is something in items else raise error
    if guests:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_guests(request, pk):
	guests = Guest.objects.get(pk=pk)
	data = GuestSerializer(instance=guests, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_guests(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.delete()
    return Response(status=status.HTTP_202_ACCEPTED)